"""Webotee AI Connect — thin Python client for the hosted Amazon Product Research MCP.

https://www.webotee.com/amazon-product-research-mcp
"""

from .client import SERVER_URL, WeboteeMCP

__all__ = ["WeboteeMCP", "SERVER_URL"]
__version__ = "1.0.0"
