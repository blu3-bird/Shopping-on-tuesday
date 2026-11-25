# Phase 1: Poetry Migration + PostgreSQL + Codebase Stabilization

**Status:** Pending approval  
**Goal:** Convert from pip/`requirements.txt` to Poetry, switch from SQLite to PostgreSQL (latest Python 3.13), and stabilize the existing broken Flask codebase so it runs cleanly. No new features yet — just make what exists work.

---

## 1. Poetry migration

### What changes
- Delete `requirements.txt`
- Create `pyproject.toml` with all dependencies
- Create `poetry.lock` (via `poetry lock`)
- Create `.env.example` (template for environment variables)
- Update `run.py` and `wsgi.py` if needed for Poetry entrypoints

### Dependencies to port (from `requirements.txt`)
Flask, Flask-SQLAlchemy, Flask-Migrate, Flask-Login, Flask-WTF, python-dotenv, SQLAlchemy, alembic, gunicorn, pillow, email-validator, blinker, click, colorama, dnspython, idna, itsdangerous, Jinja2, Mako, MarkupSafe, packaging, greenlet, typing_extensions, Werkzeug, WTForms

### New dependencies to add
- `psycopg2-binary` — PostgreSQL driver for SQLAlchemy
- `beautifulsoup4` — Meesho scraping (Phase 2, but add now)
- `requests` — HTTP client for scraping (Phase 2, but add now)

### Verification
- `poetry install` succeeds
- `poetry run python run.py` starts the app on `http://127.0.0.1:5000`
- No import errors

---

## 2. PostgreSQL setup (replacing SQLite)

### What changes
- `config.py`: Change `SQLALCHEMY_DATABASE_URI` from SQLite to PostgreSQL using `DATABASE_URL` env var
- Add `DATABASE_URL` to `.env.example`
- Choose provider: **Neon** (free tier, serverless PostgreSQL) or **Supabase** (free tier)
- Create a free PostgreSQL database on the chosen provider
- Get the connection string

### Verification
- `db.create_all()` creates tables in PostgreSQL, not SQLite
- Alembic migrations work against PostgreSQL
- Existing `Product`, `ProductImage`, `Admin` models migrate cleanly

---

## 3. Codebase stabilization (fix what's broken)

Based on my code review, these are the known issues to fix:

### Templates / layout
- `base.html`: Logo image uses `uploads/logo.png` with `onerror` fallback — fine, but verify the uploads folder exists
- Footer hardcodes `Pardeep Singh` and `pardeep@example.com` — make configurable via config/env
- About modal and bug report modal — verify they render without JS errors

### Routes
- `app/__init__.py`: 404 handler renders `errors/400.html` (wrong template name — should be `404.html`)
- `app/__init__.py`: `instance_path` uses `app.root_path / '..' / 'instance'` — fragile path; verify it works
- `auth/routes.py`: `/arson` route creates admin accounts — verify `AdminCreateClass` form exists (it does, in `forms.py`)
- `admin/routes.py`: `edit_product` has typo `product.hightlights` (missing 'g') — should be `highlights`

### Models
- `models.py`: Looks solid. `Product.primary_image` and `get_image_url` reference `ProductImage` — verify relationship works

### Config
- `config.py`: `SECRET_KEY` is `os.environ.get('SECRET_KEY')` with no fallback in base Config — DevelopmentConfig sets a fallback, ProductionConfig raises error. Good pattern, keep it.
- `UPLOAD_FOLDER` uses `basedir/app/static/uploads` — verify directory creation works

### Forms
- `admin/forms.py`: `discount_percentage` validator has `max=DISCOUNT_MIN` (should be `DISCOUNT_MAX`) — bug
- `admin/forms.py`: `original_price` render_kw has `{'placeholder': 500}` (integer, should be string) — minor

### Entry points
- `run.py`: Runs on `127.0.0.1:5000` — fine for dev
- `wsgi.py`: Imports `create_app` — fine for production (gunicorn)

---

## 4. Deliverables for Phase 1

| File | Action |
|------|--------|
| `pyproject.toml` | Create (Poetry config + dependencies) |
| `poetry.lock` | Generate via `poetry lock` |
| `requirements.txt` | Delete |
| `.env.example` | Create (SECRET_KEY, DATABASE_URL, FLASK_CONFIG) |
| `config.py` | Switch SQLite URI → PostgreSQL via env var |
| `app/__init__.py` | Fix 404 error handler template name |
| `admin/routes.py` | Fix `hightlights` → `highlights` typo |
| `admin/forms.py` | Fix `discount_percentage` max validator + placeholder type |

---

## 5. How to verify Phase 1 is complete

1. `poetry install` → no errors
2. `poetry run python run.py` → app starts, no import errors
3. Visit `http://127.0.0.1:5000` → homepage loads
4. Visit `http://127.0.0.1:5000/products` → product list loads
5. Visit `http://127.0.0.1:5000/auth/login` → login page loads
6. Database tables exist in PostgreSQL (not a local `.db` file)
7. Alembic `flask db migrate` works against PostgreSQL

---

## Next phase (Phase 2): Meesho scraping layer

After Phase 1 is approved and built, Phase 2 will add:
- `app/services/meesho_scraper.py` — BeautifulSoup + requests scraper
- Admin route to trigger Meesho import
- Product `source_url`, `meesho_price`, `markup_percentage`, `last_synced` fields
- Sync scheduler (manual trigger to start)

---

## Approval needed

Reply "Approved" for Phase 1, and I'll start building:
1. `pyproject.toml` (Poetry)
2. PostgreSQL config
3. Bug fixes listed above

Nothing is built until you say so.
