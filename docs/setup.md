# Setup guide

The Webotee MCP connector is **hosted** — you don't install or run a server. You add one URL to your AI client and sign in with your Webotee account (OAuth).

**Connector URL:** `https://app.webotee.com/mcp`
**Requires:** a paid Webotee plan — Starter ($29/mo, 7‑day free trial) or higher. [Start a trial →](https://www.webotee.com/amazon-product-research-mcp)

---

## Claude

Works in Claude Desktop and Claude on the web.

1. Open **Settings → Connectors**.
2. Choose **Add custom connector**.
3. Paste the URL: `https://app.webotee.com/mcp`
4. Complete the **Webotee sign‑in** in the OAuth prompt that appears.
5. **Approve access.** Webotee's research tools are now available in your chat.

Prefer config files (Claude Desktop)? See [`examples/configs/claude_desktop_config.json`](../examples/configs/claude_desktop_config.json).

---

## ChatGPT

ChatGPT reaches remote MCP servers through **Developer Mode**. Available on paid ChatGPT plans; on Business/Enterprise/Edu a workspace admin may need to allow custom connectors first.

1. **Settings → Apps & Connectors.**
2. Open **Advanced settings** and turn on **Developer Mode**.
3. Choose **Create** (a new connector / app).
4. Add a name (e.g. "Webotee"), a short description, and the server URL `https://app.webotee.com/mcp` — set authentication to **OAuth**.
5. **Save**, start a new chat, enable **Webotee** from the **+** (tools) menu, and approve the Webotee sign‑in when prompted.

---

## Cursor / VS Code / Claude Code (and any local‑stdio client)

If your client only supports local stdio servers, bridge to the hosted connector with [`mcp-remote`](https://www.npmjs.com/package/mcp-remote):

```jsonc
{
  "mcpServers": {
    "webotee": {
      "command": "npx",
      "args": ["-y", "mcp-remote", "https://app.webotee.com/mcp"]
    }
  }
}
```

- **Cursor:** add to `~/.cursor/mcp.json` (or project `.cursor/mcp.json`) — see [`examples/configs/cursor_mcp.json`](../examples/configs/cursor_mcp.json).
- **VS Code:** add to `.vscode/mcp.json` — see [`examples/configs/vscode_mcp.json`](../examples/configs/vscode_mcp.json).
- **Claude Code:** `claude mcp add --transport http webotee https://app.webotee.com/mcp` (native remote MCP; no proxy needed).

On first run, `mcp-remote` opens a browser for the Webotee OAuth sign‑in and caches the token locally.

---

## Verify

Ask your assistant: *"List the Webotee tools you can use,"* then try *"Find under‑competed brands under $50."* If you're on the Free tier you'll get a clear upgrade prompt — the connector requires a paid plan.

Troubleshooting and the auth model: [`auth.md`](./auth.md).
