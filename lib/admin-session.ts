import { SignJWT, jwtVerify } from "jose"

const SESSION_SECRET = new TextEncoder().encode(
  process.env.QUIZ_JWT_SECRET || process.env.ADMIN_PASSWORD || "dev-fallback-only",
)
const COOKIE_NAME = "admin_session"
const COOKIE_MAX_AGE = 60 * 60 * 24 // 24 hours

export async function createSession(): Promise<string> {
  return await new SignJWT({ role: "admin", t: "admin-session" })
    .setProtectedHeader({ alg: "HS256" })
    .setIssuedAt()
    .setExpirationTime(`${COOKIE_MAX_AGE}s`)
    .sign(SESSION_SECRET)
}

export function makeSessionCookie(token: string): string {
  return [
    `${COOKIE_NAME}=${token}`,
    "HttpOnly",
    "Secure",
    "SameSite=Strict",
    `Max-Age=${COOKIE_MAX_AGE}`,
    "Path=/admin",
  ].join("; ")
}

export async function getSession(request: Request): Promise<boolean> {
  const cookie = request.headers.get("cookie") || ""
  const match = cookie.match(new RegExp(`(?:^|;\\s*)${COOKIE_NAME}=([^;]*)`))
  if (!match) return false
  try {
    const { payload } = await jwtVerify(match[1], SESSION_SECRET)
    return payload.role === "admin" && payload.t === "admin-session"
  } catch {
    return false
  }
}
