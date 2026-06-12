# Security policy

## Reporting a vulnerability

If you find a security issue in the Webotee AI Connect connector, the hosted MCP
server, or anything in this repository, please report it privately:

- Email **security@webotee.com** (preferred), or use the contact form at
  https://www.webotee.com/contact.
- Please do **not** open a public GitHub issue for security reports.

Include steps to reproduce, affected endpoints/tools, and any logs. We aim to
acknowledge reports promptly and will keep you updated through resolution.
Please give us reasonable time to remediate before any public disclosure.

## Authentication model

- The connector authenticates with **OAuth 2.1** (PKCE S256, Dynamic Client
  Registration); see [`docs/auth.md`](./docs/auth.md). There are no API keys to
  copy or store.
- Access tokens are short-lived, opaque and **server-side revocable**.
- You authenticate to **Webotee**, not to Amazon — no Seller Central credentials
  are involved.
- The connector reads Webotee's research dataset and manages your own Webotee
  workspace; no tool places orders or changes your Amazon listings.

## Scope

This repository is the public client/docs/manifest. The Webotee server, its
dataset and infrastructure are hosted and not part of this repo.
