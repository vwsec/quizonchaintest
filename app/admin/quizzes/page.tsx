"use client"

import { Suspense, useEffect, useState } from "react"
import { useSearchParams } from "next/navigation"

const ADMIN_PASSWORD = "123456789"
const POOL_FILES = ["quizzes-litvm.json", "quizzes-base.json", "quizzes-ink.json", "quizzes-unichain.json", "quizzes-soneium.json", "quizzes-megaeth.json", "quizzes-arc.json"]

type RedisWallet = {
  ecosystem: string
  ecosystemKey: string
  address: string
  questionsDone: number
  quizzesDone: number
  totalQuizzes: number
  questionsPerSession: number
  progressPct: number
  nearCompletion: boolean
}

type RedisStats = {
  configured: boolean
  totalWallets: number
  totalSubmitted: number
  wallets: RedisWallet[]
  ecosystems: Record<string, { wallets: number; submittedSessions: number; totalPool: number; nearCompletion: number }>
  message?: string
  error?: string
}

type PoolMeta = { totalQuizzes: number; ecosystem: string; batchId: string; questionsPerSession: number }
type PoolQuizInfo = { id: number; question: string; options: string[]; correctIndex: number }

function Home() {
  const searchParams = useSearchParams()
  const password = searchParams.get("password")
  const authed = password === ADMIN_PASSWORD

  const [tab, setTab] = useState<"pool" | "stats">("pool")
  const [selectedFile, setSelectedFile] = useState(POOL_FILES[0])
  const [poolMeta, setPoolMeta] = useState<PoolMeta | null>(null)
  const [questions, setQuestions] = useState<PoolQuizInfo[]>([])
  const [searchTerm, setSearchTerm] = useState("")
  const [currentPage, setCurrentPage] = useState(0)
  const [redisStats, setRedisStats] = useState<RedisStats | null>(null)
  const [loadingStats, setLoadingStats] = useState(false)
  const itemsPerPage = 10

  // Load pool data
  useEffect(() => {
    if (!authed) return
    fetch(`/api/admin/quiz-pool?file=${selectedFile}&password=${ADMIN_PASSWORD}`)
      .then((r) => r.json())
      .then((data) => {
        setPoolMeta(data.meta ?? null)
        setQuestions(data.quizzes ?? data.questions ?? [])
        setCurrentPage(0)
      })
      .catch(() => {
        setPoolMeta(null)
        setQuestions([])
      })
  }, [authed, selectedFile])

  // Load Redis stats
  useEffect(() => {
    if (!authed || tab !== "stats") return
    setLoadingStats(true)
    fetch(`/api/admin/redis-stats?password=${ADMIN_PASSWORD}`)
      .then((r) => r.json())
      .then((data) => setRedisStats(data))
      .catch((e) =>
        setRedisStats({
          configured: false,
          totalWallets: 0,
          totalSubmitted: 0,
          wallets: [],
          ecosystems: {},
          message: "Failed to fetch: " + String(e),
        }),
      )
      .finally(() => setLoadingStats(false))
  }, [authed, tab])

  // Determine alert status
  const nearCompletionWallets = redisStats?.wallets?.filter((w) => w.nearCompletion) ?? []
  const hasNearCompletion = nearCompletionWallets.length > 0

  const filtered = questions.filter(
    (q) =>
      q.question.toLowerCase().includes(searchTerm.toLowerCase()) ||
      q.options.some((o) => o.toLowerCase().includes(searchTerm.toLowerCase())),
  )
  const pageCount = Math.ceil(filtered.length / itemsPerPage)
  const paged = filtered.slice(currentPage * itemsPerPage, (currentPage + 1) * itemsPerPage)

  // Color helpers
  const progressColor = (pct: number, near: boolean) => {
    if (near) return "bg-red-500"
    if (pct >= 70) return "bg-amber-500"
    return "bg-emerald-500"
  }

  const progressBg = (pct: number, near: boolean) => {
    if (near) return "bg-red-900/30"
    if (pct >= 70) return "bg-amber-900/30"
    return "bg-emerald-900/30"
  }

  function ProgressBar({ pct, near, totalQuizzes }: { pct: number; near: boolean; totalQuizzes: number }) {
    if (totalQuizzes === 0) return <span className="text-xs text-zinc-500 italic">Unlimited</span>
    const display = pct < 0 ? 0 : Math.min(pct, 100)
    return (
      <div className={`h-2 rounded-full ${progressBg(display, near)} overflow-hidden`}>
        <div
          className={`h-full rounded-full transition-all duration-500 ${progressColor(display, near)}`}
          style={{ width: `${display}%` }}
        />
      </div>
    )
  }

  if (!authed) {
    return (
      <div className="min-h-screen bg-zinc-950 flex items-center justify-center">
        <div className="text-zinc-400 text-sm">Unauthorized — wrong password</div>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-zinc-950 text-zinc-100">
      {/* Header */}
      <header className="border-b border-zinc-800 px-6 py-4 flex items-center justify-between">
        <div>
          <h1 className="text-lg font-semibold tracking-tight">QuizonChain Admin</h1>
          <p className="text-xs text-zinc-500 font-mono">Pool &amp; wallet tracking</p>
        </div>
        <div className="flex gap-1 bg-zinc-900 rounded-lg p-1">
          <button
            onClick={() => setTab("pool")}
            className={`px-4 py-1.5 text-sm rounded-md transition-colors ${
              tab === "pool" ? "bg-zinc-800 text-zinc-100" : "text-zinc-500 hover:text-zinc-300"
            }`}
          >
            Question Pool
          </button>
          <button
            onClick={() => setTab("stats")}
            className={`px-4 py-1.5 text-sm rounded-md transition-colors ${
              tab === "stats" ? "bg-zinc-800 text-zinc-100" : "text-zinc-500 hover:text-zinc-300"
            }`}
          >
            Redis Stats
            {hasNearCompletion && (
              <span className="ml-2 inline-flex items-center justify-center w-5 h-5 text-xs rounded-full bg-red-500 text-white">
                {nearCompletionWallets.length}
              </span>
            )}
          </button>
        </div>
      </header>

      {/* ──────────── POOL TAB ──────────── */}
      {tab === "pool" && (
        <main className="p-6 space-y-6">
          {/* Pool Selector */}
          <div className="flex items-center gap-3">
            <label className="text-sm text-zinc-500">Pool file:</label>
            <select
              value={selectedFile}
              onChange={(e) => setSelectedFile(e.target.value)}
              className="bg-zinc-900 border border-zinc-800 rounded-lg px-3 py-2 text-sm text-zinc-100"
            >
              {POOL_FILES.map((f) => (
                <option key={f} value={f}>
                  {f}
                </option>
              ))}
            </select>
            {poolMeta && (
              <span className="text-xs text-zinc-500">
                {poolMeta.totalQuizzes} quizzes &middot; {poolMeta.questionsPerSession} per session
              </span>
            )}
          </div>

          {/* Search */}
          <input
            type="text"
            placeholder="Search questions..."
            value={searchTerm}
            onChange={(e) => {
              setSearchTerm(e.target.value)
              setCurrentPage(0)
            }}
            className="w-full bg-zinc-900 border border-zinc-800 rounded-lg px-4 py-2 text-sm text-zinc-100 placeholder-zinc-600"
          />

          {/* Question List */}
          <div className="space-y-2">
            {paged.map((q) => (
              <details key={q.id} className="bg-zinc-900/50 border border-zinc-800 rounded-lg group">
                <summary className="px-4 py-3 text-sm cursor-pointer hover:bg-zinc-800/40 rounded-lg transition-colors">
                  <span className="text-zinc-500 font-mono mr-2">#{q.id}</span>
                  {q.question}
                </summary>
                <div className="px-4 pb-3 pt-1 space-y-1">
                  {q.options.map((opt, i) => (
                    <div
                      key={i}
                      className={`flex items-center gap-2 px-3 py-1.5 rounded text-sm ${
                        i === q.correctIndex ? "bg-emerald-900/30 text-emerald-300" : "text-zinc-400"
                      }`}
                    >
                      <span className="w-5 text-right font-mono text-xs text-zinc-600">{i}</span>
                      {opt}
                      {i === q.correctIndex && <span className="ml-auto text-emerald-400 text-[10px] font-mono">CORRECT</span>}
                    </div>
                  ))}
                </div>
              </details>
            ))}
          </div>

          {/* Pagination */}
          {pageCount > 1 && (
            <div className="flex items-center justify-center gap-2 text-sm">
              <button
                onClick={() => setCurrentPage(Math.max(0, currentPage - 1))}
                disabled={currentPage === 0}
                className="px-3 py-1.5 rounded-md bg-zinc-900 border border-zinc-800 disabled:opacity-30"
              >
                Prev
              </button>
              <span className="text-zinc-500">
                {currentPage + 1} / {pageCount}
              </span>
              <button
                onClick={() => setCurrentPage(Math.min(pageCount - 1, currentPage + 1))}
                disabled={currentPage >= pageCount - 1}
                className="px-3 py-1.5 rounded-md bg-zinc-900 border border-zinc-800 disabled:opacity-30"
              >
                Next
              </button>
            </div>
          )}
        </main>
      )}

      {/* ──────────── REDIS STATS TAB ──────────── */}
      {tab === "stats" && (
        <main className="p-6 space-y-6">
          {/* Alert Banner */}
          {hasNearCompletion && (
            <div className="border border-red-800 bg-red-950/40 rounded-xl px-5 py-4 flex items-start gap-3">
              <span className="text-red-400 text-lg leading-none mt-0.5">&#9650;</span>
              <div>
                <p className="font-semibold text-red-300 text-sm">
                  Pool files need attention
                </p>
                <p className="text-red-400/80 text-xs mt-1">
                  {nearCompletionWallets.length} wallet{nearCompletionWallets.length > 1 ? "s" : ""} running out of unique questions.
                  {nearCompletionWallets.map((w) => (
                    <span key={w.address} className="block font-mono mt-0.5">
                      {w.ecosystem} &mdash; {w.address.slice(0, 6)}...{w.address.slice(-4)} &mdash; {w.progressPct}% done
                    </span>
                  ))}
                  Generate a new batch of questions via Hermes Agent.
                </p>
              </div>
            </div>
          )}

          {/* Not Configured */}
          {redisStats && !redisStats.configured && !redisStats.error && (
            <div className="border border-amber-800 bg-amber-950/40 rounded-xl px-5 py-4">
              <p className="text-amber-300 font-semibold text-sm">Redis not configured</p>
              <p className="text-amber-400/70 text-xs mt-1">{redisStats.message ?? "Missing KV_REST_API_URL / KV_REST_API_TOKEN env vars."}</p>
            </div>
          )}

          {redisStats?.error && (
            <div className="border border-red-800 bg-red-950/40 rounded-xl px-5 py-4">
              <p className="text-red-300 font-semibold text-sm">API Error</p>
              <p className="text-red-400/70 text-xs mt-1 font-mono">{redisStats.error}</p>
            </div>
          )}

          {loadingStats && (
            <div className="text-center py-12">
              <div className="inline-block w-6 h-6 border-2 border-zinc-600 border-t-blue-400 rounded-full animate-spin" />
              <p className="text-zinc-500 text-sm mt-3">Loading Redis stats...</p>
            </div>
          )}

          {redisStats?.configured && !loadingStats && (
            <>
              {/* Overview Cards */}
              <div className="grid grid-cols-2 md:grid-cols-4 gap-3">
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl px-4 py-3">
                  <p className="text-2xl font-bold tracking-tight">{redisStats.totalWallets}</p>
                  <p className="text-xs text-zinc-500 mt-1">Total Wallets</p>
                </div>
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl px-4 py-3">
                  <p className="text-2xl font-bold tracking-tight">{redisStats.totalSubmitted}</p>
                  <p className="text-xs text-zinc-500 mt-1">Submitted Sessions</p>
                </div>
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl px-4 py-3">
                  <p className="text-2xl font-bold tracking-tight">
                    {redisStats.ecosystems.litvm?.nearCompletion ?? 0}
                  </p>
                  <p className="text-xs text-zinc-500 mt-1">Near Completion</p>
                </div>
                <div className="bg-zinc-900/60 border border-zinc-800 rounded-xl px-4 py-3">
                  <p className="text-2xl font-bold tracking-tight">
                    {Object.entries(redisStats.ecosystems ?? {}).filter(([, v]) => v.totalPool > 0).length}
                  </p>
                  <p className="text-xs text-zinc-500 mt-1">Pools Active</p>
                </div>
              </div>

              {/* Per-Ecosystem */}
              <div className="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-3">
                {Object.entries(redisStats.ecosystems ?? {}).map(([key, eco]) => {
                  const poolLabel = eco.totalPool > 0 ? `${eco.totalPool} quizzes` : "No pool"
                  return (
                    <div
                      key={key}
                      className={`border rounded-xl px-4 py-3 ${
                        eco.nearCompletion > 0 ? "border-red-800 bg-red-950/20" : "border-zinc-800 bg-zinc-900/40"
                      }`}
                    >
                      <p className="font-semibold text-sm capitalize">{key}</p>
                      <div className="mt-2 space-y-1 text-xs text-zinc-400">
                        <p>{eco.wallets} wallet{eco.wallets !== 1 ? "s" : ""}</p>
                        <p>{eco.submittedSessions} submitted</p>
                        <p className="font-mono text-zinc-500">{poolLabel}</p>
                        {eco.nearCompletion > 0 && (
                          <p className="text-red-400 font-semibold">
                            {eco.nearCompletion} near completion
                          </p>
                        )}
                      </div>
                    </div>
                  )
                })}
              </div>

              {/* Wallet Table */}
              {redisStats.wallets.length > 0 ? (
                <div className="overflow-x-auto">
                  <table className="w-full text-sm">
                    <thead>
                      <tr className="text-xs text-zinc-500 border-b border-zinc-800">
                        <th className="text-left py-2 pr-4 font-medium">Wallet</th>
                        <th className="text-left py-2 pr-4 font-medium">Ecosystem</th>
                        <th className="text-right py-2 pr-4 font-medium">Quizzes</th>
                        <th className="text-left py-2 pr-4 font-medium">Progress</th>
                        <th className="text-left py-2 font-medium">Status</th>
                      </tr>
                    </thead>
                    <tbody>
                      {redisStats.wallets.map((w) => {
                        const truncated = `${w.address.slice(0, 6)}...${w.address.slice(-4)}`
                        return (
                          <tr
                            key={w.address}
                            className={`border-b border-zinc-800/50 ${
                              w.nearCompletion ? "bg-red-950/15" : "hover:bg-zinc-900/30"
                            }`}
                          >
                            <td className="py-3 pr-4 font-mono text-xs text-zinc-300">{truncated}</td>
                            <td className="py-3 pr-4">
                              <span className="capitalize text-xs bg-zinc-800 px-2 py-0.5 rounded">
                                {w.ecosystem}
                              </span>
                            </td>
                            <td className="py-3 pr-4 text-right font-mono text-xs text-zinc-300">
                              {w.quizzesDone}
                              {w.totalQuizzes > 0 && (
                                <span className="text-zinc-600">
                                  {" "}/ {Math.floor(w.totalQuizzes / w.questionsPerSession)}
                                </span>
                              )}
                            </td>
                            <td className="py-3 pr-4 min-w-[120px]">
                              <div className="flex items-center gap-2">
                                <div className="flex-1">
                                  <ProgressBar pct={w.progressPct} near={w.nearCompletion} totalQuizzes={w.totalQuizzes} />
                                </div>
                                <span
                                  className={`text-xs font-mono ${
                                    w.nearCompletion ? "text-red-400" : "text-zinc-500"
                                  }`}
                                >
                                  {w.totalQuizzes > 0 ? `${w.progressPct}%` : "\u221E"}
                                </span>
                              </div>
                            </td>
                            <td className="py-3">
                              {w.totalQuizzes === 0 ? (
                                <span className="text-[10px] text-zinc-600 italic">unlimited</span>
                              ) : w.nearCompletion ? (
                                <span className="flex items-center gap-1 text-[10px] text-red-400 font-semibold">
                                  <span className="inline-block w-1.5 h-1.5 rounded-full bg-red-500" />
                                  NEED POOL
                                </span>
                              ) : (
                                <span className="flex items-center gap-1 text-[10px] text-emerald-400">
                                  <span className="inline-block w-1.5 h-1.5 rounded-full bg-emerald-500" />
                                  OK
                                </span>
                              )}
                            </td>
                          </tr>
                        )
                      })}
                    </tbody>
                  </table>
                </div>
              ) : (
                <div className="text-center py-12">
                  <p className="text-zinc-500 text-sm">No wallets tracked yet. Complete a quiz to appear here.</p>
                </div>
              )}
            </>
          )}
        </main>
      )}
    </div>
  )
}

export default function Page() {
  return (
    <Suspense>
      <Home />
    </Suspense>
  )
}
