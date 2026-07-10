"use client"

import { Suspense, useEffect, useState } from "react"
import { useSearchParams } from "next/navigation"

const ADMIN_PASSWORD = "123456789"
const POOL_FILES = ["quizzes-litvm.json", "quizzes-base.json", "quizzes-ink.json", "quizzes-unichain.json", "quizzes-soneium.json", "quizzes-megaeth.json", "quizzes-arc.json"]

type PoolData = {
  meta: { ecosystem: string; totalQuizzes: number }
  quizzes: { id: number; question: string; options: string[]; correctIndex: number }[]
}

type RedisStats = {
  configured: boolean
  message?: string
  totalWallets: number
  totalSubmitted: number
  ecosystems: Record<string, { wallets: number; submittedSessions: number }>
}

const ECOSYSTEM_LABELS: Record<string, string> = {
  litvm: "LitVM",
  base: "Base",
  ink: "Ink",
  unichain: "Unichain",
  soneium: "Soneium",
  megaeth: "MegaETH",
  arc: "Arc",
}

type Tab = "pool" | "redis"

function PoolTab({
  pools,
  selected,
  setSelected,
  qIdx,
  setQIdx,
}: {
  pools: Record<string, PoolData | null>
  selected: string | null
  setSelected: (k: string | null) => void
  qIdx: number
  setQIdx: (n: number) => void
}) {
  const poolKeys = Object.keys(pools)
  const currentPool = selected ? pools[selected] : null
  const currentQuestion = currentPool?.quizzes[qIdx]

  if (poolKeys.length === 0) {
    return <p className="text-gray-400">Loading pool data...</p>
  }

  return (
    <>
      <div className="flex gap-2 flex-wrap mb-6">
        {poolKeys.map((key) => (
          <button
            key={key}
            onClick={() => { setSelected(key); setQIdx(0) }}
            className={`px-3 py-1 rounded text-sm ${selected === key ? "bg-blue-600" : "bg-gray-800 hover:bg-gray-700"}`}
          >
            {ECOSYSTEM_LABELS[key] ?? key} ({pools[key]?.meta.totalQuizzes ?? "—"})
          </button>
        ))}
      </div>

      {currentPool && (
        <div>
          <h2 className="text-xl mb-2">
            {currentPool.meta.ecosystem} — {currentPool.quizzes.length} questions
          </h2>
          <div className="flex gap-4 items-center mb-4">
            <button onClick={() => setQIdx(Math.max(0, qIdx - 1))} className="px-3 py-1 bg-gray-800 rounded" disabled={qIdx === 0}>
              ◀ Prev
            </button>
            <span>Question {qIdx + 1} of {currentPool.quizzes.length}</span>
            <button onClick={() => setQIdx(Math.min(currentPool.quizzes.length - 1, qIdx + 1))} className="px-3 py-1 bg-gray-800 rounded" disabled={qIdx >= currentPool.quizzes.length - 1}>
              Next ▶
            </button>
            <input
              type="number"
              min={1}
              max={currentPool.quizzes.length}
              value={qIdx + 1}
              onChange={(e) => setQIdx(Math.max(0, Math.min(currentPool.quizzes.length - 1, Number(e.target.value) - 1)))}
              className="w-20 px-2 py-1 bg-gray-900 border border-gray-700 rounded text-white"
            />
          </div>
          {currentQuestion && (
            <div className="bg-gray-900 border border-gray-800 rounded p-4 max-w-2xl">
              <p className="text-lg font-medium mb-3">{currentQuestion.question}</p>
              <div className="space-y-2">
                {currentQuestion.options.map((opt, i) => (
                  <div
                    key={i}
                    className={`px-3 py-2 rounded ${i === currentQuestion.correctIndex ? "bg-green-900/50 border border-green-700" : "bg-gray-800"}`}
                  >
                    <span className="text-gray-400 mr-2">{String.fromCharCode(65 + i)}.</span>
                    {opt}
                    {i === currentQuestion.correctIndex && <span className="ml-2 text-green-400 text-sm">✓ correct</span>}
                  </div>
                ))}
              </div>
            </div>
          )}
          <div className="mt-4 text-xs text-gray-500">
            {JSON.stringify(currentPool.meta)}
          </div>
        </div>
      )}
    </>
  )
}

