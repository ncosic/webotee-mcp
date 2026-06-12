"""Thin async convenience client for the hosted Webotee MCP connector.

A small wrapper over the official MCP SDK so you can call Webotee tools in a few
lines. The server stays hosted at https://app.webotee.com/mcp — this is just a
typed-ish convenience layer over Streamable HTTP + OAuth.

    from webotee_mcp import WeboteeMCP

    async with WeboteeMCP() as wb:
        print(await wb.list_tool_names())
        rows = await wb.call("find_undercompeted_brands", max_avg_price=50, limit=5)

Requires a paid Webotee plan: https://www.webotee.com/amazon-product-research-mcp
"""

from __future__ import annotations

from contextlib import AsyncExitStack
from typing import Any

from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client

SERVER_URL = "https://app.webotee.com/mcp"


class WeboteeMCP:
    """Async context manager wrapping a Webotee MCP session.

    Pass your own `auth` (an mcp OAuthClientProvider or compatible) to control
    the sign-in / token storage. With no auth, the SDK will negotiate OAuth and
    your token storage must be supplied via `auth` for non-interactive use.
    """

    def __init__(self, server_url: str = SERVER_URL, auth: Any | None = None) -> None:
        self.server_url = server_url
        self._auth = auth
        self._stack: AsyncExitStack | None = None
        self._session: ClientSession | None = None

    async def __aenter__(self) -> "WeboteeMCP":
        self._stack = AsyncExitStack()
        read, write, _ = await self._stack.enter_async_context(
            streamablehttp_client(self.server_url, auth=self._auth)
        )
        self._session = await self._stack.enter_async_context(ClientSession(read, write))
        await self._session.initialize()
        return self

    async def __aexit__(self, *exc: object) -> None:
        if self._stack is not None:
            await self._stack.aclose()
        self._stack = None
        self._session = None

    def _require(self) -> ClientSession:
        if self._session is None:
            raise RuntimeError("Use `async with WeboteeMCP() as wb:` before calling.")
        return self._session

    async def list_tool_names(self) -> list[str]:
        tools = await self._require().list_tools()
        return [t.name for t in tools.tools]

    async def call(self, tool: str, **arguments: Any) -> str:
        """Call a Webotee tool and return its concatenated text output."""
        result = await self._require().call_tool(tool, arguments)
        return "\n".join(
            b.text for b in result.content if getattr(b, "type", None) == "text"
        )
