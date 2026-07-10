import { NextResponse } from "next/server"
import fs from "fs"
import path from "path"

const ADMIN_PASSWORD = "123456789"
const ALLOWED_FILES = [
  "quizzes-litvm.json",
  "quizzes-base.json",
  "quizzes-ink.json",
  "quizzes-unichain.json",
  "quizzes-soneium.json",
  "quizzes-megaeth.json",
  "quizzes-arc.json",
]

export async function GET(request: Request) {
  const { searchParams } = new URL(request.url)
  const password = searchParams.get("password")
  const file = searchParams.get("file")

  if (password !== ADMIN_PASSWORD) {
    return NextResponse.json({ error: "Unauthorized" }, { status: 401 })
  }

  if (!file || !ALLOWED_FILES.includes(file)) {
    return NextResponse.json({ error: "Invalid file" }, { status: 400 })
  }

  try {
    const filePath = path.join(process.cwd(), "data", file)
    const raw = fs.readFileSync(filePath, "utf-8")
    const data = JSON.parse(raw)
    return NextResponse.json(data)
  } catch {
    return NextResponse.json({ error: "Pool file not found" }, { status: 404 })
  }
}
