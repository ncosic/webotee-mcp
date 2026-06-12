# Authentication

Webotee AI Connect uses **OAuth 2.1** — there are no API keys to copy or store.

## How it works

- The connector is an MCP **Resource Server** at `https://app.webotee.com/mcp`, protected by an OAuth **Authorization Server** on the same domain.
- Standards: OAuth 2.1 with **PKCE (S256)**, Dynamic Client Registration (RFC 7591), protected‑resource + authorization‑server metadata (RFC 9728 / RFC 8414), and resource indicators (RFC 8707).
- Discovery endpoints (public):
  - `https://app.webotee.com/.well-known/oauth-protected-resource`
  - `https://app.webotee.com/.well-known/oauth-authorization-server`
- Your client registers itself, opens a browser for you to sign in to Webotee, and receives a short‑lived **access token** (refreshed automatically). Tokens are opaque and **revocable** — you can disconnect at any time and the token is invalidated server‑side.

## Tiers & limits

- The connector requires a **paid plan** (Starter or higher). Free accounts receive an empty tool list plus a machine‑readable "upgrade to unlock" response — never an error.
- Each tool call counts against your plan's **daily AI Connect allowance** (Starter 200 · Scout 1,000 · Scout Pro 3,000 · Scout + Protect 10,000). When you hit the cap, the connector returns a clear limit message.

## Privacy & scope

- The connector **reads and explains** Webotee's research dataset and manages your own Webotee workspace (watchlists, cost floors). **No tool places orders or changes your Amazon listings.**
- No Amazon Seller Central credentials are involved. You authenticate to **Webotee**, not to Amazon.

## Disconnect

Remove the connector in your AI client, and/or revoke it from your Webotee account. See [`SECURITY.md`](../SECURITY.md) to report a security issue.
