import { NextResponse } from "next/server"
import { getRedis } from "@/lib/redis"
import fs from "fs"
import path from "path"

const ADMIN_PASSWORD = "123456789"

const ECOSYSTEMS = [
  { key: "litvm", name: "LitVM" },
  { key: "base", name: "Base" },
  { key: "ink", name: "Ink" },
  { key: "unichain", name: "Unichain" },
  { key: "soneium", name: "Soneium" },
  { key: "megaeth", name: "MegaETH" },
  { key: "arc", name: "Arc Testnet" },
]

/** Load pool metadata for an ecosystem — returns total quiz count or 0 if no pool file */
function getPoolSize(ecosystemKey: string): { totalQuizzes: number; questionsPerSession: number } {
  try {
    const filePath = path.join(process.cwd(), "data", `quizzes-${ecosystemKey}.json`)
    if (!fs.existsSync(filePath)) return { totalQuizzes: 0, questionsPerSession: 5 }
    const raw = fs.readFileSync(filePath, "utf-8")
    const pool = JSON.parse(raw)
    return {
      totalQuizzes: pool.meta?.totalQuizzes ?? pool.quizzes?.length ?? 0,
      questionsPerSession: pool.meta?.questionsPerSession ?? 5,
    }
  } catch {
    return { totalQuizzes: 0, questionsPerSession: 5 }
  }
}

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url)
    const password = searchParams.get("password")

    if (password !== ADMIN_PASSWORD) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    const r = getRedis()
    if (!r) {
      return NextResponse.json({
        configured: false,
        message: "KV_REST_API_URL / KV_REST_API_TOKEN not set.",
        wallets: [],
        ecosystems: {},
      })
    }

    // Get all progress keys
    const progressKeys = await r.keys("progress:*")
    const progressArr = Array.isArray(progressKeys) ? progressKeys : []

    // Get all submitted keys
    const submittedKeys = await r.keys("submitted:*")
    const submittedArr = Array.isArray(submittedKeys) ? submittedKeys : []

    // Get individual wallet values in batch where possible
    // For each progress key, fetch the value (questions done)
    const wallets: {
      ecosystem: string
      ecosystemKey: string
      address: string
      questionsDone: number
      quizzesDone: number
      totalQuizzes: number
      questionsPerSession: number
      progressPct: number
      nearCompletion: boolean
    }[] = []

    for (const key of progressArr) {
      const parts = key.split(":")
      if (parts.length < 3) continue
      const ecoKey = parts[1].toLowerCase()
      const address = parts.slice(2).join(":") // handle edge case where address contains colons

      const val = await r.get<number>(key)
      const questionsDone = val ?? 0
      const quizzesDone = Math.floor(questionsDone / 5)

      const poolInfo = getPoolSize(ecoKey)
      const totalQ = poolInfo.totalQuizzes

      // Progress percentage: if pool exists, % of total; if no pool, mark as unlimited
      const progressPct = totalQ > 0 ? Math.round((questionsDone / totalQ) * 100 * 10) / 10 : -1
      const nearCompletion = totalQ > 0 && progressPct >= 80

      wallets.push({
        ecosystem: ECOSYSTEMS.find((e) => e.key === ecoKey)?.name ?? ecoKey,
        ecosystemKey: ecoKey,
        address,
        questionsDone,
        quizzesDone,
        totalQuizzes: totalQ,
        questionsPerSession: poolInfo.questionsPerSession,
        progressPct,
        nearCompletion,
      })
    }

    // Sort: near-completion wallets first, then by progress descending
    wallets.sort((a, b) => {
      if (a.nearCompletion !== b.nearCompletion) return a.nearCompletion ? -1 : 1
      return b.progressPct - a.progressPct
    })

    // Per-ecosystem aggregate
    const ecosystems: Record<
      string,
      { wallets: number; submittedSessions: number; totalPool: number; nearCompletion: number }
    > = {}
    for (const eco of ECOSYSTEMS) {
      const ecoWallets = wallets.filter((w) => w.ecosystemKey === eco.key)
      const poolInfo = getPoolSize(eco.key)
      ecosystems[eco.key] = {
        wallets: ecoWallets.length,
        submittedSessions: submittedArr.filter((k) => k.startsWith(`submitted:${eco.key}:`)).length,
        totalPool: poolInfo.totalQuizzes,
        nearCompletion: ecoWallets.filter((w) => w.nearCompletion).length,
      }
    }

    return NextResponse.json({
      configured: true,
      totalWallets: wallets.length,
      totalSubmitted: submittedArr.length,
      wallets,
      ecosystems,
    })
  } catch (err) {
    const msg = err instanceof Error ? `${err.name}: ${err.message}` : String(err)
    console.error("[redis-stats] Error:", msg)
    return NextResponse.json({ error: msg }, { status: 500 })
  }
}
