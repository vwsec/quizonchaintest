import { NextResponse } from "next/server"
import { getRedis } from "@/lib/redis"

const ADMIN_PASSWORD = "123456789"

const ECOSYSTEMS = ["litvm", "base", "ink", "unichain", "soneium", "megaeth", "arc"]

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url)
  const password = searchParams.get("password")

  if (password !== ADMIN_PASSWORD) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const r = getRedis()
  if (!r) {
    return NextResponse.json({
      configured: false,
      message: "Upstash Redis is not configured. Add KV_URL and KV_REST_API_TOKEN env vars.",
      ecosystems: {},
    })
  }

  try {
    // Fetch all progress and submitted keys
    const [progressKeys, submittedKeys] = await Promise.all([
      r.keys("progress:*"),
      r.keys("submitted:*"),
    ])

    // Group progress keys by ecosystem
    // Key format: progress:{ecosystem}:{address}
    const progressByEco: Record<string, string[]> = {}
    for (const key of progressKeys) {
      const parts = key.split(":")
      if (parts.length >= 3) {
        const eco = parts[1].toLowerCase()
        if (!progressByEco[eco]) progressByEco[eco] = []
        progressByEco[eco].push(key)
      }
    }

    // Group submitted keys by ecosystem
    // Key format: submitted:{ecosystem}:{address}:{startIndex}
    const submittedByEco: Record<string, number> = {}
    for (const key of submittedKeys) {
      const parts = key.split(":")
      if (parts.length >= 4) {
        const eco = parts[1].toLowerCase()
        submittedByEco[eco] = (submittedByEco[eco] || 0) + 1
      }
    }

    // Build per-ecosystem stats
    const ecosystems: Record<
      string,
      { wallets: number; submittedSessions: number }
    > = {}

    for (const eco of ECOSYSTEMS) {
      ecosystems[eco] = {
        wallets: progressByEco[eco]?.length ?? 0,
        submittedSessions: submittedByEco[eco] ?? 0,
      }
    }

    // Total across all ecosystems
    const totalWallets = progressKeys.length
    const totalSubmitted = submittedKeys.length

    return NextResponse.json({
      configured: true,
      totalWallets,
      totalSubmitted,
      ecosystems,
    })
  } catch (err) {
    console.error("[redis-stats] Error:", err)
    return NextResponse.json(
      { error: "Failed to read Redis stats", detail: String(err) },
      { status: 500 },
    )
  }
}
