# Django & DRF Learning Journey

A focused, 4-day intensive study sprint documenting my transition from Flask to Django and Django REST Framework — from first `startproject` command to a working multi-model CRUD API with authentication.

## Why This Repo Exists

I came into this with solid hands-on experience in **Flask**: REST APIs, JWT authentication, SQLAlchemy-style ORM thinking, WebSockets, and backend architecture in general. What I didn't have was real, hands-on experience with Django or DRF — and I needed that gap closed fast, before starting a production backend that required it.

This repo is the record of that sprint: not a tutorial copy-paste, but a working log of code I wrote, broke, debugged, and rebuilt from memory to confirm I actually understood it — not just recognized it.

## Why Learn Django (Instead of Just Staying in Flask)

Flask is a microframework — it gives you a router and lets you build everything else yourself. That's great for control, but it also means every new project starts by re-deciding: which ORM, which auth pattern, which project layout, which admin tooling (if any).

Django takes the opposite stance — "batteries included." A few concrete reasons this matters for real backend work:

- **A production-grade ORM with a built-in migration system.** Schema changes are tracked as versioned, reviewable Python files (`makemigrations` → `migrate`), not left to manual SQL or a bolted-on tool like Alembic.
- **An admin interface for free.** Register a model, and Django generates a full CRUD UI over it — genuinely useful for internal tooling, debugging, and giving non-technical teammates safe access to data, without writing a single view or template for it.
- **Django REST Framework** turns Django into a serious API backend: serializers, ViewSets, routers, authentication classes, and permissions that compose cleanly instead of being hand-rolled per endpoint.
- **Conventions that scale with a team.** The project/app split, the settings model, the URL-namespacing system — all of it exists so that a codebase stays navigable as it grows past what one person can hold in their head.

None of this makes Django "better than Flask" in the abstract — it makes it a different trade-off, and one that matches the shape of the production backend I was about to build.

## How This Repo Is Organized

| Day | Focus |
|-----|-------|
| **Day 1** | Django project/app structure, `settings.py`, `manage.py` vs `django-admin`, URL dispatching, `ROOT_URLCONF`, `include()` |
| **Day 2** | Django ORM — models, migrations, relationships, QuerySets, `select_related()` / `prefetch_related()`, the N+1 problem |
| **Day 3** | Django REST Framework — serializers, `APIView` vs `ViewSet`, routers, JWT authentication, permissions |
| **Day 4** | Retrieval build — a small multi-model CRUD API built from scratch, without copying from earlier code, to test what actually stuck |

Each day's folder contains the code written that day, plus notes on the specific points where a Flask-shaped mental model didn't transfer cleanly to Django — those mismatches were often more instructive than the parts that just worked.

## What This Repo Is Not

This isn't a Django course, a boilerplate template, or a production-ready starter kit. It's a personal learning artifact — code written under a tight timeline, meant to demonstrate real understanding rather than polished output.