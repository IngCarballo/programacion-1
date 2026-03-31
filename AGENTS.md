# AGENTS.md

## Scope
- This repository currently contains planning/instruction material for a 10-step course project, not a checked-in Django/React application.
- Most guidance below is inferred from `agent.md`, `tp1.md` through `tp10.md`, and the code snippets embedded in those documents.
- Use this file as the working contract for agentic contributors operating in this repo.

## Repository Reality Check
- There is no `package.json`, `requirements.txt`, `manage.py`, or app source tree committed at the repository root today.
- The documented target stack is Django + Django REST Framework for the backend and React + Bootstrap + React Router for the frontend.
- Treat commands in this file as the canonical commands the course material expects students to use once the scaffolded app exists.
- If you are asked to edit application code, first confirm whether the code exists in the repo or whether you are expected to generate new project files.

## External Agent Rules
- No `.cursorrules` file was found.
- No files were found under `.cursor/rules/`.
- No `.github/copilot-instructions.md` file was found.
- As a result, this `AGENTS.md` is the primary agent instruction source for the repository.

## Project Shape Expected By The TP Files
- Backend bootstrap: Django project created with `django-admin startproject config .` and app creation via `python manage.py startapp <app_name>`.
- Backend libraries repeatedly referenced: `django`, `djangorestframework`, `django-cors-headers`, `drf-spectacular`, `mysqlclient`, `pymysql`, `djangorestframework-simplejwt`.
- Frontend bootstrap: `npx create-react-app frontend` or equivalent CRA-style app creation.
- Frontend libraries repeatedly referenced: `bootstrap`, `react-router-dom`.
- API themes repeated across the docs: CRUD endpoints, authentication, CORS, Swagger/OpenAPI docs, protected routes, and full frontend/backend integration.

## Build / Setup Commands

### Backend Setup
- Create venv: `python -m venv venv`
- Activate venv on macOS/Linux: `source venv/bin/activate`
- Install base backend deps: `pip install django djangorestframework django-cors-headers drf-spectacular`
- Install MySQL support: `pip install mysqlclient pymysql`
- Install JWT auth support: `pip install djangorestframework-simplejwt`
- Freeze deps when the backend exists: `pip freeze > requirements.txt`
- Create project scaffold: `django-admin startproject config .`
- Create base app: `python manage.py startapp core`

### Backend Development Commands
- Create migrations: `python manage.py makemigrations`
- Apply migrations: `python manage.py migrate`
- Create admin user: `python manage.py createsuperuser`
- Run dev server: `python manage.py runserver`

### Frontend Setup
- Verify tooling: `node -v` and `npm -v`
- Create app: `npx create-react-app frontend`
- Install frontend deps: `npm install`
- Install UI/routing deps: `npm install bootstrap react-router-dom`

### Frontend Development Commands
- Run dev server: `npm start`

## Test Commands

### Backend Tests
- Run all Django tests: `python manage.py test`
- Run tests for one app: `python manage.py test <app_name>`
- Run one test module: `python manage.py test <app_name>.tests`
- Run one test class: `python manage.py test <app_name>.tests.<TestClass>`
- Run one test method: `python manage.py test <app_name>.tests.<TestClass>.<test_method>`
- The repo docs explicitly mention `python manage.py test`; the more specific forms are standard Django patterns and should be preferred for focused work.

### Frontend Tests
- No frontend test command is documented in the repo.
- If a Create React App frontend is generated, the usual single-run entry point is `npm test`.
- For a single Jest test file in a CRA app, prefer `npm test -- <filePattern>`.
- For a single named test, prefer `npm test -- --testNamePattern="<name>"`.
- Only document or run these once a real frontend exists in the repo.

## Lint / Format Commands
- No lint or formatter configuration is committed yet.
- Do not invent `ruff`, `black`, `flake8`, `eslint`, or `prettier` commands unless config files for them are later added.
- When the actual app is created, inspect committed config before adding lint commands here.

## Documentation / Verification Commands
- Backend Swagger UI target from the TP docs: `http://127.0.0.1:8000/api/docs/`
- Backend schema endpoint target: `http://127.0.0.1:8000/api/schema/`
- Backend admin target: `http://127.0.0.1:8000/admin/`
- Frontend dev target: `http://localhost:3000`

## Code Style Guidelines

