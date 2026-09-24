---
baseline_commit: f5b0e37f768bd97fc7f526d3ed47bed367f39e3e
---

# Story 1.1: Run the Local dmud Application Foundation

Status: done

## Story

As a player,
I want to start the local application with a validated foundation,
so that I can begin a campaign on a stable local system.

## Acceptance Criteria

1. **Given** the documented Node, Python, uv, and SQLite prerequisites are available, **when** dependencies are installed from committed lockfiles, **then** the create-vite 9.2.0 React/TypeScript starter and uv-managed FastAPI backend initialized from scratch build successfully, and dependency availability has been revalidated against Architecture 1.2's selected versions.
2. **Given** the development environment is started, **when** the player opens the frontend, **then** the browser receives a working application shell, and frontend `/api` requests are proxied to loopback FastAPI without development CORS configuration.
3. **Given** backend configuration includes an LLM credential or other secret, **when** frontend output, logs, authored content, generated API client, and browser storage are inspected, **then** the secret is absent, and configuration is constructed and validated only at the backend composition root.
4. **Given** the initial repository structure, **when** dependencies and directories are reviewed, **then** it follows the feature-oriented monorepo and inward dependency direction, without speculative P1–P9 modules, distributed infrastructure, audio pipeline, or unused asset directories.
5. **Given** the runnable shell is checked in, **when** its baseline checks run, **then** formatting, linting, strict type checking, and an isolated real-browser startup journey pass through the real local frontend/backend boundary.

## Tasks / Subtasks

- [x] Establish the two pinned applications and documented prerequisites (AC: 1, 4)
  - [x] Use Architecture 1.2's exact create-vite React/TypeScript command for `frontend/` and `uv init --app backend` for `backend/`; add the specified direct runtime and quality-tool versions, then commit `frontend/package-lock.json` and `backend/uv.lock`.
  - [x] Verify every selected package/version resolves and the installed Node, Python, uv, and SQLite meet project constraints. Record any necessary pin correction and reason; do not silently float to `latest`. Reject SQLite older than 3.37.0 at backend startup before opening application data.
  - [x] Document clean install and separate development start/check commands in a short root README. Keep generated/build/runtime files and secrets out of source control.
- [x] Build a small vertical startup path (AC: 2, 3, 4)
  - [x] Add a FastAPI application factory/composition root, backend-only validated settings, and one typed read-only `/api` status resource with an explicit response model. This route proves the boundary; it has no game-state mutation or provider call.
  - [x] Configure Vite `/api` proxy to the loopback backend. Render a semantic, keyboard-readable React application shell that displays the API's validated status. Provide a clear unavailable/error state if the backend is down; do not claim a campaign or save exists.
  - [x] Export FastAPI OpenAPI 3.1 to `contracts/openapi.json`; generate and commit native fetch client, TypeScript types, Zod schemas, and TanStack Query bindings under `frontend/src/api/generated/`. Use that generated boundary in the shell and make regeneration/drift detectable. Never hand edit generated output.
  - [x] Load any optional provider secret only in backend settings, never from a `VITE_` environment variable or frontend config. Use a canary value in tests and inspect browser-visible assets/responses/storage plus ordinary logs for leakage.
- [x] Add the smallest meaningful quality gates (AC: 1, 2, 3, 5)
  - [x] Run frontend formatting/linting, `tsc --noEmit` in strict mode, and build; run backend Ruff format/lint, Pyright strict, and pytest. Keep these as separate failing commands.
  - [x] Add a backend integration test through the real FastAPI ASGI app, including the SQLite minimum-version guard where it can be injected without global state. Add a real Playwright browser journey that starts Vite and FastAPI, sees the shell and API result, and verifies the proxy without route mocks. Use isolated test storage if startup opens SQLite.
  - [x] Regenerate the OpenAPI/client artifacts in the check path and fail on drift. Run the checks from a clean install, document actual commands/results, and verify secret-canary absence.

### Review Findings

