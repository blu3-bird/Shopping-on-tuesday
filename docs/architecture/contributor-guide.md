# Contributor Guide — Shopping on Tuesday

Welcome contributors! This project is a Flask-based Meesho dropshipping store. We use **Poetry** (not pip) and deploy on **Render** (free tier).

## How to contribute

1. **Fork** the repo
2. **Clone** your fork: `git clone https://github.com/<your-username>/Shopping-on-tuesday.git`
3. **Create a branch**: `git checkout -b feature/your-feature-name`
4. **Install Poetry** (if not installed): `curl -sSL https://install.python-poetry.org | python3 -`
5. **Install dependencies**: `poetry install`
6. **Copy env**: `cp .env.example .env` and fill in your values
7. **Set up DB**: Create a free PostgreSQL database (Neon/Supabase) and add `DATABASE_URL` to `.env`
8. **Run migrations**: `poetry run flask db upgrade`
9. **Run the app**: `poetry run python run.py`
10. **Test** your changes
11. **Commit** and **push**: `git push origin feature/your-feature-name`
12. **Open a Pull Request**

## Code style

- Follow PEP 8
- Write docstrings for functions and classes
- Keep functions small and focused
- Add tests where applicable
- Update documentation if you change behavior

## Issue labels

We use these labels to help new contributors find good first issues:

| Label | Meaning |
|-------|---------|
| `good first issue` | Beginner-friendly, well-scoped, no deep context needed |
| `help wanted` | Needs assistance, any skill level |
| `bug` | Something is broken |
| `enhancement` | New feature or improvement |
| `documentation` | Docs-only changes |
| `poetry` | Dependency/Poetry related |
| `frontend` | HTML/CSS/JS changes |
| `backend` | Python/Flask/SQLAlchemy changes |
| `scraping` | Meesho scraper related |

## First-good-issues

See `docs/plans/first-good-issues.md` for the current list of beginner-friendly issues ready for contributors.

## Pull request checklist

- [ ] Branch is up to date with `main`
- [ ] Code follows PEP 8
- [ ] Tests pass (if applicable)
- [ ] Documentation updated (if applicable)
- [ ] Linked to an issue (if applicable)

## Code of conduct

Be respectful, inclusive, and patient with newcomers. This is a learning project — everyone starts somewhere.
