# Vercel Deployment

This Django app is configured for Vercel with:

- `api/index.py` as the Python serverless entrypoint
- `vercel.json` to run migrations, seed the menu, collect static files, and route requests to Django
- Python dependencies are declared in `requirements.txt` and `pyproject.toml`; Vercel installs them automatically
- `DATABASE_URL` support for hosted Postgres, with local SQLite as the development fallback
- `.python-version` pinned to Python 3.12 for Vercel's Python runtime

## Environment variables

Set these in Vercel Project Settings or with the Vercel CLI:

```bash
vercel env add DJANGO_SECRET_KEY production preview
vercel env add DATABASE_URL production preview
```

Generate a Django secret key locally:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

Optional:

```bash
vercel env add DJANGO_ALLOWED_HOSTS production preview
vercel env add DJANGO_CSRF_TRUSTED_ORIGINS production preview
```

For the default Vercel domain, these can usually stay unset because `.vercel.app` is already allowed.

## Deploy

```bash
vercel
```

For production:

```bash
vercel --prod
```

Use a hosted Postgres database for real contact form/admin data. SQLite is fine locally, but serverless deployments do not provide durable local disk storage.
