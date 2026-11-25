# Architecture Decisions

Decisions are recorded here as they are made. Each entry includes the decision, the alternatives considered, and the rationale.

## Decided

| Decision | Choice | Alternatives considered | Rationale |
|----------|--------|------------------------|-----------|
| Dependency manager | **Poetry** | pip | User requirement; better lockfile reproducibility |
| Web framework | **Flask** | FastAPI, Django | Existing codebase; user is learning Python via Flask |
| Meesho integration | **Scraping-first** | Meesho API (none available) | No public API; BeautifulSoup + requests to start, swappable to API later |
| Scraping tool | **BeautifulSoup + requests** | Selenium, Playwright | Lightweight, no browser needed; switch to Playwright only if pages are JS-heavy |
| Free host | **Render** (free tier) | Koyeb, PythonAnywhere, Fly.io | Simplest Flask hosting, free subdomain + SSL, easy to switch later |
| Free domain | **onrender.com subdomain** | freenom, custom domain | Comes with Render, no renewal games, free forever |
| Database | **PostgreSQL** (free tier) | SQLite | User wants proper storage for future analysis; SQLite doesn't scale for analytics |
| PostgreSQL provider | **Neon** or **Supabase** (free tier) | Render managed PG, ElephantSQL | Generous free tiers, serverless, easy Flask/SQLAlchemy integration |
| Python version | **Latest (3.13)** | 3.10, 3.11, 3.12 | User wants latest Python to learn modern features |

## Design principles
- Scraping layer isolated behind a service interface → swappable to API later
- No pip anywhere — Poetry only
- Free tier only, $0 budget
- One phase at a time, each approved before building
