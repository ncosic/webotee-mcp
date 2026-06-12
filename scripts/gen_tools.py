"""
Regenerate the tool catalog from the LIVE connector so docs never drift.

Connects to https://app.webotee.com/mcp, signs in (OAuth, browser), pulls
`tools/list`, and writes docs/tools.generated.md — a flat, always-accurate dump
of every tool name + description your plan can see. The curated, grouped
docs/tools.md stays the human-friendly version; regenerate this alongside it
whenever the registry changes.

    pip install "mcp>=1.9"
    python scripts/gen_tools.py

Reuses the OAuth flow from examples/quickstart.py (paid plan required).
"""

import asyncio
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "examples"))

from mcp.client.session import ClientSession  # noqa: E402
from mcp.client.streamable_http import streamablehttp_client  # noqa: E402

from quickstart import SERVER_URL, _build_auth_provider  # noqa: E402  (see note below)

OUT = os.path.join(os.path.dirname(__file__), "..", "docs", "tools.generated.md")


async def main() -> None:
    auth = _build_auth_provider()
    async with streamablehttp_client(SERVER_URL, auth=auth) as (read, write, _):
        async with ClientSession(read, write) as session:
            await session.initialize()
            tools = sorted((await session.list_tools()).tools, key=lambda t: t.name)

    lines = [
        "# Tool catalog (generated)",
        "",
        f"> Auto-generated from the live connector's `tools/list`. {len(tools)} tools "
        "visible to the plan used to generate this. Do not edit by hand — run "
        "`python scripts/gen_tools.py`.",
        "",
        "| Tool | Description |",
        "|---|---|",
    ]
    for t in tools:
        desc = (t.description or "").replace("\n", " ").replace("|", "\\|").strip()
        lines.append(f"| `{t.name}` | {desc} |")

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"Wrote {len(tools)} tools -> {os.path.relpath(OUT)}")


if __name__ == "__main__":
    asyncio.run(main())
