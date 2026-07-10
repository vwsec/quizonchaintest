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
        message:
          "Upstash Redis is not configured on Vercel. Add KV_URL and KV_REST_API_TOKEN env vars.",
        ecosystems: {},
        totalWallets: 0,
        totalSubmitted: 0,
      })
    }

    // Ping Redis first to verify connection is alive
    const ping = await r.ping()
    if (ping !== "PONG") {
      return NextResponse.json(
        { error: "Redis ping failed", detail: String(ping) },
        { status: 500 },
      )
    }

    // Fetch all progress and submitted keys
    const [progressKeys, submittedKeys] = await Promise.all([
      r.keys("progress:*"),
      r.keys("submitted:*"),
    ])

    const progressKeysList = Array.isArray(progressKeys) ? progressKeys : []
    const submittedKeysList = Array.isArray(submittedKeys) ? submittedKeys : []

    // Group by ecosystem
    const progressByEco: Record<string, number> = {}
    for (const key of progressKeysList) {
      const parts = key.split(":")
      if (parts.length >= 3) {
        const eco = parts[1].toLowerCase()
        progressByEco[eco] = (progressByEco[eco] || 0) + 1
      }
    }

    const submittedByEco: Record<string, number> = {}
    for (const key of submittedKeysList) {
      const parts = key.split(":")
      if (parts.length >= 4) {
        const eco = parts[1].toLowerCase()
        submittedByEco[eco] = (submittedByEco[eco] || 0) + 1
      }
    }

    // Build per-ecosystem stats
    const ecosystems: Record<string, { wallets: number; submittedSessions: number }> = {}
    for (const eco of ECOSYSTEMS) {
      ecosystems[eco] = {
        wallets: progressByEco[eco] ?? 0,
        submittedSessions: submittedByEco[eco] ?? 0,
      }
    }

    return NextResponse.json({
      configured: true,
      totalWallets: progressKeysList.length,
      totalSubmitted: submittedKeysList.length,
      ecosystems,
    })
  } catch (err) {
    const msg = err instanceof Error ? `${err.name}: ${err.message}` : String(err)
    console.error("[redis-stats] Error:", msg)
    return NextResponse.json(
      { error: "Failed to read Redis stats", detail: msg },
      { status: 500 },
    )
  }
}
