# Documentation — Shopping on Tuesday (Meesho Dropshipping Store)

This folder holds all planning, design, approval, change, and progress records for the project rebuild. Nothing in the codebase is touched without a corresponding entry here first.

## Folder structure

| Folder | Purpose |
|--------|---------|
| `plans/` | Detailed implementation plans, one file per phase/feature |
| `changes/` | Changelog of every codebase change, what was fixed/updated and why |
| `approval/` | Design doc approvals — sign-off required before building anything |
| `progress/` | Running progress log, what's done, what's blocked, what's next |
| `architecture/` | Architecture decisions (DB schema, scraping layer, hosting, etc.) |
| `scraping/` | Meesho scraping strategy, selectors, rate limits, robustness notes |
| `deployment/` | Free hosting + free domain strategy and deployment steps |

## How we work

1. **Discuss** → agree on approach
2. **Design doc** → written in `plans/` or `architecture/`
3. **Approval** → recorded in `approval/` before any code is written
4. **Build** → code changes tracked in `changes/`
5. **Progress** → updated in `progress/` after every session

## Ground rules

- No pip — we use **Poetry** for dependency management.
- No paid services — **free tier only** for hosting and domain.
- Meesho has no usable public API → **scraping-first**, designed to swap in an API later.
- Don't fix everything at once — one phase at a time.
