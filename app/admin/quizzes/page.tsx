"use client"

import { useEffect, useState } from "react"

const ADMIN_PASSWORD = "123456789"
const POOL_FILES = ["quizzes-litvm.json", "quizzes-base.json", "quizzes-ink.json", "quizzes-unichain.json", "quizzes-soneium.json", "quizzes-megaeth.json", "quizzes-arc.json"]

type PoolData = {
  meta: { ecosystem: string; totalQuizzes: number }
  quizzes: { id: number; question: string; options: string[]; correctIndex: number }[]
}

export default function AdminQuizzesPage() {
  const [authed, setAuthed] = useState(false)
  const [pools, setPools] = useState<Record<string, PoolData | null>>({})
  const [selected, setSelected] = useState<string | null>(null)
  const [qIdx, setQIdx] = useState(0)

  useEffect(() => {
    const pw = new URLSearchParams(window.location.search).get("password")
    if (pw === ADMIN_PASSWORD) setAuthed(true)
  }, [])

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

  if (!authed) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-black text-white">
        <p className="text-red-400">Invalid password. Add <code>?password=123456789</code> to the URL.</p>
      </div>
    )
  }

  const poolKeys = Object.keys(pools)
  const currentPool = selected ? pools[selected] : null
  const currentQuestion = currentPool?.quizzes[qIdx]

  return (
    <div className="min-h-screen bg-black text-white p-6">
      <h1 className="text-2xl font-bold mb-4">Quiz Pool Admin</h1>
      <div className="flex gap-2 flex-wrap mb-6">
        {poolKeys.map((key) => (
          <button
            key={key}
            onClick={() => { setSelected(key); setQIdx(0) }}
            className={`px-3 py-1 rounded text-sm ${selected === key ? "bg-blue-600" : "bg-gray-800 hover:bg-gray-700"}`}
          >
            {key} ({pools[key]?.meta.totalQuizzes ?? "—"})
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
    </div>
  )
}