### General Principles
- Follow the repository's teaching-oriented style: explicit, readable, stepwise, and friendly to students.
- Prefer clear structure over clever abstractions.
- Keep changes aligned with the current TP stage instead of implementing future stages early.
- Preserve Spanish-language instructional tone when editing TP documents unless the user asks for another language.
- Keep examples practical and runnable.

### Imports
- Group imports by standard library, third-party, and local imports.
- Prefer explicit imports over wildcard imports, even though `tp2.md` shows `from .serializer import *` and `from .models import *` in an example.
- In Django, import only the DRF classes actually used, such as `APIView`, `ModelViewSet`, `Response`, and `IsAuthenticated`.
- In React, keep framework imports, router imports, and local component/context imports clearly separated.

### Formatting
- Use consistent 4-space indentation in Python.
- Keep Django setting blocks and URL lists vertically aligned and easy to scan.
- Use one class per logical responsibility when possible.
- Favor short, readable functions over large multi-purpose blocks.
- In Markdown, prefer clear headings, ordered steps, fenced code blocks, and concise bullet lists.

### Types And Data Shape Discipline
- No typing standard is documented yet, but new Python code should use type hints when they improve clarity.
- Keep serializer fields, request payloads, and response shapes explicit.
- When documenting APIs, show representative JSON examples for request and response bodies.
- In React, keep auth/session state shape consistent across context, hooks, and route guards.

### Naming Conventions
- Use descriptive English identifiers in code, matching the framework conventions shown in the docs.
- Use `PascalCase` for Django/React classes and React components, for example `CustomUser`, `ProtectedView`, `AuthContext`, `ProtectedRoute`.
- Use `snake_case` for Python variables, functions, modules, and test methods.
- Use `camelCase` for JavaScript variables and functions if a frontend is added.
- Use clear route names like `token_obtain_pair`, `token_refresh`, `protected`, and app names that reflect the domain.
- Use branch names in the style already suggested by the repo, such as `feature/auth-system` or `feature/bootstrap-views`.

### Django Backend Conventions
- Register third-party apps explicitly in `INSTALLED_APPS`.
- Keep auth customization centralized through `AUTH_USER_MODEL` if a custom user model is introduced.
- Put CORS configuration in `settings.py` and keep local origins explicit.
- Prefer DRF serializers and viewsets/APIViews over ad hoc JSON handling.
- Add Swagger/OpenAPI wiring through `drf-spectacular` when the backend reaches the documentation stage.
- Keep URLs predictable under `/api/...` prefixes.

### React Frontend Conventions
- Organize screens under `views/` or `pages/` as suggested in `tp8.md`.
- Use an auth context for session state rather than duplicating login state across components.
- Protect private routes through a dedicated `ProtectedRoute` abstraction.
- Favor responsive Bootstrap layout primitives instead of ad hoc CSS when following the TP instructions.
- Keep login, register, logout, and home flows separate and easy to trace.

### Error Handling
- Fail loudly and clearly for invalid credentials, missing permissions, and invalid request payloads.
- Return framework-appropriate HTTP status codes instead of hiding backend failures.
- In frontend code, surface actionable messages to the user for login, registration, and API failures.
- Do not swallow exceptions just to keep UI flows moving.
- For docs, explain why an error might happen and how to verify the fix.

### Security And Config
- Never commit `.env` files; this is explicitly called out in `agent.md` and `tp10.md`.
- Keep secrets, DB credentials, and tokens out of Markdown examples unless they are obvious placeholders.
- Use environment variables for deploy-time configuration when the actual app exists.
- Be careful with MySQL examples in the docs; avoid turning sample credentials into committed real values.

### Testing Expectations
- Add or update tests when changing backend behavior.
- Prefer targeted test runs during iteration and a full `python manage.py test` before final handoff.
- For frontend work, add tests only once a real test harness exists in the committed app.
- When no executable project exists, validate changes by keeping docs internally consistent and runnable in principle.

### Git And Documentation Hygiene
- Keep `README.md` updated as the docs repeatedly request.
- Make small, descriptive commits.
- Prefer feature branches for scoped work.
- Do not commit generated virtual environments.
- Add `.gitignore` before introducing generated or local-only files.

## Agent Workflow Recommendations
- First inspect whether the requested change belongs to the current repository state or to the projected Django/React app described by the TP files.
- If the repo still only contains TP documents, prefer editing guidance/documentation over inventing missing source trees unless the user explicitly asks for scaffolding.
- When adding commands or conventions, derive them from existing docs first and only then fill gaps with standard framework defaults.
- Call out clearly when a command is documented in the repo versus inferred from Django/CRA conventions.
