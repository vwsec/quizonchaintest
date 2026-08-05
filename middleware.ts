import { NextResponse } from 'next/server'
import type { NextRequest } from 'next/server'

const ALLOWED_ORIGINS = [
  'https://quizonchain.app',
  'https://www.quizonchain.app',
  'https://quizonchaintest.vercel.app',
  'https://quizonchain0.vercel.app',
  'https://quizonchain1.vercel.app',
  'http://localhost:3000',
  'http://localhost:3100',
  'https://app.startale.com',
]

// ponytail: common crawlers + AI-crawler wave (they send no Origin/Referer, so UA is the only cheap filter); expand if a real user reports being blocked
const BLOCKED_BOT_PATTERNS = [
  'googlebot', 'bingbot', 'slurp', 'duckduckbot', 'baiduspider',
  'yandexbot', 'facebookexternalhit', 'twitterbot', 'rogerbot',
  'linkedinbot', 'embedly', 'quora link preview', 'showyoubot',
  'outbrain', 'pinterest', 'slackbot', 'vkshare', 'w3c_validator',
  'python-requests', 'python-urllib', 'go-http-client', 'curl',
  'wget', 'scrapy', 'semrush', 'ahrefsbot', 'dotbot', 'mj12bot',
  // AI crawlers + scrapers (2024-2026 wave)
  'gptbot', 'chatgpt-user', 'claudebot', 'anthropic-ai', 'perplexitybot',
  'bytespider', 'ccbot', 'amazonbot', 'meta-externalagent',
  'meta-externalfetcher', 'applebot', 'petalbot', 'cohere-ai', 'omgili',
  'imagesiftbot', 'seekrbot', 'youbot', 'dataforseo', 'zoominfobot',
  'diffbot', 'headlesschrome', 'phantomjs',
]

function isAllowed(value: string): boolean {
  return ALLOWED_ORIGINS.some((allowed) => value.replace(/\/$/, "") === allowed)
}

export function middleware(request: NextRequest) {
  const ua = (request.headers.get('user-agent') ?? '').toLowerCase()
  for (const pattern of BLOCKED_BOT_PATTERNS) {
    if (ua.includes(pattern)) {
      return new NextResponse(null, { status: 444 })
    }
  }

  const origin = request.headers.get('origin')
  const referer = request.headers.get('referer')

  if (origin && !isAllowed(origin)) {
    return NextResponse.json({ error: 'Forbidden' }, { status: 403 })
  }
  if (referer) {
    const refUrl = referer.replace(/\/$/, "")
    if (!isAllowed(refUrl)) {
      return NextResponse.json({ error: 'Forbidden' }, { status: 403 })
    }
  }

  return NextResponse.next()
}

export const config = {
  matcher: ['/api/:path*'],
}
