# Phase 2: Meesho Scraping Layer

**Status:** Pending approval  
**Goal:** Build the Meesho product scraping service so products can be imported into the store. No API — scraping only.

---

## 1. Product model updates

Add Meesho-specific fields to the `Product` model:

| Field | Type | Purpose |
|-------|------|---------|
| `source_url` | String | Original Meesho product URL |
| `meesho_price` | Float | Price on Meesho (supplier price) |
| `markup_percentage` | Float | Your markup % (default 20) |
| `last_synced` | DateTime | When product was last synced from Meesho |
| `is_imported` | Boolean | Whether product was imported from Meesho |

Selling price = `meesho_price * (1 + markup_percentage / 100)`

## 2. Scraping service

Create `app/services/meesho_scraper.py`:

- `scrape_product(url)` — scrape a single Meesho product page
- `scrape_category(category_url, limit)` — scrape multiple products from a category
- Uses `requests` + `BeautifulSoup4` (lightweight, no browser)
- Respectful rate limiting (delay between requests)
- Returns structured product data (title, price, description, images, category)

## 3. Admin import route

Add admin route to trigger Meesho import:

- `POST /admin/import-meesho` — accept a Meesho URL, scrape, create product
- Admin reviews imported product before publishing (draft mode)
- Show Meesho price + calculated selling price with markup

## 4. Verification

- `poetry install` works with new `beautifulsoup4`, `requests` deps
- Admin can import a Meesho product URL
- Product appears in store with correct markup pricing
- `last_synced` timestamp updates on import

---

## Next phase (Phase 3): Cart + orders

After Phase 2, we'll add customer cart, order models, and checkout flow.

---

## Approval needed

Reply "Approved" for Phase 2, and I'll start building. Nothing is built until you say so.
