import { NextResponse } from "next/server"
import { getRedis } from "@/lib/redis"

const ADMIN_PASSWORD = "123456789"

const ECOSYSTEMS = ["litvm", "base", "ink", "unichain", "soneium", "megaeth", "arc"]

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
        totalWallets: 0,
        totalSubmitted: 0,
        ecosystems: {},
      })
    }

    const [progressKeys, submittedKeys] = await Promise.all([
      r.keys("progress:*"),
      r.keys("submitted:*"),
    ])

    const progressArr = Array.isArray(progressKeys) ? progressKeys : []
    const submittedArr = Array.isArray(submittedKeys) ? submittedKeys : []

    const byEco = (keys: string[], minParts: number): Record<string, number> => {
      const out: Record<string, number> = {}
      for (const key of keys) {
        const parts = key.split(":")
        if (parts.length >= minParts) {
          const eco = parts[1].toLowerCase()
          out[eco] = (out[eco] || 0) + 1
        }
      }
      return out
    }

    const progressByEco = byEco(progressArr, 3)
    const submittedByEco = byEco(submittedArr, 4)

    const ecosystems: Record<string, { wallets: number; submittedSessions: number }> = {}
    for (const eco of ECOSYSTEMS) {
      ecosystems[eco] = {
        wallets: progressByEco[eco] ?? 0,
        submittedSessions: submittedByEco[eco] ?? 0,
      }
    }

    return NextResponse.json({
      configured: true,
      totalWallets: progressArr.length,
      totalSubmitted: submittedArr.length,
      ecosystems,
    })
  } catch (err) {
    const msg = err instanceof Error ? `${err.name}: ${err.message}` : String(err)
    console.error("[redis-stats] Error:", msg)
    return NextResponse.json({ error: msg }, { status: 500 })
  }
}