- [x] [Review][Patch] Keep the credential canary outside Vite's served root and test that it is not browser-readable (High; AC 3) [`frontend/playwright.config.cjs`:9, `tests/e2e/app.spec.ts`:31]
- [x] [Review][Patch] Restrict the development API proxy override to a loopback target (Medium; AC 2) [`frontend/vite.config.ts`:9]
- [x] [Review][Patch] Report malformed API responses separately from a disconnected backend (Low; AC 2) [`frontend/src/app/App.tsx`:19]
- [x] [Review][Patch] Enforce contract regeneration and drift checks in CI (Medium; AC 5 and project context) [`.github/workflows/quality.yml`:51]
- [x] [Review][Patch] Classify invalid JSON as an unexpected API response (Low; AC 2) [`frontend/src/app/App.tsx`:22]
- [x] [Review][Patch] Forward the query abort signal to the status request (Low) [`frontend/src/api/useStatus.ts`:11]

## Dev Notes

### Scope and handoffs

- This story owns only the runnable development shell and baseline contract/checks. Story 1.2 owns New Game/Continue and Title states; 1.3 owns durable operations; 1.4 owns P0 authored-content validation; 1.35 owns packaged FastAPI SPA serving and the full P0 production gate. A status resource is an implementation seam for AC 2, not a gameplay endpoint. Do not prebuild those later systems. [Source: `_bmad-output/planning-artifacts/epics.md`, Overview; Stories 1.1–1.4, 1.35]
- The repository currently contains planning/tooling artifacts and no `frontend/`, `backend/`, `content/`, or `contracts/` application tree. There are no existing application files to update or prior story lessons. Preserve existing planning files and the unrelated untracked UX `.DS_Store`. [Source: repository inspection, 2026-09-23]
- No LLM provider is selected. An optional settings field may validate a secret without contacting a provider; missing credentials must not prevent this local shell from starting. Do not create a provider SDK integration or expose configuration in the status resource. [Source: `_bmad-output/game-architecture.md`, Runtime, Deployment, and Security; `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`, Foundation]

### Architecture and structure

- Use React only for presentation and FastAPI as the future authority. `frontend/src/app/` owns shell composition; `frontend/src/api/` owns generated client use; `backend/src/dmud/main.py` and a composition root own app construction; `backend/src/dmud/platform/` may own concrete settings/runtime checks. Introduce feature directories only when the feature exists. `tests/e2e/` owns the browser journey and `backend/tests/integration/` the API test. [Source: `_bmad-output/game-architecture.md`, Project Initialization, Project Structure, System Location Mapping]
- Keep domain/application code free of FastAPI, SQLite, environment access, provider SDKs, and frontend imports. Construct validated dependencies at the composition root and pass them explicitly. Separate query/read and command/write code; this story needs no write path. Use one named application function/component per source file where practical, with precise types and purpose/example documentation for exported or nontrivial functions. [Source: `_bmad-output/project-context.md`, Code Organization Rules; `/Users/kyle/.codex/standards/code-architecture.md`, Functions and Files]
- Use a typed Pydantic response for `/api`, camelCase JSON, strict schema validation, and generated Zod parsing of the browser response. Do not add handwritten transport types or raw `fetch` in the feature. TanStack Query owns the server-derived status. Unknown external data stays unknown until validation. [Source: `_bmad-output/game-architecture.md`, API Contract and Frontend State; `_bmad-output/project-context.md`, Critical Implementation Rules]
- Keep frontend/backend development servers separate, with Vite proxying `/api` to FastAPI bound on loopback. Do not add permissive CORS to make the development flow work. Packaged one-process serving belongs to 1.35. [Source: `_bmad-output/game-architecture.md`, Runtime, Deployment, and Security; `_bmad-output/planning-artifacts/epics.md`, Story 1.1 and 1.35]
- The shell should have semantic landmarks and headings, accessible status/error text, visible focus for any control, relative text sizing, and usable narrow/zoom layout. It need not implement the full Title or notebook visual system yet, but should use the approved paper/ink/forest direction if styled. [Source: `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md`, Accessibility Floor; `DESIGN.md`, colors/typography]

### Dependency and verification notes

