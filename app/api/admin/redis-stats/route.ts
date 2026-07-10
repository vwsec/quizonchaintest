import { NextResponse } from "next/server"

const ADMIN_PASSWORD = "123456789"

export async function GET(request: Request) {
  try {
    const { searchParams } = new URL(request.url)
    const password = searchParams.get("password")

    if (password !== ADMIN_PASSWORD) {
      return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
    }

    // Try to import Redis dynamically (catches module-level errors)
    let r: import("@upstash/redis").Redis | null = null
    try {
      const { getRedis } = await import("@/lib/redis")
      r = getRedis()
    } catch (importErr) {
      return NextResponse.json({
        configured: false,
        message: "Redis module error: " + String(importErr),
        totalWallets: 0,
        totalSubmitted: 0,
        ecosystems: {},
      })
    }

    if (!r) {
      return NextResponse.json({
        configured: false,
        message: "KV_URL / KV_REST_API_TOKEN not set.",
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

    const byEco = (keys: string[], idx: number): Record<string, number> => {
      const out: Record<string, number> = {}
      for (const key of keys) {
        const parts = key.split(":")
        if (parts.length > idx) {
          const eco = parts[1].toLowerCase()
          out[eco] = (out[eco] || 0) + 1
        }
      }
      return out
    }

    const progressByEco = byEco(progressArr, 2)
    const submittedByEco = byEco(submittedArr, 3)

    const ecosystems: Record<string, { wallets: number; submittedSessions: number }> = {}
    for (const eco of ["litvm", "base", "ink", "unichain", "soneium", "megaeth", "arc"]) {
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
