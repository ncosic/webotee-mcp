# Tool catalog

Webotee AI Connect exposes **50+ research tools** to your AI. Your assistant decides which to call from your plain‑language question; you don't call them by hand.

> **Authoritative source:** the live connector's `tools/list` (tier‑gated) is the single source of truth for tool names, descriptions and parameters. This file is a human summary — regenerate it any time with [`scripts/gen_tools.py`](../scripts/gen_tools.py). Tools that change your Webotee **workspace** (watchlists, cost floors) write only to your Webotee account; **no tool places orders or changes your Amazon listings.**
>
> **Glossary:** an **operator** is a professional, often cross‑brand, third‑party **seller**. **Marketplaces:** `1` = Amazon UK, `2` = Amazon US (default), with select Amazon↔Walmart cross‑marketplace tools.

## Product & ASIN sourcing
| Tool | What it does |
|---|---|
| `search_products` | Free‑text keyword search over product titles/descriptions; returns brand, price, 30‑day demand, fulfillment (FBA/Amazon/FBM) and rating. |
| `top_sourcing_picks` | Top sourcing‑pick ASINs across the catalog with filters (price band, category, brand, exclude gated, exclude Amazon PL, min velocity). |
| `evaluate_asin_sourcing` | Score one ASIN for FBA sourcing: composite 0–100 + 5 dimensions (velocity, gating, friction, margin, brand posture), demand, est. 30‑day revenue, ship‑by days, red flags. |
| `asin_profit_calc` | Estimate whether an ASIN hits a target margin given buy‑box price, est. FBA fees and referral fee; or breakeven COGS. |
| `asin_comparables` | Find ASINs similar to a given ASIN by brand, price band and seller count. |
| `asin_buybox_history` | Buy‑box seller history for an ASIN over the observed window. |
| `collect_asin_now` | On‑demand single‑ASIN snapshot (current title, price, today's offers/sellers) alongside Webotee's historical intelligence. Amazon US, one ASIN per call. |

## Brand intelligence
| Tool | What it does |
|---|---|
| `evaluate_brand` | Brand‑level portfolio read: control posture, winner diversity (HHI), Amazon retail %, FBA %, churn, demand, est. revenue, ship‑by, cross‑brand seller count, top 10 ASINs. |
| `brand_buybox_trajectory` | A brand's buy‑box winner trajectory over time. |
| `brand_new_asins` | A brand's newly‑appeared ASINs. |
| `brand_similar` | Brands similar to a given brand by category, price tier and competition level. |
| `brand_under_attack` | Detect competitive attack: surge in new sellers, buy‑box churn or price drops. |
| `brands_gaining_sellers` | Brands gaining sellers (rising competition / pressure signal). |
| `brands_in_operator_network` | Brands that share sellers with a target brand — the operator graph through shared distribution. |
| `find_undercompeted_brands` | Flagship discovery: brands with low seller competition but real sales presence (price/seller/sales filters; seed from a reference brand). |
| `find_brands_with_high_seller_churn` | Brands with high buy‑box / seller churn. |
| `find_deconcentrating_brands` | Brands whose seller concentration is falling — opening up. |
| `find_single_seller_brands` | Brands held by a single dominant seller (a target to compete with). |
| `filter_brands_by_fba_share` | Brands filtered by FBA share of the buy box. |
| `top_velocity_brands` | Highest sales‑velocity brands. |
| `category_undercompeted_brands` | Under‑competed brands within a specific category. |

## Seller / operator network
| Tool | What it does |
|---|---|
| `find_new_operators` | Brand‑new sellers that recently started selling. |
| `operator_compare` | Two sellers head‑to‑head: brand / ASIN / category overlap and marketplace presence. |
| `operator_top_brands` | The brands a seller carries most, ranked by estimated 30‑day sales (or buy‑box days / ASIN count). |
| `operator_top_asins` | The ASINs a seller wins most, ranked by estimated 30‑day sales, with normalized buy‑box share. |
| `operator_brands_by_competition` | A seller's brands ranked by fewest competing sellers. |
| `operator_category_dominance` | Which categories a seller dominates. |
| `operator_new_brands` | Brands a seller recently added. |
| `operator_lost_brands` | Brands a seller recently dropped. |
| `top_expanding_operators` | Sellers expanding fastest (adding brands). |
| `filter_operators_by_fba_share` | Sellers filtered by FBA share. |

## Category & niche
| Tool | What it does |
|---|---|
| `find_underserved_niches` | Under‑served sub‑categories with real demand and room to compete, ranked by private‑label winnability. Returns categories, never brands. |
| `evaluate_category_for_private_label` | Is a category/niche winnable for a new private‑label brand? Per‑signal pass/fail + Strong/Moderate/Weak verdict. |
| `category_metrics` | Per‑category metrics: sellers, demand, concentration. |
| `category_new_entrants` | Brands/sellers newly entering a category. |
| `category_top_growers` | Fastest‑growing brands in a category. |
| `categories_amazon_retreating` | Categories where Amazon retail is retreating — openings for third‑party sellers. |
| `competitive_landscape` | For a brand or category: top sellers by buy‑box days, top brands by winner‑diversity HHI, with week‑over‑week deltas. |

## Cross‑marketplace (Amazon ↔ Walmart)
| Tool | What it does |
|---|---|
| `xmkt_pricing_compare` | Matched Amazon vs Walmart pricing, delta %, and a coarse FBA profitability check (single‑ASIN or by brand). |
| `brand_xmarket` | A brand's Amazon vs Walmart cross‑marketplace presence. |
| `operator_xmarket_presence` | A seller's Amazon vs Walmart presence. |

## Pricing, gating & protection
| Tool | What it does |
|---|---|
| `gating_repricing_advice` | Ungate / arbitrage / avoid recommendation for an ASIN, with a rationale citing named metrics. |
| `set_cost_floor` | Set your cost floor for an ASIN/brand (workspace setting for margin/repricing context). |
| `map_violations_today` | Active MAP (Minimum Advertised Price) violations for products in your workspace. |
| `unauthorized_sellers` | Given a brand + your authorized‑seller list, flag sellers who are not authorized. |
| `risk_assessment` | Composite risk score for an ASIN or brand: recent MAP events, unauthorized sellers, recommended actions. |

## Watchlist & monitoring
| Tool | What it does |
|---|---|
| `watchlist_add` | Create or add to a saved tracking list (ASINs, brands, sellers, niches); captures a baseline. |
| `watchlist_add_rule` | Add an alert rule to a watchlist. |
| `watchlist_list` | List your watchlists and their items. |
| `watchlist_delta` | What changed since the watchlist's baseline (new sellers, score moves). |
| `watchlist_diff` | Diff two watchlist snapshots. |
| `watchlist_remove` | Remove items or a whole watchlist. |
