"""
Webotee AI Connect — Python quickstart.

Connects to the hosted Webotee MCP server over Streamable HTTP, completes the
OAuth sign-in in your browser, lists the available tools, and calls one.

Requires a PAID Webotee plan (Starter or higher): https://www.webotee.com/amazon-product-research-mcp

    pip install "mcp>=1.9"
    python examples/quickstart.py

This is a reference example. It uses the official MCP Python SDK's OAuth client
helper; on first run it opens a browser to sign in to Webotee and caches the
token in memory for the duration of the run.
"""

import asyncio
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

from mcp.client.auth import OAuthClientProvider, TokenStorage
from mcp.client.session import ClientSession
from mcp.client.streamable_http import streamablehttp_client
from mcp.shared.auth import OAuthClientInformationFull, OAuthClientMetadata, OAuthToken

SERVER_URL = "https://app.webotee.com/mcp"
CALLBACK_PORT = 33418  # local loopback port that catches the OAuth redirect


class InMemoryTokenStorage(TokenStorage):
    """Minimal token store. Swap for a file/keyring store to persist across runs."""

    def __init__(self) -> None:
        self._tokens: OAuthToken | None = None
        self._client_info: OAuthClientInformationFull | None = None

    async def get_tokens(self) -> OAuthToken | None:
        return self._tokens

    async def set_tokens(self, tokens: OAuthToken) -> None:
        self._tokens = tokens

    async def get_client_info(self) -> OAuthClientInformationFull | None:
        return self._client_info

    async def set_client_info(self, client_info: OAuthClientInformationFull) -> None:
        self._client_info = client_info


def _wait_for_callback() -> tuple[str, str | None]:
    """Run a one-shot loopback HTTP server to capture (code, state) from the redirect."""
    result: dict[str, str | None] = {}

    class Handler(BaseHTTPRequestHandler):
        def do_GET(self):  # noqa: N802
            params = parse_qs(urlparse(self.path).query)
            result["code"] = params.get("code", [None])[0]
            result["state"] = params.get("state", [None])[0]
            self.send_response(200)
            self.send_header("Content-Type", "text/html")
            self.end_headers()
            self.wfile.write(b"<h3>Webotee connected. You can close this tab.</h3>")

        def log_message(self, *_):  # silence
            return

    server = HTTPServer(("127.0.0.1", CALLBACK_PORT), Handler)
    server.handle_request()  # blocks until the single redirect arrives
    return result.get("code", ""), result.get("state")


def _build_auth_provider() -> OAuthClientProvider:
    """Reusable OAuth client provider for the hosted Webotee connector.

    Imported by scripts/gen_tools.py so both share one auth flow.
    """
    return OAuthClientProvider(
        server_url=SERVER_URL,
        client_metadata=OAuthClientMetadata(
            client_name="Webotee Quickstart",
            redirect_uris=[f"http://127.0.0.1:{CALLBACK_PORT}/callback"],
            grant_types=["authorization_code", "refresh_token"],
            response_types=["code"],
        ),
        storage=InMemoryTokenStorage(),
        redirect_handler=lambda url: asyncio.create_task(_open(url)),
        callback_handler=lambda: asyncio.to_thread(_wait_for_callback),
    )


async def main() -> None:
    auth = _build_auth_provider()

    async with streamablehttp_client(SERVER_URL, auth=auth) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()

            tools = await session.list_tools()
            print(f"\nWebotee exposes {len(tools.tools)} tools. A few:")
            for t in tools.tools[:8]:
                print(f"  - {t.name}")

            print("\nCalling find_undercompeted_brands (max_avg_price=50)...\n")
            result = await session.call_tool(
                "find_undercompeted_brands", {"max_avg_price": 50, "limit": 5}
            )
            for block in result.content:
                if getattr(block, "type", None) == "text":
                    print(block.text)


async def _open(url: str) -> None:
    print(f"Opening browser to sign in to Webotee:\n  {url}\n")
    webbrowser.open(url)


if __name__ == "__main__":
    asyncio.run(main())
