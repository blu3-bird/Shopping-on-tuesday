# Project Overview — Shopping on Tuesday

## Goal
Rebuild the existing broken Flask e-commerce store into a working **Meesho dropshipping/reselling store**, deployed for free, with a free domain, managed with Poetry.

## Current state (as found)
- Flask app factory (`create_app`) with 3 blueprints: `main`, `auth`, `admin`
- Models: `Product`, `ProductImage`, `Admin` (SQLAlchemy + Alembic migrations)
- Admin-only auth (login/logout/create-admin), no customer accounts
- No cart, no checkout, no orders, no payments
- No Meesho integration at all
- `requirements.txt` (pip-style) — needs migration to Poetry
- Templates + static CSS/JS exist but layout is broken
- SQLite database, file-based image uploads

## What the final store needs (MVP → long-term)

### MVP (Phase 1)
- Working public product browse + detail pages
- Admin can add/edit/delete products
- Admin login
- Products can be imported from Meesho via scraping
- Customer can add to cart and place an order (order recorded, no payment yet)

### Long-term
- Customer registration/login
- Payment integration (Razorpay/Stripe/UPI — free tier where possible)
- Order fulfillment tracking (mark shipped/delivered)
- Markup/margin management (Meesho price → your selling price)
- Stock sync from Meesho
- Reviews, search, filters
- Free custom domain + SSL

## Constraints
- Python dev learning more Python — code should be readable and Pythonic
- Poetry, not pip
- Free hosting + free domain only
- Meesho scraping (no API) — must be robust to site changes, respectful of rate limits
- No big-bang rewrite — one phase at a time, each approved before building

## Decisions pending your approval
1. Free host choice (Render / Koyeb / PythonAnywhere / Fly.io free tier)
2. Free domain choice (onrender.com subdomain / freenom / GitHub Pages custom)
3. Scraping approach (BeautifulSoup + requests vs Selenium/Playwright for JS-heavy pages)
4. Whether to keep SQLite or move to PostgreSQL free tier
