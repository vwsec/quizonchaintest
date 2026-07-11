"use client"

import { useCallback, useEffect, useState, useRef } from "react"
import { ErrorBoundary } from "react-error-boundary"
import { HomeScreen } from "@/components/home-screen"
import { QuizScreen } from "@/components/quiz-screen"
import { ResultsScreen } from "@/components/results-screen"
import type { Question } from "@/lib/quiz-data"
import { useChainId, useAccount, usePublicClient, useSignMessage } from "wagmi"
import { getTimeUntilNextSubmissionSeconds } from "@/lib/submitScore"
import type { Hex } from "viem"

type Screen = "home" | "quiz" | "results"

type GenerateQuizApiQuestion = {
  id?: number
  question: string
  options: string[]
  correctIndex?: number
}

type GenerateQuizApiResponse = {
  error?: string
  questions?: GenerateQuizApiQuestion[]
  quizToken?: string
  ecosystem?: string
  startIndex?: number
}

function normalizeQuestions(raw: GenerateQuizApiQuestion[]): Question[] {
  return raw.map((q, i) => ({
    id: q.id ?? i + 1,
    question: q.question,
    options: q.options,
    correctIndex: q.correctIndex ?? 0,
  }))
}

function QuizApp() {
  const [mounted, setMounted] = useState(false)
  useEffect(() => setMounted(true), [])

  const chainId = useChainId()
  const chainIdRef = useRef(chainId)
  useEffect(() => {
    chainIdRef.current = chainId
  }, [chainId])

  const { isConnected } = useAccount()
  const { signMessageAsync } = useSignMessage()
  const [screen, setScreen] = useState<Screen>("home")
  const [finalScore, setFinalScore] = useState(0)
  const [userAnswers, setUserAnswers] = useState<number[]>([])
  const [questions, setQuestions] = useState<Question[]>([])
  const [quizToken, setQuizToken] = useState<string | null>(null)
  const [startIndex, setStartIndex] = useState<number | null>(null)
  const [ecosystem, setEcosystem] = useState<string | null>(null)
  const [sessionSignature, setSessionSignature] = useState<Hex | null>(null)
  const [quizLoading, setQuizLoading] = useState(false)
  const [quizError, setQuizError] = useState<string | null>(null)
  const [globalRefreshKey, setGlobalRefreshKey] = useState(0)

  const [cooldownRemaining, setCooldownRemaining] = useState(0)
  const [isCheckingCooldown, setIsCheckingCooldown] = useState(true)
  const [isSigning, setIsSigning] = useState(false)
  const [verifyError, setVerifyError] = useState<string | null>(null)
  const publicClient = usePublicClient()
  const { address } = useAccount()

  const fetchQuiz = useCallback(async () => {
    setQuizLoading(true)
    setQuizError(null)
    const controller = new AbortController()
    const timeout = setTimeout(() => controller.abort(), 60_000)
    try {
      const params = new URLSearchParams({ chainId: String(chainId) })
      if (address) params.set("address", address.toLowerCase())
      const res = await fetch(`/api/generate-quiz?${params}`, {
        signal: controller.signal,
      })
      if (!res.ok) {
        const text = await res.text()
        if (res.status === 429) {
          throw new Error("Too many quizzes generated recently. Please wait a moment and try again.")
        }
        throw new Error("Couldn't load the quiz right now. Please try again.")
      }
      const data = (await res.json()) as GenerateQuizApiResponse
      if (!data.questions?.length) {
        throw new Error("Something went wrong loading the quiz. Please try again.")
      }
      if (!data.quizToken) {
        throw new Error("Something went wrong loading the quiz. Please try again.")
      }
      
      // Safety: Only update state if we are still on the same chain as when the request started
      if (chainIdRef.current !== chainId) {
        return;
      }

      // Final dynamic safety check: Verify the ecosystem returned by API matches our current chain
      const expectedEcosystem = 
        chainId === 8453 ? "Base" :
        chainId === 130 ? "Unichain" :
        chainId === 1868 ? "Soneium" :
        [57073].includes(chainId) ? "Ink" : null;

      if (expectedEcosystem && data.ecosystem && data.ecosystem !== expectedEcosystem) {
        console.warn(`[QuizApp] Ecosystem mismatch: expected ${expectedEcosystem}, got ${data.ecosystem}. Retrying...`)
        return void fetchQuiz();
      }

      setQuestions(normalizeQuestions(data.questions))
      setQuizToken(data.quizToken)
      if (data.ecosystem) setEcosystem(data.ecosystem)

      // Store the start index — session signature is handled on connect
      if (address && data.startIndex != null) {
        setStartIndex(data.startIndex)
      } else {
        setStartIndex(null)
      }
    } catch (e) {
      if (chainIdRef.current !== chainId) return;
      if (e instanceof Error && e.name === "AbortError") {
        setQuizError("Request timed out. Please try again.")
      } else {
        setQuizError(e instanceof Error ? e.message : "Something went wrong loading the quiz. Please try again.")
      }
      setQuestions([])
      setQuizToken(null)
      setStartIndex(null)
    } finally {
      clearTimeout(timeout)
      setQuizLoading(false)
    }
  }, [chainId, address])

  // Automatically clear rate limit error after 60 seconds
  useEffect(() => {
    if (quizError?.includes("Too many quizzes")) {
      const timer = setTimeout(() => {
        setQuizError(null)
      }, 60000)
      return () => clearTimeout(timer)
    }
  }, [quizError])

  useEffect(() => {
    setQuestions([])
    setQuizToken(null)
    setStartIndex(null)
    setEcosystem(null)
    setSessionSignature(null)
    setQuizError(null)
    setFinalScore(0)
    setUserAnswers([])
    setScreen("home")
  }, [chainId])

  // Fetch cooldown status from on-chain
  useEffect(() => {
    let cancelled = false
    const readCooldown = async () => {
      if (!isConnected || !address) {
        if (!cancelled) {
          setCooldownRemaining(0)
          setIsCheckingCooldown(false)
        }
        return
      }
      setIsCheckingCooldown(true)
      const seconds = await getTimeUntilNextSubmissionSeconds({
        chainId,
        player: address,
        publicClient,
      })
      if (!cancelled) {
        setCooldownRemaining(Math.max(0, seconds))
        setIsCheckingCooldown(false)
      }
    }
    void readCooldown()
    return () => {
      cancelled = true
    }
  }, [isConnected, address, chainId, publicClient, globalRefreshKey])

  // Cross-tab cooldown sync logic
  useEffect(() => {
    const handleStorage = (e: StorageEvent) => {
      if (e.key === 'quiz-cooldown-sync') {
        setGlobalRefreshKey(k => k + 1)
      }
    }
    window.addEventListener('storage', handleStorage)
    return () => window.removeEventListener('storage', handleStorage)
  }, [])

  // Timer for cooldown
  useEffect(() => {
    if (cooldownRemaining <= 0) return
    const timer = setInterval(() => {
      setCooldownRemaining((prev) => Math.max(0, prev - 1))
    }, 1000)
    return () => clearInterval(timer)
  }, [cooldownRemaining])

  // Auto-fetch quiz when connected, signed, and cooldown is done
  useEffect(() => {
    if (isConnected && sessionSignature && questions.length === 0 && !quizLoading && !quizError && cooldownRemaining === 0 && !isCheckingCooldown) {
      void fetchQuiz()
    }
  }, [isConnected, sessionSignature, fetchQuiz, questions.length, quizLoading, quizError, cooldownRemaining, isCheckingCooldown])

  const handleVerify = useCallback(async () => {
    if (!address) return
    setIsSigning(true)
    setVerifyError(null)
    try {
      const message = `QuizonChain Session:${address}`
      const sig = await signMessageAsync({ message })
      setSessionSignature(sig)
    } catch {
      setVerifyError("Signature was rejected. You must sign to verify your wallet.")
    } finally {
      setIsSigning(false)
    }
  }, [address, signMessageAsync])

  const handleStartQuiz = () => {
    setScreen("quiz")
  }

  const handleQuizComplete = async (answers: number[]) => {
    if (!quizToken) {
      setQuizError("Quiz session expired. Please shuffle and try again.")
      setScreen("home")
      return
    }
    try {
      const body: Record<string, unknown> = { quizToken, answers }
      if (sessionSignature && startIndex != null && address) {
        body.signature = sessionSignature
        body.address = address.toLowerCase()
        body.startIndex = startIndex
      }
      const res = await fetch("/api/verify-quiz", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(body),
      })
      if (!res.ok) {
        const text = await res.text()
        throw new Error(`Quiz API error ${res.status}: ${text.slice(0, 200)}`)
      }
      const data = (await res.json()) as { score?: number; error?: string }
      if (typeof data.score !== "number") {
        throw new Error(data.error ?? "Failed to verify quiz answers")
      }
      setFinalScore(data.score)
      setUserAnswers(answers)
      setScreen("results")
    } catch (e) {
      setQuizError(e instanceof Error ? e.message : "Failed to verify quiz answers")
      setScreen("home")
    }
  }

  const handleRestart = () => {
    setFinalScore(0)
    setUserAnswers([])
    setQuestions([])
    setQuizToken(null)
    setStartIndex(null)
    setEcosystem(null)
    setSessionSignature(null)
    setScreen("home")
    setGlobalRefreshKey((k) => k + 1)
  }

  if (!mounted) return null

  return (
    <main className="relative z-10 min-h-screen">
        {/* Verification overlay — blocks UI until wallet is signed */}
        {isConnected && !sessionSignature && address && (
          <div className="fixed inset-0 z-[70] flex items-center justify-center bg-black/80 p-4 backdrop-blur-md">
            <div className="w-full max-w-md rounded-2xl border border-white/10 bg-[#0a0a0a] p-8 text-center shadow-2xl animate-scale-in">
              <div className="mx-auto mb-6 flex size-16 items-center justify-center rounded-full border border-white/10 bg-white/5">
                <svg className="size-8 text-white/80" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={1.5} d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.623 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.285z" />
                </svg>
              </div>
              <h2 className="mb-2 text-xl font-bold text-white">Verify your account</h2>
              <p className="mb-6 text-sm text-white/60">
                To finish connecting, you must sign a message in your wallet to verify that you are the owner of this account.
              </p>
              {verifyError && (
                <p className="mb-4 text-sm text-red-400">{verifyError}</p>
              )}
              <button
                onClick={handleVerify}
                disabled={isSigning}
                className="w-full rounded-xl bg-white px-4 py-3 text-sm font-semibold text-black transition-all duration-200 hover:bg-white/90 disabled:opacity-50"
              >
                {isSigning ? "Waiting for signature..." : "Sign Message"}
              </button>
            </div>
          </div>
        )}

        {screen === "home" && (
          <HomeScreen
            onStartQuiz={handleStartQuiz}
            onShuffleQuiz={() => void fetchQuiz()}
            onRetryQuiz={() => void fetchQuiz()}
            quizLoading={quizLoading}
            quizError={quizError}
            hasQuiz={questions.length >= 5}
            nftRefreshKey={globalRefreshKey}
            cooldownRemaining={cooldownRemaining}
            isCheckingCooldown={isCheckingCooldown}
          />
        )}
        {screen === "quiz" && questions.length > 0 && (
          <QuizScreen questions={questions} onComplete={handleQuizComplete} />
        )}
        {screen === "results" && (
          <ResultsScreen
            score={finalScore}
            totalQuestions={questions.length || 5}
            quizToken={quizToken || undefined}
            userAnswers={userAnswers}
            ecosystem={ecosystem || undefined}
            startIndex={startIndex ?? undefined}
            onRestart={handleRestart}
            onScoreSubmitted={() => setGlobalRefreshKey(k => k + 1)}
          />
        )}
      </main>
    )
}

export default function HomeContent() {
  return (
    <ErrorBoundary
      fallbackRender={({ resetErrorBoundary }) => (
        <main className="min-h-screen flex items-center justify-center px-4">
          <div className="w-full max-w-md rounded-2xl border border-border bg-card/50 p-6 text-center">
            <h2 className="text-xl font-semibold text-foreground">Something went wrong</h2>
            <p className="mt-2 text-sm text-muted-foreground">
              An unexpected error occurred while loading the quiz.
            </p>
            <button
              type="button"
              onClick={resetErrorBoundary}
              className="mt-4 inline-flex h-10 items-center rounded-md bg-primary px-4 text-sm font-medium text-primary-foreground hover:bg-primary/90"
            >
              Try again
            </button>
          </div>
        </main>
      )}
    >
      <QuizApp />
    </ErrorBoundary>
  )
}
