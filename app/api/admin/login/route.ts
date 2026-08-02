import { NextResponse } from "next/server"
import { createSession, makeSessionCookie, getSession } from "@/lib/admin-session"

export async function POST(request: Request) {
  const adminPassword = process.env.ADMIN_PASSWORD
  if (!adminPassword) {
    return NextResponse.json({ error: "ADMIN_PASSWORD is not set. Configure it in your environment variables." }, { status: 500 })
  }

  let body: { password?: string }
  try {
    body = await request.json()
  } catch {
    return NextResponse.json({ error: "Invalid JSON" }, { status: 400 })
  }

  if (body.password !== adminPassword) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  const token = await createSession()
  return NextResponse.json({ ok: true }, { headers: { "Set-Cookie": makeSessionCookie(token) } })
}

export async function GET(request: Request) {
  const authed = await getSession(request)
  return NextResponse.json({ authed })
}
