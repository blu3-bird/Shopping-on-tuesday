# Meesho Scraping Strategy

## Status
Not started — awaiting approval.

## Why scraping
Meesho has no usable public API for resellers/dropshippers. Scraping the public website is the only way to import products without API approval.

## Risks
- Meesho can change HTML selectors at any time → scraper breaks
- Rate limiting / IP blocking if we scrape too aggressively
- Terms of service — must be respectful, no aggressive crawling
- Product data quality varies (missing images, wrong prices)

## Planned approach (to be designed in detail)
1. Use `requests` + `BeautifulSoup` (lightweight, no browser needed) — OR Selenium/Playwright if pages are JS-rendered
2. Respect `robots.txt`, add delays between requests
3. Store scraped products in our DB with a `source_url` field pointing back to Meesho
4. Add a `last_synced` timestamp so we can refresh prices/stock
5. Add a `markup_percentage` field so you control your resale price
6. Admin can trigger a sync, review imported products before publishing

## Data to scrape per product
- Product title
- Price (Meesho price)
- Original price / MRP
- Description
- Category
- Images (primary + gallery)
- Stock availability
- Product URL (source link)

## Design principle
The scraping layer is isolated behind a service interface (`app/services/meesho_scraper.py`) so we can swap in the official API later without touching the rest of the app.
