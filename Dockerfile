# Thin local stdio <-> remote bridge for the hosted Webotee MCP connector.
# The Webotee server is NOT in this image; this only runs `mcp-remote`, which
# forwards a local stdio MCP connection to https://app.webotee.com/mcp and
# handles the browser OAuth sign-in. Useful for clients that only speak stdio.
#
#   docker build -t webotee-mcp .
#   docker run -i --rm webotee-mcp
FROM node:22-alpine
ENTRYPOINT ["npx", "-y", "mcp-remote", "https://app.webotee.com/mcp"]
