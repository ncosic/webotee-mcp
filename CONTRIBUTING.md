# Contributing

Thanks for your interest! A quick note on scope so PRs land smoothly.

This is the **public client + docs** repository for the **hosted** Webotee AI
Connect connector. The MCP server, its dataset and tool implementations are
hosted at `https://app.webotee.com/mcp` and are **not** part of this repo — so
there's no server code to contribute here.

**Great contributions:**

- Fixes/improvements to the **setup docs**, **example prompts**, and **client
  configs** (Claude, ChatGPT, Cursor, VS Code, Claude Code).
- Bug fixes to the **example client**, the **`webotee_mcp` SDK**, or
  **`scripts/gen_tools.py`**.
- New client integrations or quickstarts in additional languages.
- Typo/clarity fixes, broken‑link fixes.

**Out of scope here:** the hosted service, its data, pricing, tool logic, or
account/billing behavior. For those, or anything product‑related, use
https://www.webotee.com/contact.

**How:** open an issue to discuss non‑trivial changes first, then a PR against
`main`. Keep examples runnable and docs accurate (regenerate the tool dump with
`python scripts/gen_tools.py` if tool names change). Security issues: see
[`SECURITY.md`](./SECURITY.md) — do not file them as public issues.
