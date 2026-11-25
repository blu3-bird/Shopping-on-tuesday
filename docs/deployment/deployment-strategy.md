# Free Deployment Strategy

## Status
Not started — awaiting your host + domain choices.

## Constraints
- $0 budget — free tiers only
- Must support Python/Flask (WSGI)
- Must support SQLite or free PostgreSQL
- Must support environment variables (SECRET_KEY, etc.)
- Free domain or free subdomain

## Candidate free hosts (to evaluate)

| Host | Free tier limits | Notes |
|------|-----------------|-------|
| Render | 750 hours/month, spins down after inactivity | Popular for Flask, gives `yourapp.onrender.com` |
| Koyeb | Free tier with Nanos instances | Gives `yourapp.koyeb.app` |
| PythonAnywhere | Beginner account: 1 web app, MySQL only (no PostgreSQL on free) | `yourapp.pythonanywhere.com` |
| Fly.io | Small shared VM, 3 shared-cpu-1x VMs free | `yourapp.fly.dev`, needs credit card for verification |
| Railway | $5 trial credit, then paid | Not truly free long-term |

## Candidate free domains
- `yourapp.onrender.com` (comes with Render hosting)
- `yourapp.koyeb.app` (comes with Koyeb hosting)
- `yourapp.pythonanywhere.com` (comes with PythonAnywhere)
- freenom `.tk`, `.ml`, `.ga` (free but less reputable)
- GitHub Pages custom domain (static only — doesn't work for Flask backend)

## Recommendation (my pick, awaiting your approval)
**Render free tier** + `yourapp.onrender.com` subdomain. It's the simplest Flask hosting with a free subdomain and SSL included.

## Deployment artifacts needed
- `pyproject.toml` (Poetry)
- `Procfile` or `render.yaml` (start command: `gunicorn wsgi:app`)
- Environment variables (`SECRET_KEY`, `FLASK_CONFIG=production`)
- `requirements.txt` export from Poetry (some hosts still need it)
