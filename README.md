# Dynamic FastAPI Portfolio

This project upgrades the original Django/static portfolio into a FastAPI full-stack application with a database-driven public site and a protected Super User dashboard.

## What Is Included

- FastAPI application in `app/`
- SQLAlchemy models for users, profile information, skills, education, experience, projects, certificates, achievements, services, testimonials, social links, media files, contact messages, and activity logs
- Pydantic schemas in `app/schemas.py`
- JWT login, bcrypt password hashing, protected admin routes, and logout
- Admin dashboard with counts, search, pagination, sorting, quick actions, recent activity, and media uploads
- Dynamic Jinja2 portfolio templates
- Separated CSS in `static/css/style.css`
- Separated JavaScript in `static/js/app.js`
- Alembic setup and initial migration
- SQLite by default, PostgreSQL-ready through `DATABASE_URL`

## Installation

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
alembic upgrade head
uvicorn app.main:app --reload
```

Open:

- Public site: http://127.0.0.1:8000/
- Admin dashboard: http://127.0.0.1:8000/admin

Default development admin:

- Email: `admin@example.com`
- Password: `ChangeMe123!`

Change these immediately in `.env` before deployment.

## API Examples

Authenticate:

```bash
curl -X POST http://127.0.0.1:8000/api/login ^
  -H "Content-Type: application/json" ^
  -d "{\"email\":\"admin@example.com\",\"password\":\"ChangeMe123!\"}"
```

Use the returned bearer token for protected endpoints:

- `GET /api/projects`
- `POST /api/projects`
- `PUT /api/projects/{id}`
- `DELETE /api/projects/{id}`

Equivalent CRUD endpoints exist for:

- `/api/skills`
- `/api/education`
- `/api/experience`
- `/api/certificates`
- `/api/achievements`
- `/api/services`
- `/api/testimonials`
- `/api/social-links`

## Database

Development uses SQLite:

```env
DATABASE_URL="sqlite:///./portfolio.db"
```

PostgreSQL deployment only requires changing the URL:

```env
DATABASE_URL="postgresql+psycopg2://user:password@host:5432/portfolio"
```

Then run:

```bash
alembic upgrade head
```

## Deployment Guide

1. Set a strong `SECRET_KEY`.
2. Set `ADMIN_EMAIL` and `ADMIN_PASSWORD` for the first boot, then rotate the password.
3. Use PostgreSQL for production.
4. Serve uploaded files from durable storage or a mounted volume.
5. Run behind HTTPS.
6. Start with a production ASGI server command such as:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

7. Put Nginx, Caddy, or a platform router in front for TLS, compression, static caching, and upload limits.

## Folder Structure

```text
app/
  auth/
  database/
  routes/
  services/
  utils/
  main.py
  models.py
  schemas.py
alembic/
static/
  css/
  docs/
  js/
  uploads/
  videos/
templates/
  admin/
  base.html
  index.html
requirements.txt
.env.example
```
