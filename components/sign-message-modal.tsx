"use client"

import { useState } from "react"
import { useSignMessage, useAccount } from "wagmi"
import {
  Dialog,
  DialogContent,
  DialogHeader,
  DialogTitle,
  DialogDescription,
} from "@/components/ui/dialog"
import { Button } from "@/components/ui/button"

interface SignMessageModalProps {
  isOpen: boolean
  onClose: () => void
  onSuccess: (signature: string) => void
  walletAddress: string
}

const STORAGE_PREFIX = "quizonchain_session"

export function getStoredSignature(address: string): string | null {
  try {
    const key = `${STORAGE_PREFIX}:${address.toLowerCase()}`
    const raw = localStorage.getItem(key)
    if (!raw) return null
    const data = JSON.parse(raw)
    if (data.address === address.toLowerCase() && data.signature) {
      return data.signature
    }
    return null
  } catch {
    return null
  }
}

export function clearStoredSignature(address: string) {
  try {
    const key = `${STORAGE_PREFIX}:${address.toLowerCase()}`
    localStorage.removeItem(key)
  } catch {
    // ignore
  }
}

export function SignMessageModal({ isOpen, onClose, onSuccess, walletAddress }: SignMessageModalProps) {
  const { signMessageAsync } = useSignMessage()
  const [isSigning, setIsSigning] = useState(false)
  const [error, setError] = useState<string | null>(null)

  const handleSign = async () => {
    setIsSigning(true)
    setError(null)
    try {
      const message = `QuizonChain Session:${walletAddress}`
      const sig = await signMessageAsync({ message })
      // Persist to localStorage
      const key = `${STORAGE_PREFIX}:${walletAddress.toLowerCase()}`
      localStorage.setItem(
        key,
        JSON.stringify({
          address: walletAddress.toLowerCase(),
          signature: sig,
          timestamp: Date.now(),
        }),
      )
      onSuccess(sig)
      onClose()
    } catch {
      setError("Signature was rejected. You must sign to verify your wallet.")
    } finally {
      setIsSigning(false)
    }
  }

  return (
    <Dialog open={isOpen} onOpenChange={(open) => { if (!open) onClose() }}>
      <DialogContent className="sm:max-w-md">
        <DialogHeader>
          <DialogTitle>Verify your account</DialogTitle>
          <DialogDescription>
            To finish connecting, you must sign a message in your wallet to verify that you are the owner of this account.
          </DialogDescription>
        </DialogHeader>
        {error && (
          <p className="text-sm text-red-500">{error}</p>
        )}
        <div className="flex gap-3 justify-end">
          <Button variant="outline" onClick={onClose} disabled={isSigning}>
            Cancel
          </Button>
          <Button onClick={handleSign} disabled={isSigning}>
            {isSigning ? "Waiting for signature..." : "Sign Message"}
          </Button>
        </div>
      </DialogContent>
    </Dialog>
  )
}
