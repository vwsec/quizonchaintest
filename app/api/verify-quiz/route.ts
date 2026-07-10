export const dynamic = "force-dynamic"
import { jwtVerify } from "jose"
import { NextResponse } from "next/server"
import { z } from "zod"
import { verifyMessage } from "viem"
import type { Address, Hex } from "viem"
import { getEcosystem } from "@/lib/quiz-data"
import {
  isSubmitted,
  markSubmitted,
  incrementWalletProgress,
} from "@/lib/redis"

const verifySchema = z.object({
  quizToken: z.string().min(1),
  answers: z.array(z.number().int().min(0).max(3)).length(5),
  signature: z.string().optional(),
  address: z.string().optional(),
  startIndex: z.number().int().min(0).optional(),
})

const verifySecret = process.env.QUIZ_JWT_SECRET

type QuizTokenPayload = {
  answers: number[]
  chainId: number | null
  address: string | null
  startIndex: number | null
  type: "quiz-answers"
}

export async function POST(request: Request) {
  if (!verifySecret) {
    return NextResponse.json(
      { error: "Server configuration error: QUIZ_JWT_SECRET is not set" },
      { status: 500 },
    )
  }

  let body: unknown
  try {
    body = await request.json()
  } catch {
    return NextResponse.json({ error: "Malformed JSON body" }, { status: 400 })
  }

  const parsed = verifySchema.safeParse(body)
  if (!parsed.success) {
    return NextResponse.json({ error: "Invalid request body" }, { status: 400 })
  }

  try {
    const secret = new TextEncoder().encode(verifySecret)
    const { payload } = await jwtVerify(parsed.data.quizToken, secret)
    const quizPayload = payload as unknown as QuizTokenPayload

    if (
      quizPayload.type !== "quiz-answers" ||
      !Array.isArray(quizPayload.answers) ||
      quizPayload.answers.length !== 5
    ) {
      return NextResponse.json({ error: "Invalid quiz token" }, { status: 400 })
    }

    // ── Wallet signature verification (when provided) ──
    const hasSignatureProof =
      parsed.data.signature && parsed.data.address && parsed.data.startIndex != null

    if (hasSignatureProof) {
      const sig = parsed.data.signature as string
      const claimAddr = parsed.data.address as string
      const sIdx = parsed.data.startIndex as number

      // Verify the JWT was issued for this address
      if (quizPayload.address && quizPayload.address.toLowerCase() !== claimAddr.toLowerCase()) {
        return NextResponse.json(
          { error: "Address mismatch between signature and quiz token" },
          { status: 403 },
        )
      }

      // Derive ecosystem from chainId in JWT
      const ecosystem = getEcosystem(quizPayload.chainId)
      if (!ecosystem) {
        return NextResponse.json(
          { error: "Invalid chain in quiz token" },
          { status: 400 },
        )
      }

      // Verify wallet signature
      const message = `QuizonChain:${quizPayload.chainId}:${sIdx}`
      const isValid = await verifyMessage({
        address: claimAddr as Address,
        message,
        signature: sig as Hex,
      })

      if (!isValid) {
        return NextResponse.json(
          { error: "Signature verification failed — not the real wallet owner" },
          { status: 403 },
        )
      }

      // Dedup check
      const alreadySubmitted = await isSubmitted(ecosystem, claimAddr, sIdx)
      if (alreadySubmitted) {
        return NextResponse.json(
          { error: "This quiz session was already submitted" },
          { status: 409 },
        )
      }

      // Calculate score
      const score = parsed.data.answers.reduce((acc, answer, idx) => {
        return acc + (answer === quizPayload.answers[idx] ? 1 : 0)
      }, 0)

      // Mark as submitted (prevents replay)
      await markSubmitted(ecosystem, claimAddr, sIdx)

      // Advance wallet progress
      await incrementWalletProgress(ecosystem, claimAddr, 5)

      return NextResponse.json({ score })
    }

    // ── Legacy flow (no signature) ──
    const score = parsed.data.answers.reduce((acc, answer, idx) => {
      return acc + (answer === quizPayload.answers[idx] ? 1 : 0)
    }, 0)

    return NextResponse.json({ score })
  } catch {
    return NextResponse.json(
      { error: "Invalid or expired quiz token" },
      { status: 400 },
    )
  }
}
