# Build target for MCP directory crawlers (e.g. Glama).
#
# This builds the repo's Python package and runs the introspection-only catalog
# stub (`webotee-mcp-stub`) over stdio, so a crawler can enumerate + quality-score
# the tool catalog WITHOUT a browser OAuth round-trip. It contacts nothing and runs
# no research — see webotee_mcp/stub.py.
#
# The real Webotee server is fully HOSTED at https://app.webotee.com/mcp. End users
# do not build this image — they add that URL as a remote MCP connector in
# Claude/ChatGPT, or (for stdio-only clients) run
# `npx -y mcp-remote https://app.webotee.com/mcp` per the README. Nothing to self-host.
#
# Mirrors Glama's own working build (debian + uv + mcp-proxy); only the launch
# command differs (runs the stub instead of the MCP SDK CLI).
FROM debian:trixie-slim
RUN apt-get update && apt-get install -y --no-install-recommends ca-certificates curl \
 && curl -fsSL https://deb.nodesource.com/setup_24.x | bash - \
 && apt-get install -y --no-install-recommends nodejs \
 && npm install -g mcp-proxy@6.4.3 \
 && curl -LsSf https://astral.sh/uv/install.sh | UV_INSTALL_DIR="/usr/local/bin" sh \
 && apt-get clean && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY . /app
RUN uv sync
CMD ["mcp-proxy", "--", "uv", "run", "webotee-mcp-stub"]
