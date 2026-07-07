I found the root causes. Here's the analysis:

---

## Why fallback questions still fire — 4 failure points

### 1. 🔴 **Jina Reader scraping fails first** (most likely cause)
The pipeline fetches docs via `https://r.jina.ai/` (Jina Reader) with an **8-second timeout** and **300ms delay**. If Jina is rate-limited, down, or slow — which happens often on the free tier — the scrape returns `< 200 chars`, and the app **falls back at line 713** *before even trying Groq*.

```
scrape fails → chars < 200 → FALLBACK (line 713-723)
```

### 2. 🔴 **Single-shot generation — no retry loop**
The Groq generation block (lines 772-800) runs **exactly once**. If the model returns poor quality:
- `validQuestions < 5` → throws → caught → **fallback (line 807)**
- Even with 7 keys, it only hits **one** key (`workingKeys[0]`)

### 3. 🔶 **Partial results: 3-4 valid questions → silently truncated quiz**
If Groq returns 3 or 4 good questions, the code sets `lastValid` then throws "retrying" — but there's no retry. It serves a quiz with 3-4 questions instead of 5. User sees fewer questions, not the hardcoded fallback.

### 4. 🔶 **Ping passes, generation fails (HTTP error or timeout)**
All 7 keys pass the 5s ping test, but the actual generation call (30s timeout, `max_tokens: 2048`) can still time out or return HTTP 429/500. No fallback key is tried — only `workingKeys[0]` is used.

---

## Root cause summary

| Issue | Impact | Where |
|---|---|---|
| **Jina Reader is unreliable** on free tier | **hard fallback** (scrapedText < 200) | line 713 |
| **No retry** on bad LLM output | **hard fallback** after 1 bad generation | lines 786-800 |
| **No key rotation** if generation fails | falls back instead of trying key 2, 3, … | line 596: `workingKeys[0]` |
| Function timeout (60s ceiling) | race condition: scrape + gen must fit in window | line 2 |

You have **7 healthy keys and 3.5M tokens/day** — the bottleneck isn't Groq capacity, it's that the pipeline gives up after one attempt instead of retrying with the next key.
