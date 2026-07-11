"use client"

import { useState, useEffect, useCallback } from "react"
import { useSignMessage, useAccount, useDisconnect, useChainId } from "wagmi"
import { SiweMessage } from "siwe"
import {
  Dialog,
  DialogContent,
  DialogOverlay,
} from "@/components/ui/dialog"
import { cn } from "@/lib/utils"
import { useChainUI } from "@/hooks/use-chain-ui"

const STORAGE_PREFIX = "siwe_verified"

function getVerifiedKey(address: string): string {
  return `${STORAGE_PREFIX}:${address.toLowerCase()}`
}

export function getStoredSIWEVerification(address: string): boolean {
  try {
    const key = getVerifiedKey(address)
    const raw = localStorage.getItem(key)
    if (!raw) return false
    const data = JSON.parse(raw)
    return data.address === address.toLowerCase() && !!data.signature
  } catch {
    return false
  }
}

export function clearStoredSIWEVerification(address: string) {
  try {
    localStorage.removeItem(getVerifiedKey(address))
  } catch {
    // ignore
  }
}

export function getStoredSIWESignature(address: string): string | null {
  try {
    const key = getVerifiedKey(address)
    const raw = localStorage.getItem(key)
    if (!raw) return null
    const data = JSON.parse(raw)
    return data.signature ?? null
  } catch {
    return null
  }
}

// Get SIWE domain from env (falls back to current host for local dev)
function getSIWEDomain(): string {
  if (typeof window === "undefined") return "localhost"
  return process.env.NEXT_PUBLIC_SIWE_DOMAIN ?? window.location.host
}

function getSIWEUri(): string {
  if (typeof window === "undefined") return "http://localhost:3000"
  return process.env.NEXT_PUBLIC_SIWE_URI ?? window.location.origin
}

interface SIWEVerificationModalProps {
  isOpen: boolean
  onVerified: () => void
  onCancel: () => void
}

export function SIWEVerificationModal({
  isOpen,
  onVerified,
  onCancel,
}: SIWEVerificationModalProps) {
  const { address } = useAccount()
  const chainId = useChainId()
  const { signMessageAsync } = useSignMessage()
  const { disconnect } = useDisconnect()
  const ui = useChainUI()

  const [isSigning, setIsSigning] = useState(false)
  const [error, setError] = useState<string | null>(null)
  const [mounted, setMounted] = useState(false)

  useEffect(() => setMounted(true), [])

  // Generate SIWE message
  const generateSIWEMessage = useCallback((): string => {
    if (!address) throw new Error("No address")
    
    const domain = getSIWEDomain()
    const uri = getSIWEUri()
    const nonce = crypto.randomUUID().replace(/-/g, "").slice(0, 32)
    const issuedAt = new Date().toISOString()

    const message = new SiweMessage({
      domain,
      address,
      statement: "Sign in to Quiz On Chain with Ethereum.",
      uri,
      version: "1",
      chainId,
      nonce,
      issuedAt,
    })

    return message.prepareMessage()
  }, [address, chainId])

  const handleSign = async () => {
    if (!address) return
    setIsSigning(true)
    setError(null)
    try {
      const message = generateSIWEMessage()
      const signature = await signMessageAsync({ message })
      
      // Store verification
      const key = getVerifiedKey(address)
      localStorage.setItem(key, JSON.stringify({
        address: address.toLowerCase(),
        signature,
        message,
        timestamp: Date.now(),
      }))
      
      onVerified()
    } catch (err: unknown) {
      const isRejected = err instanceof Error && (
        err.message.includes("rejected") ||
        err.message.includes("denied") ||
        err.message.includes("User rejected")
      )
      
      if (isRejected) {
        // User rejected - disconnect wallet
        await disconnect()
        onCancel()
      } else {
        setError("Signature was rejected. You must sign to verify your wallet ownership.")
      }
    } finally {
      setIsSigning(false)
    }
  }

  const handleCancel = async () => {
    if (!isSigning) {
      await disconnect()
      onCancel()
    }
  }

  if (!mounted) return null

  const radiusClass = ui.radius === 'rounded-none' ? 'rounded-none' : 'rounded-2xl'

  return (
    <Dialog open={isOpen} onOpenChange={(open) => { if (!open && !isSigning) handleCancel() }}>
      <DialogOverlay className="bg-black/60 backdrop-blur-sm" />
      <DialogContent
        showCloseButton={false}
        className={cn(
          "sm:max-w-md border-0 p-0 shadow-2xl",
          radiusClass,
          ui.isLight
            ? "bg-white/95 backdrop-blur-xl"
            : "bg-black/80 backdrop-blur-xl",
        )}
      >
        <div className={cn("flex flex-col items-center text-center p-8 gap-5", radiusClass)}>
          {/* Shield/verification icon */}
          <div className={cn(
            "flex items-center justify-center w-14 h-14 rounded-full",
            ui.isLight ? "bg-black/5" : "bg-white/5",
          )}>
            <svg
              width="28"
              height="28"
              viewBox="0 0 24 24"
              fill="none"
              stroke="currentColor"
              strokeWidth="1.5"
              strokeLinecap="round"
              strokeLinejoin="round"
              className={ui.accentClass}
            >
              <path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" />
              <path d="M9 12l2 2 4-4" />
            </svg>
          </div>

          <h2 className={cn("text-xl font-bold", ui.isLight ? "text-black" : "text-white")}>
            Verify your account
          </h2>

          <p className={cn("text-sm leading-relaxed max-w-xs", ui.bodyMuted)}>
            To finish connecting, you must sign a message in your wallet to verify that you are the owner of this account.
          </p>

          {error && (
            <div className={cn(
              "flex items-start gap-2 px-4 py-3 text-sm w-full",
              ui.error,
            )}>
              <svg className="size-4 shrink-0 mt-0.5" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
                <circle cx="12" cy="12" r="10" />
                <line x1="12" y1="8" x2="12" y2="12" />
                <line x1="12" y1="16" x2="12.01" y2="16" />
              </svg>
              <span>{error}</span>
            </div>
          )}

          <div className="flex flex-col gap-3 w-full">
            <button
              type="button"
              onClick={handleSign}
              disabled={isSigning}
              className={cn(
                "h-12 w-full flex items-center justify-center gap-2 font-semibold transition-all duration-200 cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed",
                ui.btnPrimary,
              )}
            >
              {isSigning ? (
                <>
                  <svg className="animate-spin size-4" viewBox="0 0 24 24" fill="none">
                    <circle className="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" strokeWidth="4" />
                    <path className="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4z" />
                  </svg>
                  Waiting for signature...
                </>
              ) : (
                <>
                  <svg className="size-4" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                    <path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4" />
                    <polyline points="7 10 12 15 17 10" />
                    <line x1="12" y1="15" x2="12" y2="3" />
                  </svg>
                  Sign Message
                </>
              )}
            </button>

            <button
              type="button"
              onClick={handleCancel}
              disabled={isSigning}
              className={cn("h-12 w-full transition-colors duration-200 cursor-pointer disabled:opacity-50", ui.btnSecondary)}
            >
              Cancel
            </button>
          </div>
        </div>
      </DialogContent>
    </Dialog>
  )
}