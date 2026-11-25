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

## Planned (not yet done)
- Set up PostgreSQL database (Neon/Supabase free tier) for production
- Phase 2: Meesho scraping layer
- Phase 3: Cart + orders
- Phase 4: Payments
- Phase 5: Free deployment on Render
