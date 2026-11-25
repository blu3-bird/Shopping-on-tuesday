# First-Good-Issues — Ready for Contributors

These are beginner-friendly issues scoped for new contributors. Each issue is small, self-contained, and labeled `good first issue`.

## Phase 1 — Poetry migration & stabilization

| # | Issue | Label | Estimated effort |
|---|-------|-------|------------------|
| 1 | Create `pyproject.toml` from `requirements.txt` + add `psycopg2-binary`, `beautifulsoup4`, `requests` | `good first issue`, `poetry`, `backend` | 30 min |
| 2 | Generate `poetry.lock` and verify `poetry install` works | `good first issue`, `poetry`, `backend` | 15 min |
| 3 | Create `.env.example` with `SECRET_KEY`, `DATABASE_URL`, `FLASK_CONFIG` | `good first issue`, `backend` | 10 min |
| 4 | Switch `config.py` from SQLite URI to PostgreSQL via `DATABASE_URL` env var | `good first issue`, `backend`, `database` | 20 min |
| 5 | Fix 404 error handler template name (`errors/400.html` → `errors/404.html`) | `good first issue`, `bug`, `backend` | 10 min |
| 6 | Fix typo `hightlights` → `highlights` in `admin/routes.py` | `good first issue`, `bug`, `backend` | 5 min |
| 7 | Fix `discount_percentage` validator max value (`DISCOUNT_MIN` → `DISCOUNT_MAX`) | `good first issue`, `bug`, `backend` | 10 min |
| 8 | Fix `original_price` placeholder type (integer → string) in `admin/forms.py` | `good first issue`, `bug`, `frontend` | 5 min |

## Phase 2 — Meesho scraping layer (upcoming)

| # | Issue | Label | Estimated effort |
|---|-------|-------|------------------|
| 9 | Create `app/services/meesho_scraper.py` with BeautifulSoup + requests | `good first issue`, `scraping`, `backend` | 1-2 hours |
| 10 | Add `source_url`, `meesho_price`, `markup_percentage`, `last_synced` to Product model | `good first issue`, `database`, `backend` | 30 min |
| 11 | Admin route to trigger Meesho product import | `good first issue`, `scraping`, `backend` | 1 hour |

## Phase 3+ — Cart, orders, payments (upcoming)

Cart model, checkout flow, payment integration, customer accounts, etc.

## How to claim an issue

1. Comment on the GitHub issue: "I'd like to work on this"
2. A maintainer will assign it to you
3. Create a branch: `git checkout -b feature/issue-<number>-short-description`
4. Implement, test, commit, push
5. Open a PR linking the issue

## Need help?

- Drop a comment on the issue
- Tag a maintainer
- Read `docs/architecture/contributor-guide.md` for setup instructions
