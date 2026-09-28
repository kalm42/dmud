# dmud local foundation

The current application is a local startup shell. Campaign creation and saves arrive in later stories.

## Prerequisites

- Node.js 24.20.0 with npm
- Python 3.14.7
- uv 0.12.0
- SQLite 3.37.0 or newer, available to Python
- Playwright Chromium and WebKit for the browser checks

The initial architecture selected TypeScript 7.0.2. The pinned `typescript-eslint@8.69.0` declares TypeScript `<6.1`, so this story pins TypeScript 6.0.3 until that tool supports 7.x. The lockfile records the resolved dependency tree.
The `@hey-api/openapi-ts` dependency tree resolves a vulnerable `js-yaml` 4.3.1; an npm override pins patched 4.3.2 without changing the selected generator.

## Clean install

```sh
cd frontend && npm ci && npx playwright install chromium webkit
cd ../backend && uv sync --locked
```

## Develop

In separate terminals:

```sh
cd backend && PYTHONPATH=src uv run uvicorn dmud.main:app --host 127.0.0.1 --port 8000
cd frontend && npm run dev -- --host 127.0.0.1
```

Open `http://127.0.0.1:5173`. Vite proxies `/api` to the loopback backend. Optional `DMUD_LLM_API_KEY` is read and validated by the backend only; it is unused by the startup shell.

## Checks

Run each command independently:

```sh
cd frontend && npm run format:check
cd frontend && npm run lint
cd frontend && npm run typecheck
cd frontend && npm run build
cd frontend && npm test
cd backend && uv run ruff format --check src tests scripts
cd backend && uv run ruff check src tests scripts
cd backend && uv run pyright
cd backend && uv run pytest
python3 scripts/check_contract.py
cd frontend && npm run test:e2e
```

The GitHub Actions quality workflow runs these gates on pushes and pull requests, including contract regeneration and the real-browser journey.

## Verified on 2026-09-23

Node 24.20.0 and uv 0.12.0 were exercised through `npm exec --yes --package=node@24.20.0 -- npm ci` and `uvx --from uv==0.12.0 uv sync --locked`. Python 3.14.7 and SQLite 3.54.0 were installed locally. The host's default Node 24.13.0 and uv 0.8.11 are older than the documented prerequisites, so use the selected versions for routine development.

The clean installs passed. Frontend format, ESLint, strict TypeScript, build, Vitest (2 tests), backend Ruff format/lint, Pyright strict, pytest (3 tests), contract regeneration/drift, and Playwright (3 real-browser tests) passed. `npm audit` found 0 vulnerabilities after the YAML override. The browser checks cover an available API, an unavailable API, and canary exclusion from browser-visible output and storage.
