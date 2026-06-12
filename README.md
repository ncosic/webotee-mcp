# Webotee — Amazon Product Research MCP

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](./LICENSE)
[![Smoke test](https://github.com/webotee/webotee-mcp/actions/workflows/smoke.yml/badge.svg)](https://github.com/webotee/webotee-mcp/actions/workflows/smoke.yml)
[![MCP](https://img.shields.io/badge/MCP-Streamable_HTTP-5A4FCF.svg)](https://modelcontextprotocol.io)

**Amazon brand, seller, niche & buy-box intelligence — inside your own Claude or ChatGPT.**

Webotee AI Connect adds Webotee's Amazon operator, brand, niche and seller research dataset to the AI you already use. Ask a question in Claude or ChatGPT and it queries the Webotee dataset directly — a research connector for sellers, built on 2+ years of daily US (and UK) marketplace observations of the BSR top‑1M+.

👉 **Product page / start a 7‑day free trial:** https://www.webotee.com/amazon-product-research-mcp

This repository is the **public client + docs + manifest** for the connector. The Webotee MCP server is hosted and runs at `https://app.webotee.com/mcp` — you don't install or run it; you add it to your assistant and sign in with your Webotee account.

---

## What you can ask (in your own Claude or ChatGPT)

- *"Which sellers dominate the buy box on `<brand>`?"*
- *"Find under‑competed sub‑categories worth sourcing in home & kitchen."*
- *"What other brands does seller `<X>` carry, by estimated sales?"*
- *"Who's controlled the buy box on ASIN `<B0…>` over the past 24 months?"*
- *"Score this ASIN for FBA sourcing — velocity, gating risk, margin."*
- *"Is `<brand>` under attack — new sellers flooding the listings?"*
- *"Show unauthorized sellers on `<brand>` given my authorized list."*
- *"Compare this ASIN's price on Amazon vs Walmart."*

See [`examples/prompts.md`](./examples/prompts.md) for more, and [`docs/tools.md`](./docs/tools.md) for the full tool catalog (50+ research tools).

---

## Requirements

- A **paid Webotee plan** — Starter ($29/mo, 7‑day free trial) or higher. [Start a trial →](https://www.webotee.com/amazon-product-research-mcp)
- An AI client that supports remote MCP connectors: **Claude** (Desktop/Web), **ChatGPT** (Developer Mode), **Cursor**, **VS Code**, **Claude Code**.
- Sign‑in is via **OAuth** in your browser — no API keys to copy, nothing to store.

---

## Setup (~2 minutes)

The connector URL is the same everywhere:

```
https://app.webotee.com/mcp
```

**Claude (Desktop or Web):** Settings → Connectors → **Add custom connector** → paste the URL → complete the Webotee sign‑in (OAuth) → approve. Full steps: [`docs/setup.md`](./docs/setup.md#claude).

**ChatGPT:** Settings → Apps & Connectors → enable **Developer Mode** → Create → name it "Webotee", paste the URL, set auth to **OAuth** → enable it from the **+** (tools) menu in a chat. Steps: [`docs/setup.md`](./docs/setup.md#chatgpt).

**Cursor / VS Code / Claude Code (or any client that only speaks local stdio):** point it at the remote server through [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```jsonc
// examples/configs/cursor_mcp.json
{
  "mcpServers": {
    "webotee": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://app.webotee.com/mcp"]
    }
  }
}
```

Ready‑to‑paste configs: [`examples/configs/`](./examples/configs). Auth details: [`docs/auth.md`](./docs/auth.md).

---

## Pricing & daily AI Connect limits

The connector is available on every paid plan; each tool call your AI makes counts as one AI Connect call against that day's allowance.

| Plan | Price | AI Connect calls / day |
|---|---|---|
| Starter | $29/mo (7‑day trial) | 200 |
| Scout | $89/mo | 1,000 |
| Scout Pro | $179/mo | 3,000 |
| Scout + Protect | $295/mo | 10,000 |

Full pricing: https://www.webotee.com/pricing

---

## What it is — and isn't

- **It is** Amazon seller research surfaced as tools your AI can call: brands, sellers, ASINs, niches, buy‑box history and cross‑marketplace overlap, from a pre‑collected research dataset.
- **It is not** a live shopping agent and not an account‑automation bot. The connector **reads and explains** — it does **not** place orders or change your Amazon listings. Answers come from historical, pre‑collected intelligence, so they're consistent, fast and citeable. Treat every answer as a researched starting point to validate, not a guarantee.

---

## Links

- **Product / trial:** https://www.webotee.com/amazon-product-research-mcp
- **Pricing:** https://www.webotee.com/pricing
- **Tool catalog:** [`docs/tools.md`](./docs/tools.md)
- **Setup guide:** [`docs/setup.md`](./docs/setup.md)
- **Quickstart (Python):** [`examples/quickstart.py`](./examples/quickstart.py)

A product by CP Development d.o.o. · Amazon is a trademark of Amazon.com, Inc.; Webotee is not affiliated with Amazon. · [MIT License](./LICENSE)