- Architecture 1.2 pins Node 24.20.0, create-vite 9.2.0, React/React DOM 19.2.8, TypeScript 7.0.2, Vite 8.2.2, React plugin 6.1.1, Python 3.14.7, uv 0.12.0, FastAPI 0.141.1, Pydantic 2.13.5, Pydantic Settings 2.15.0, PyYAML 6.0.3, `@hey-api/openapi-ts` 0.99.0, Zod 4.5.4, TanStack Query 5.102.8, Playwright 1.63.0, Vitest 5.0.0, ESLint 10.9.1, Pyright 1.1.411, Ruff 0.16.6, and pytest 9.1.1. Use the Architecture initialization commands for the remaining direct test dependencies. These are selected project pins, not an instruction to upgrade automatically. [Source: `_bmad-output/game-architecture.md`, Selected Application Stack and Project Initialization]
- Registry checks on 2026-09-23 confirm the selected Vite 8.2.2 exists, while Vite 8.3.0 and create-vite 9.2.1 are also listed; PyPI lists FastAPI 0.141.1. This does not establish full transitive compatibility. Resolve the exact project pins during scaffolding, verify Node engine/Python constraints, and record any incompatibility before changing a pin. [Sources: [npm Vite versions](https://www.npmjs.com/package/vite?activeTab=versions), [npm create-vite versions](https://www.npmjs.com/package/create-vite?activeTab=versions), [FastAPI on PyPI](https://pypi.org/project/fastapi/)]
- Prefer a real SPA-to-API Playwright assertion and real ASGI test over mocks. Cover API-up and API-unavailable shell behavior, status shape/runtime validation, and the canary-secret exclusion through observable output. Verify formatting, linting, typing, tests, and contract drift as independent gates. Do not claim the stage-wide accessibility/performance/endurance evidence from this startup check; the P0 Verification and Exit Plan owns that gate. [Source: `_bmad-output/project-context.md`, Testing Rules; `_bmad-output/planning-artifacts/p0-verification-and-exit-plan.md`]

### Project Context Rules

- Follow `_bmad-output/project-context.md` and the shared code-architecture standard for strict typing, vertical slices, one concern per source file, dependency injection, boundary validation, and integration-first tests. Python names are `snake_case`, React components `PascalCase`, feature directories `kebab-case`; generated files are committed but never edited manually.
- Keep credentials, databases, saves, logs, provider responses, build output, and browser-test artifacts outside source control. Avoid WebSockets, Redis, Celery, external brokers, auth, remote hosting, audio, and conditional P1–P9 systems. No MCP service is required by this story; Playwright and quality tools are repository dependencies. [Source: `_bmad-output/project-context.md`, Platform & Build Rules; `_bmad-output/game-architecture.md`, MCP Decision]

### References

- `_bmad-output/planning-artifacts/epics.md` — Epic 1; Story 1.1; Additional Requirements; NFR1, NFR12–NFR16.
- `_bmad-output/game-architecture.md` — Engine & Framework; API Contract and Frontend State; Project Structure; Runtime, Deployment, and Security.
- `_bmad-output/project-context.md` — Technology Stack & Versions; Code Organization Rules; Testing Rules; Platform & Build Rules.
- `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/EXPERIENCE.md` — Foundation; Accessibility Floor.
- `_bmad-output/planning-artifacts/ux-designs/ux-dmud-2026-09-08/DESIGN.md` — color and typography tokens.
- `_bmad-output/planning-artifacts/p0-verification-and-exit-plan.md` — later P0 stage gate.

## Dev Agent Record

### Agent Model Used

Codex GPT-6.

### Implementation Plan

- Scaffold the exact specified Vite and uv applications, pin and lock dependencies, and establish a read-only backend readiness boundary.
- Export OpenAPI from FastAPI, generate the browser boundary, validate unknown response data with generated Zod, and render readiness with TanStack Query.
- Exercise the real ASGI app and browser proxy, then run independent format, lint, type, build, test, contract drift, and canary gates.

### Debug Log References

- Red phase: backend integration tests initially failed because `dmud` did not exist.
- Architecture TypeScript 7.0.2 conflicted with `typescript-eslint@8.69.0` (`<6.1` peer range); pinned TypeScript 6.0.3 instead.
- Strict E2E type checking initially changed Playwright's config loading; a CommonJS Playwright config and separate strict E2E TypeScript config resolved it.

### Completion Notes List

- Ultimate context engine analysis completed - comprehensive developer guide created.
- Created the frontend/backend lockfiles, version pins, root setup instructions, and source-control exclusions. Selected Node 24.20.0 and uv 0.12.0 were exercised with `npm exec` and `uvx`; host defaults are older and are documented in README.
- FastAPI validates settings and SQLite before application data use and exposes only typed, read-only `/api/status`. Vite proxies `/api` to loopback; the semantic shell shows validated readiness or a backend-unavailable alert.
- Generated OpenAPI 3.1, fetch SDK, types, Zod, and TanStack Query bindings; contract regeneration detects drift. A patched `js-yaml` 4.3.2 override keeps the pinned generator and leaves `npm audit` at zero findings.
- Clean `npm ci` and `uv sync --locked` passed. Frontend format, lint, strict typecheck, build, and 2 Vitest tests passed; backend Ruff format/lint, strict Pyright, and 3 pytest integration tests passed; 3 real Playwright journeys passed; contract drift and canary inspections passed. Pytest emits an upstream Starlette TestClient deprecation warning.

### File List

- `.github/workflows/quality.yml`
- `.gitignore`
- `README.md`
- `_bmad-output/implementation-artifacts/1-1-run-the-local-dmud-application-foundation.md`
- `_bmad-output/implementation-artifacts/sprint-status.yaml`
- `backend/.python-version`
- `backend/pyproject.toml`
- `backend/scripts/export_openapi.py`
- `backend/src/dmud/__init__.py`
- `backend/src/dmud/get_status.py`
- `backend/src/dmud/main.py`
- `backend/src/dmud/platform/__init__.py`
- `backend/src/dmud/platform/require_sqlite.py`
- `backend/src/dmud/platform/settings.py`
- `backend/src/dmud/status.py`
- `backend/tests/integration/test_status.py`
- `backend/uv.lock`
- `contracts/openapi.json`
- `frontend/.gitignore`
- `frontend/.node-version`
- `frontend/.prettierignore`
- `frontend/eslint.config.js`
- `frontend/index.html`
- `frontend/openapi-ts.config.ts`
- `frontend/package-lock.json`
- `frontend/package.json`
- `frontend/playwright.config.cjs`
- `frontend/src/api/generated/@tanstack/react-query.gen.ts`
- `frontend/src/api/generated/client.gen.ts`
- `frontend/src/api/generated/client/client.gen.ts`
- `frontend/src/api/generated/client/index.ts`
- `frontend/src/api/generated/client/types.gen.ts`
- `frontend/src/api/generated/client/utils.gen.ts`
- `frontend/src/api/generated/core/auth.gen.ts`
- `frontend/src/api/generated/core/bodySerializer.gen.ts`
- `frontend/src/api/generated/core/params.gen.ts`
- `frontend/src/api/generated/core/pathSerializer.gen.ts`
- `frontend/src/api/generated/core/queryKeySerializer.gen.ts`
- `frontend/src/api/generated/core/serverSentEvents.gen.ts`
- `frontend/src/api/generated/core/types.gen.ts`
- `frontend/src/api/generated/core/utils.gen.ts`
- `frontend/src/api/generated/index.ts`
- `frontend/src/api/generated/sdk.gen.ts`
- `frontend/src/api/generated/types.gen.ts`
- `frontend/src/api/generated/zod.gen.ts`
- `frontend/src/api/parseStatus.test.ts`
- `frontend/src/api/parseStatus.ts`
- `frontend/src/api/useStatus.ts`
- `frontend/src/app/App.tsx`
- `frontend/src/app/app.css`
- `frontend/src/main.tsx`
- `frontend/tsconfig.app.json`
- `frontend/tsconfig.e2e.json`
- `frontend/tsconfig.json`
- `frontend/tsconfig.node.json`
- `frontend/vite.config.ts`
- `scripts/check_contract.py`
- `tests/e2e/app.spec.ts`

### Change Log

- 2026-09-23: Built the locked local frontend/backend foundation, generated API boundary, startup shell, and independent verification gates; moved story to review.
- 2026-09-23: Resolved all three code-review findings, repaired the frontend lint gate, reran frontend checks and three real-browser journeys; moved story to done.
- 2026-09-23: Applied follow-up review patches for CI contract drift enforcement, malformed JSON messaging, and request cancellation; verified all local quality gates.