function RedisTab({ stats }: { stats: RedisStats | null }) {
  if (!stats) {
    return <p className="text-gray-400">Loading Redis stats...</p>
  }

  if (!stats.configured) {
    return (
      <div className="bg-yellow-900/30 border border-yellow-700 rounded p-4 max-w-xl">
        <p className="text-yellow-400 font-medium">Redis not configured</p>
        <p className="text-sm text-gray-300 mt-1">{stats.message}</p>
      </div>
    )
  }

  const ecoEntries = Object.entries(stats.ecosystems).filter(([_, v]) => v.wallets > 0 || v.submittedSessions > 0)

  return (
    <div className="max-w-2xl space-y-6">
      {/* Summary cards */}
      <div className="flex gap-4">
        <div className="bg-gray-900 border border-gray-800 rounded p-4 flex-1">
          <p className="text-sm text-gray-400">Total Wallets</p>
          <p className="text-3xl font-bold text-white">{stats.totalWallets}</p>
        </div>
        <div className="bg-gray-900 border border-gray-800 rounded p-4 flex-1">
          <p className="text-sm text-gray-400">Total Submitted Sessions</p>
          <p className="text-3xl font-bold text-white">{stats.totalSubmitted}</p>
        </div>
      </div>

      {/* Per-ecosystem table */}
      {ecoEntries.length > 0 ? (
        <div>
          <h3 className="text-lg font-medium mb-3">Per Ecosystem</h3>
          <table className="w-full text-sm">
            <thead>
              <tr className="border-b border-gray-800 text-gray-400">
                <th className="text-left py-2 pr-4">Ecosystem</th>
                <th className="text-right py-2 pr-4">Wallets</th>
                <th className="text-right py-2">Submitted Sessions</th>
              </tr>
            </thead>
            <tbody>
              {ecoEntries.map(([key, val]) => (
                <tr key={key} className="border-b border-gray-800/50">
                  <td className="py-2 pr-4 text-white font-medium">{ECOSYSTEM_LABELS[key] ?? key}</td>
                  <td className="text-right py-2 pr-4 text-gray-300">{val.wallets}</td>
                  <td className="text-right py-2 text-gray-300">{val.submittedSessions}</td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      ) : (
        <p className="text-gray-500">No wallet activity yet.</p>
      )}
    </div>
  )
}

function AdminContent() {
  const searchParams = useSearchParams()
  const [authed, setAuthed] = useState(false)
  const [tab, setTab] = useState<Tab>("pool")
  const [pools, setPools] = useState<Record<string, PoolData | null>>({})
  const [redisStats, setRedisStats] = useState<RedisStats | null>(null)
  const [selected, setSelected] = useState<string | null>(null)
  const [qIdx, setQIdx] = useState(0)

  useEffect(() => {
    const pw = searchParams.get("password")
    setAuthed(pw === ADMIN_PASSWORD)
  }, [searchParams])

  // Load pool data
  useEffect(() => {
    if (!authed) return
    Promise.all(
      POOL_FILES.map(async (file) => {
        const key = file.replace("quizzes-", "").replace(".json", "")
        try {
          const res = await fetch(`/api/admin/quiz-pool?file=${file}&password=${ADMIN_PASSWORD}`)
          if (!res.ok) return [key, null] as const
          const data: PoolData = await res.json()
          return [key, data] as const
        } catch {
          return [key, null] as const
        }
      }),
    ).then((entries) => setPools(Object.fromEntries(entries)))
  }, [authed])

  // Load Redis stats
  useEffect(() => {
    if (!authed) return
    fetch(`/api/admin/redis-stats?password=${ADMIN_PASSWORD}`)
      .then((r) => r.json())
      .then((data) => setRedisStats(data))
      .catch(() => setRedisStats({ configured: false, totalWallets: 0, totalSubmitted: 0, ecosystems: {}, message: "Failed to fetch" }))
  }, [authed])

  if (!authed) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-black text-white">
        <p className="text-red-400">Invalid password. Add <code>?password=123456789</code> to the URL.</p>
      </div>
    )
  }

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <h1 className="text-2xl font-bold mb-4">QuizOnChain Admin</h1>

      {/* Tabs */}
      <div className="flex gap-1 mb-6 border-b border-gray-800">
        <button
          onClick={() => setTab("pool")}
          className={`px-4 py-2 text-sm rounded-t ${tab === "pool" ? "bg-gray-900 border border-b-0 border-gray-800 text-white" : "text-gray-400 hover:text-white"}`}
        >
          Question Pool
        </button>
        <button
          onClick={() => setTab("redis")}
          className={`px-4 py-2 text-sm rounded-t ${tab === "redis" ? "bg-gray-900 border border-b-0 border-gray-800 text-white" : "text-gray-400 hover:text-white"}`}
        >
          Redis Stats
        </button>
      </div>

      {/* Tab content */}
      {tab === "pool" && (
        <PoolTab
          pools={pools}
          selected={selected}
          setSelected={setSelected}
          qIdx={qIdx}
          setQIdx={setQIdx}
        />
      )}
      {tab === "redis" && <RedisTab stats={redisStats} />}
    </div>
  )
}

export default function AdminQuizzesPage() {
  return (
    <Suspense fallback={<div className="min-h-screen bg-black text-white flex items-center justify-center">Loading...</div>}>
      <AdminContent />
    </Suspense>
  )
}
