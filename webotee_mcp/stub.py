"""
Introspection-only stub for the hosted Webotee AI Connect (Amazon Product Research) MCP.

The real Webotee server is fully hosted at https://app.webotee.com/mcp and is
OAuth-gated for execution. This tiny local stdio server exists ONLY so MCP
directory crawlers (e.g. Glama) can build, start and introspect the tool catalog
without a browser OAuth round-trip: it advertises the same research tools the
hosted connector exposes and answers `initialize` + `tools/list`. Calling any
tool just returns a pointer to the hosted endpoint -- this stub never contacts
Amazon, runs no research, and stores nothing.

    uv run webotee-mcp-stub      # or:  python -m webotee_mcp.stub

To actually use the tools, add https://app.webotee.com/mcp as a remote MCP
connector in Claude/ChatGPT and sign in with your Webotee account (see README).
"""
from __future__ import annotations

import asyncio

import mcp.types as types
from mcp.server.lowlevel import Server
from mcp.server.stdio import stdio_server

# (name, description) for every tool the hosted connector exposes.
# Generated from docs/tools.md -- the curated mirror of the live `tools/list`.
TOOLS: list[tuple[str, str]] = [
    ('search_products', 'Free‑text keyword search over product titles/descriptions; returns brand, price, 30‑day demand, fulfillment (FBA/Amazon/FBM) and rating.'),
    ('top_sourcing_picks', 'Top sourcing‑pick ASINs across the catalog with filters (price band, category, brand, exclude gated, exclude Amazon PL, min velocity).'),
    ('evaluate_asin_sourcing', 'Score one ASIN for FBA sourcing: composite 0–100 + 5 dimensions (velocity, gating, friction, margin, brand posture), demand, est. 30‑day revenue, ship‑by days, red flags.'),
    ('asin_profit_calc', 'Estimate whether an ASIN hits a target margin given buy‑box price, est. FBA fees and referral fee; or breakeven COGS.'),
    ('asin_comparables', 'Find ASINs similar to a given ASIN by brand, price band and seller count.'),
    ('asin_buybox_history', 'Buy‑box seller history for an ASIN over the observed window.'),
    ('collect_asin_now', "On‑demand single‑ASIN snapshot (current title, price, today's offers/sellers) alongside Webotee's historical intelligence. Amazon US, one ASIN per call."),
    ('evaluate_brand', 'Brand‑level portfolio read: control posture, winner diversity (HHI), Amazon retail %, FBA %, churn, demand, est. revenue, ship‑by, cross‑brand seller count, top 10 ASINs.'),
    ('brand_buybox_trajectory', "A brand's buy‑box winner trajectory over time."),
    ('brand_new_asins', "A brand's newly‑appeared ASINs."),
    ('brand_similar', 'Brands similar to a given brand by category, price tier and competition level.'),
    ('brand_under_attack', 'Detect competitive attack: surge in new sellers, buy‑box churn or price drops.'),
    ('brands_gaining_sellers', 'Brands gaining sellers (rising competition / pressure signal).'),
    ('brands_in_operator_network', 'Brands that share sellers with a target brand — the operator graph through shared distribution.'),
    ('find_undercompeted_brands', 'Flagship discovery: brands with low seller competition but real sales presence (price/seller/sales filters; seed from a reference brand).'),
    ('find_brands_with_high_seller_churn', 'Brands with high buy‑box / seller churn.'),
    ('find_deconcentrating_brands', 'Brands whose seller concentration is falling — opening up.'),
    ('find_single_seller_brands', 'Brands held by a single dominant seller (a target to compete with).'),
    ('filter_brands_by_fba_share', 'Brands filtered by FBA share of the buy box.'),
    ('top_velocity_brands', 'Highest sales‑velocity brands.'),
    ('category_undercompeted_brands', 'Under‑competed brands within a specific category.'),
    ('find_new_operators', 'Brand‑new sellers that recently started selling.'),
    ('operator_compare', 'Two sellers head‑to‑head: brand / ASIN / category overlap and marketplace presence.'),
    ('operator_top_brands', 'The brands a seller carries most, ranked by estimated 30‑day sales (or buy‑box days / ASIN count).'),
    ('operator_top_asins', 'The ASINs a seller wins most, ranked by estimated 30‑day sales, with normalized buy‑box share.'),
    ('operator_brands_by_competition', "A seller's brands ranked by fewest competing sellers."),
    ('operator_category_dominance', 'Which categories a seller dominates.'),
    ('operator_new_brands', 'Brands a seller recently added.'),
    ('operator_lost_brands', 'Brands a seller recently dropped.'),
    ('top_expanding_operators', 'Sellers expanding fastest (adding brands).'),
    ('filter_operators_by_fba_share', 'Sellers filtered by FBA share.'),
    ('find_underserved_niches', 'Under‑served sub‑categories with real demand and room to compete, ranked by private‑label winnability. Returns categories, never brands.'),
    ('evaluate_category_for_private_label', 'Is a category/niche winnable for a new private‑label brand? Per‑signal pass/fail + Strong/Moderate/Weak verdict.'),
    ('category_metrics', 'Per‑category metrics: sellers, demand, concentration.'),
    ('category_new_entrants', 'Brands/sellers newly entering a category.'),
    ('category_top_growers', 'Fastest‑growing brands in a category.'),
    ('categories_amazon_retreating', 'Categories where Amazon retail is retreating — openings for third‑party sellers.'),
    ('competitive_landscape', 'For a brand or category: top sellers by buy‑box days, top brands by winner‑diversity HHI, with week‑over‑week deltas.'),
    ('xmkt_pricing_compare', 'Matched Amazon vs Walmart pricing, delta %, and a coarse FBA profitability check (single‑ASIN or by brand).'),
    ('brand_xmarket', "A brand's Amazon vs Walmart cross‑marketplace presence."),
    ('operator_xmarket_presence', "A seller's Amazon vs Walmart presence."),
    ('gating_repricing_advice', 'Ungate / arbitrage / avoid recommendation for an ASIN, with a rationale citing named metrics.'),
    ('set_cost_floor', 'Set your cost floor for an ASIN/brand (workspace setting for margin/repricing context).'),
    ('map_violations_today', 'Active MAP (Minimum Advertised Price) violations for products in your workspace.'),
    ('unauthorized_sellers', 'Given a brand + your authorized‑seller list, flag sellers who are not authorized.'),
    ('risk_assessment', 'Composite risk score for an ASIN or brand: recent MAP events, unauthorized sellers, recommended actions.'),
    ('watchlist_add', 'Create or add to a saved tracking list (ASINs, brands, sellers, niches); captures a baseline.'),
    ('watchlist_add_rule', 'Add an alert rule to a watchlist.'),
    ('watchlist_list', 'List your watchlists and their items.'),
    ('watchlist_delta', "What changed since the watchlist's baseline (new sellers, score moves)."),
    ('watchlist_diff', 'Diff two watchlist snapshots.'),
    ('watchlist_remove', 'Remove items or a whole watchlist.'),
]

_INPUT_SCHEMA = {"type": "object", "properties": {}, "additionalProperties": True}

_CALL_NOTE = (
    "This is the discovery/catalog stub for Webotee AI Connect. Tools execute on the "
    "hosted endpoint https://app.webotee.com/mcp -- add it as a remote MCP connector in "
    "Claude or ChatGPT and sign in with your Webotee account to run them."
)

server = Server("webotee-amazon-product-research")


@server.list_tools()
async def list_tools() -> list[types.Tool]:
    return [
        types.Tool(name=name, description=description, inputSchema=_INPUT_SCHEMA)
        for name, description in TOOLS
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict | None = None) -> list[types.TextContent]:
    return [types.TextContent(type="text", text=_CALL_NOTE)]


async def _run() -> None:
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


def main() -> None:
    asyncio.run(_run())


if __name__ == "__main__":
    main()
