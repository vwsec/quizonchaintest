import { NextResponse } from "next/server"
import { createSession, makeSessionCookie, getSession } from "@/lib/admin-session"

const ADMIN_PASSWORD = process.env.ADMIN_PASSWORD
if (!ADMIN_PASSWORD) {
  console.warn("[admin] ADMIN_PASSWORD env var not set — using default. Set it on Vercel for security.")
}

export async function POST(request: Request) {
  if (!ADMIN_PASSWORD) {
    return NextResponse.json(
      { error: "ADMIN_PASSWORD env var not set on server" },
      { status: 500 },
    )
  }

  let body: { password?: string }
  try {
    body = await request.json()
  } catch {
    return NextResponse.json({ error: "Invalid JSON" }, { status: 400 })
  }

  if (body.password !== ADMIN_PASSWORD) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const token = await createSession()
  return NextResponse.json({ ok: true }, { headers: { "Set-Cookie": makeSessionCookie(token) } })
}

export async function GET(request: Request) {
  const authed = await getSession(request)
  return NextResponse.json({ authed })
}
