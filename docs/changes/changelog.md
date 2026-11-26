# Changelog

All notable changes to the codebase are recorded here. Format: `YYYY-MM-DD — description`.

## 2026-11-25
- Created docs directory structure (`plans/`, `changes/`, `approval/`, `progress/`, `architecture/`, `scraping/`, `deployment/`)
- Wrote `docs/plans/000-project-overview.md`
- Explored existing codebase: Flask app, models, routes, templates, requirements.txt
- **Phase 1 COMPLETED:**
  - Created `pyproject.toml` (Poetry, Python >=3.12,<3.14, package-mode=false)
  - Generated `poetry.lock` (46 dependencies resolved)
  - Deleted `requirements.txt` (pip removed)
  - Created `.env.example` (SECRET_KEY, DATABASE_URL, FLASK_CONFIG, INSTAGRAM_URL)
  - Added dependencies: `psycopg2-binary`, `beautifulsoup4`, `requests`
  - Dev dependencies: `pytest`, `pytest-flask`, `black`, `flake8`, `isort`
  - `config.py`: SQLALCHEMY_DATABASE_URI now uses `DATABASE_URL` env var (falls back to SQLite for local dev)
  - `app/__init__.py`: Fixed 404 error handler (`errors/400.html` → `errors/404.html`)
  - `admin/routes.py`: Fixed typo `hightlights` → `highlights`
  - `admin/forms.py`: Fixed `discount_percentage` validator max (`DISCOUNT_MIN` → `DISCOUNT_MAX`)
  - `admin/forms.py`: Fixed `original_price` placeholder (integer → string)
  - Verified: `poetry install` works, app starts, all pages load (200/302), DB tables created

## 2026-11-26
- **Phase 2 COMPLETED:** Meesho scraping layer
  - `app/models.py`: Added Meesho fields (`source_url`, `meesho_price`, `markup_percentage`, `last_synced`, `is_imported`) + `selling_price` property
  - `app/services/__init__.py`: New services package
  - `app/services/meesho_scraper.py`: `scrape_product()`, `scrape_category()`, `is_meesho_url()` using requests + BeautifulSoup4
  - `app/admin/routes.py`: Added `/admin/import-meesho` GET/POST route
  - `app/templates/admin/import_meesho.html`: Import form template
  - Recreated local SQLite DB with new columns
  - Verified: all pages load (200/302), import route works

## Planned (not yet done)
- Set up PostgreSQL database (Neon/Supabase free tier) for production
- Phase 3: Cart + orders
- Phase 4: Payments
- Phase 5: Free deployment on Render
