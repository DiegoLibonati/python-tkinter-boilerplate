# Python Tkinter Boilerplate

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Description

**Python Tkinter Boilerplate** is a starting point for building desktop applications with a graphical interface using Python and Tkinter.

**The problem it solves**: avoid repeating the same setup and architecture decisions every time a new desktop project is started. Instead of configuring linting, testing, logging, and project structure from scratch each time, this template has all of that already in place.

**What it includes**:

- Ruff for linting and formatting
- pre-commit hooks for enforcing code quality before every commit
- Pydantic v2 for data validation and modeling
- Logging configured per environment (development, production, testing)
- A hierarchy of custom exceptions with centralized error handling
- pytest configured with coverage, env variables, and parallel execution

**How to use it**: clone the repository, rename the package and its references to match your project, and replace the template logic (users, auth, sample views) with your own application logic.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

All dependencies are declared in `pyproject.toml`. The `requirements*.txt` files are thin wrappers that delegate to it.

#### Runtime (`[project.dependencies]`)

```
pydantic==2.11.9
python-dotenv==1.2.2
```

#### Dev (`[project.optional-dependencies]` dev)

```
pre-commit==4.3.0
pip-audit==2.7.3
ruff==0.11.12
mypy==1.13.0
```

#### Test (`[project.optional-dependencies]` test)

```
pytest==9.0.3
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Build (`[project.optional-dependencies]` build)

```
pyinstaller==6.16.0
```

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Copy the development environment template:
   - Windows: `copy .env.example.dev .env`
   - Linux/Mac: `cp .env.example.dev .env`
6. Execute: `pip install -e ".[dev,test]"` (installs runtime, dev and test deps via pyproject.toml)
7. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

NOTE: Install **pre-commit** inside the repository folder.

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Env Keys

The application reads its configuration from environment variables. Here is a reference of all the keys it expects.

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.
2. `ENV_NAME`: A custom environment variable for template demonstration purposes.

```
ENVIRONMENT=development
ENV_NAME=template_value
```

## Project Structure

```
python-tkinter-boilerplate/
├── src/
│   ├── configs/
│   │   ├── __init__.py
│   │   ├── default_config.py
│   │   ├── development_config.py
│   │   ├── production_config.py
│   │   ├── testing_config.py
│   │   └── logger_config.py
│   ├── data_access/
│   │   ├── __init__.py
│   │   └── user_dao.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── user_model.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── auth_service.py
│   │   └── hash_service.py
│   ├── constants/
│   │   ├── __init__.py
│   │   └── messages.py
│   ├── ui/
│   │   ├── __init__.py
│   │   ├── interface_app.py
│   │   ├── styles.py
│   │   ├── components/
│   │   │   ├── __init__.py
│   │   │   └── labeled_entry.py
│   │   └── views/
│   │       ├── __init__.py
│   │       ├── login_view.py
│   │       ├── register_view.py
│   │       └── main_view.py
│   ├── utils/
│   │   ├── dialogs.py
│   │   ├── tkinter_exception_hook.py
│   │   ├── exceptions_decorator.py
│   │   └── __init__.py
│   ├── assets/
│   │   └── images/
│   ├── __init__.py
│   └── __main__.py
├── tests/
│   ├── test_configs/
│   │   ├── __init__.py
│   │   ├── test_development_config.py
│   │   ├── test_logger_config.py
│   │   ├── test_production_config.py
│   │   ├── test_testing_config.py
│   │   └── test_default_config.py
│   ├── test_constants/
│   │   ├── __init__.py
│   │   └── test_messages.py
│   ├── test_data_access/
│   │   ├── __init__.py
│   │   └── test_user_dao.py
│   ├── test_models/
│   │   ├── __init__.py
│   │   └── test_user_model.py
│   ├── test_services/
│   │   ├── __init__.py
│   │   ├── test_auth_service.py
│   │   └── test_hash_service.py
│   ├── test_ui/
│   │   ├── __init__.py
│   │   └── test_interface_app.py
│   ├── __init__.py
│   └── conftest.py
├── app.py
├── pyproject.toml
├── requirements.txt
├── requirements.dev.txt
├── requirements.test.txt
├── requirements.build.txt
├── app.spec
├── build.bat
├── build.sh
├── .env
├── .env.example.dev
├── .env.example.prod
├── .gitignore
├── .pre-commit-config.yaml
├── .python-version
├── CHANGELOG.md
├── LICENSE
└── README.md
```

1. `src` -> Root directory of the source code. Contains the full application logic following a **layered architecture** pattern.
2. `configs` -> Contains all **configuration classes** organized by environment (development, production, testing). Includes logging setup and application settings.
3. `data_access` -> Implements the **Repository/DAO pattern**. Abstracts all data operations, making it easy to switch from in-memory storage to a real database without affecting other layers.
4. `models` -> Defines **Pydantic models** for data validation and serialization.
5. `services` -> Contains **business logic and rules**. Validates data, enforces constraints, and orchestrates operations between UI and data access layer.
6. `constants` -> Holds **static values** like error codes and user messages.
7. `ui` -> Contains the **graphical interface** logic, organized into views, components, and styles.
8. `ui/views` -> Individual **screen/window classes** (login, register, main). Each view is a self-contained Tkinter Frame or Toplevel.
9. `ui/components` -> **Reusable UI widgets** shared across multiple views (e.g., labeled entry fields).
10. `ui/styles.py` -> Centralized **visual theme** configuration (colors, fonts, spacing).
11. `ui/interface_app.py` -> The **main application orchestrator**. Manages navigation between views and coordinates user actions with services.
12. `utils` -> Contains **shared utilities**: `tkinter_exception_hook.py` handles unhandled Tkinter exceptions (the `root.report_callback_exception` hook); `exceptions_decorator.py` is a method decorator that converts Pydantic `ValidationError` into dialog errors.
13. `assets` -> Static files such as **images and icons** used by the application.
14. `tests` -> Contains **tests** organized to mirror the `src/` structure.
15. `conftest.py` -> Defines **pytest fixtures** for application setup and tests data.
16. `app.py` -> The **application entry point**. Creates the Tkinter root window and initializes the application.
17. `pyproject.toml` -> **Unified project configuration** for pytest, ruff, and project metadata.
18. `requirements.txt` -> Thin wrapper: installs the package in editable mode (`-e .`). Actual deps are in `pyproject.toml`.
19. `requirements.dev.txt` -> Thin wrapper: installs dev extras (`-e .[dev]`).
20. `requirements.test.txt` -> Thin wrapper: installs test extras (`-e .[test]`).
21. `requirements.build.txt` -> Thin wrapper: installs build extras (`-e .[build]`).
22. `app.spec` -> **PyInstaller configuration** for generating standalone executables.
23. `.python-version` -> Pins the Python version (`3.11`) for tools like **pyenv**. If you use pyenv, it will automatically switch to the correct version when entering the project directory.

## Architecture & Design Patterns

The structure above reflects a deliberate architectural design. Here are the patterns that govern how the layers interact.

### Layered Architecture

This project follows a **Layered Architecture** pattern, organizing code into distinct levels with clear responsibilities. Each layer only communicates with the layer directly below it.

```
┌─────────────────────────────────────────────────────────────┐
│                    PRESENTATION LAYER                       │
│                   (UI Views & Components)                   │
│          Handles user interactions and display              │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   ORCHESTRATION LAYER                       │
│                     (InterfaceApp)                          │
│        Coordinates views with business logic                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                      BUSINESS LAYER                         │
│                        (Services)                           │
│          Contains business logic and validations            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     DATA ACCESS LAYER                       │
│                       (Repository)                          │
│              Abstracts data operations                      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       DATA STORAGE                          │
│                  (In-Memory / Database)                     │
└─────────────────────────────────────────────────────────────┘
```

#### Benefits

- **Separation of Concerns**: Each layer has a single responsibility
- **Testability**: Layers can be tested independently
- **Maintainability**: Changes in one layer don't affect others
- **Flexibility**: Easy to swap implementations (e.g., change from in-memory to a real database)

#### User Action Flow Example

```
User clicks "Login"
    │
    ▼
LoginView (login_view.py)              →  Captures user input
    │
    ▼
InterfaceApp (interface_app.py)        →  Handles navigation and coordination
    │
    ▼
AuthService (auth_service.py)          →  Validates credentials (business rules)
    │
    ▼
UserDAO (user_dao.py)    →  Retrieves user data
    │
    ▼
In-Memory Dict                         →  Stores/retrieves data
```

### Design Patterns

#### 1. Repository Pattern (DAO)

**Purpose**: Abstracts data access logic, providing a clean API for data operations. The business layer doesn't know how data is stored.

**Location**: `src/data_access/user_dao.py`

```python
class UserDAO:
    """In-memory user storage. Replace with a real database implementation."""

    def __init__(self) -> None:
        self._users: dict[str, UserModel] = { ... }

    def get_by_username(self, username: str) -> UserModel | None:
        return self._users.get(username)

    def exists(self, username: str) -> bool:
        return username in self._users

    def save(self, user: UserModel) -> None:
        self._users[user.username] = user
```

**Benefit**: If you switch from in-memory storage to SQLite, PostgreSQL, or any database, only the repository layer needs to change.

#### 2. Service Layer Pattern

**Purpose**: Encapsulates business logic in a dedicated layer. The UI stays thin, and business rules are centralized.

**Location**: `src/services/auth_service.py`

```python
class AuthService:
    # The DAO is injected here because UserDAO uses an in-memory dictionary as the data store.
    # If using a real database, the DAO would be imported and used directly inside each method
    # without needing to initialize it in the constructor.
    def __init__(self, dao: UserDAO) -> None:
        self._dao = dao

    def login(self, username: str, password: str) -> UserModel:
        # Business rules: validate fields, check user exists, verify password
        ...

    def register(self, username: str, password: str, confirm_password: str) -> bool:
        # Business rules: validate fields, check duplicates, hash password
        ...
```

**Benefit**: Business rules are in one place, not scattered across UI code.

#### 3. Template Method Pattern

**Purpose**: Defines a base structure that subclasses can customize by overriding specific parts.

**Location**: `src/configs/`

```python
# default_config.py - Base template
class DefaultConfig:
    def __init__(self) -> None:
        # General
        self.TZ = os.getenv("TZ", "America/Argentina/Buenos_Aires")
        self.DEBUG = False
        self.TESTING = False

        # App
        self.ENV_NAME = os.getenv("ENV_NAME", "python tkinter boilerplate")

# development_config.py - Customizes for development
class DevelopmentConfig(DefaultConfig):
    def __init__(self) -> None:
        super().__init__()
        self.DEBUG = True
        self.ENV = "development"

# production_config.py - Customizes for production
class ProductionConfig(DefaultConfig):
    def __init__(self) -> None:
        super().__init__()
        self.DEBUG = False
        self.ENV = "production"
```

**Benefit**: Common configuration in one place; environments only override what's different.

#### 4. Composite Pattern (UI Components)

**Purpose**: Builds complex UI elements from simpler, reusable components. Each component is self-contained and can be composed into larger views.

**Location**: `src/ui/components/labeled_entry.py`

```python
class LabeledEntry(Frame):
    def __init__(self, parent: Misc, label_text: str, styles: Styles, variable: StringVar, show: str = "") -> None:
        super().__init__(parent, bg=styles.PRIMARY_COLOR)
        # Creates a Label + Entry combination as a single reusable widget
        ...
```

**Usage in Views**:

```python
LabeledEntry(
    parent=self,
    label_text="Username",
    styles=self._styles,
    variable=self.text_username,
).grid(row=0, column=0, pady=(20, 5), sticky="ew")
```

**Benefit**: Eliminates code duplication across views and ensures consistent styling.

### Additional Information

#### Adding a Database

If you need to connect a real database, create the appropriate configuration and modify the repository layer:

1. Add your database library to `[project.dependencies]` in `pyproject.toml` (e.g., `sqlalchemy>=2.0`, `pymongo>=4.0`)
2. Create a database configuration file in `src/configs/` (e.g., `database_config.py`)
3. Update `src/data_access/user_dao.py` to use the database instead of in-memory storage
4. No changes needed in services or UI layers — that's the benefit of the layered architecture

#### Adding New Views

1. Create a new view file in `src/ui/views/` (e.g., `settings_view.py`)
2. The view should extend `Frame` (for embedded views) or `Toplevel` (for new windows)
3. Use existing components from `src/ui/components/` or create new ones
4. Register the navigation in `src/ui/interface_app.py`

#### Adding New Services

1. Create a new service file in `src/services/` (e.g., `product_service.py`)
2. If it needs data access, create a corresponding dao in `src/data_access/`
3. If it needs a data model, create one in `src/models/`
4. Connect it to the UI through `src/ui/interface_app.py`

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -e ".[test]"`
6. Execute: `pytest --log-cli-level=INFO`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -e ".[dev]"`
4. Execute: `pip-audit`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -e ".[build]"`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Continuous Integration

The repository ships with a **GitHub Actions** pipeline defined in [`.github/workflows/ci.yml`](.github/workflows/ci.yml). It runs automatically on every `push` and `pull_request` targeting the `main` branch. On `push` to `main`, the same workflow continues with three additional jobs that produce an automated release.

### Pipeline overview

```
                      ┌─── PR or push to main ───┐
                      ▼                          ▼
┌──────────────────────┐  ┌──────────────────┐  ┌──────────────────┐
│   lint-and-audit     │─▶│       test       │─▶│      build       │
│ ruff · mypy · audit  │  │ pytest (headless)│  │ pyinstaller (lnx)│
└──────────────────────┘  └──────────────────┘  └──────────────────┘
                                                          │
                                       (only on push to main, sequentially)
                                                          ▼
                                                ┌──────────────────────┐
                                                │   prepare-release    │
                                                │ bump · changelog · tag│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │  build-windows-exe   │
                                                │ pyinstaller (windows)│
                                                └──────────────────────┘
                                                          │
                                                          ▼
                                                ┌──────────────────────┐
                                                │   publish-release    │
                                                │ GitHub Release + .exe│
                                                └──────────────────────┘
```

### Validation jobs (run on every PR and push)

1. **`lint-and-audit`** — `ruff check`, `ruff format --check`, `mypy`, `pip-audit --skip-editable`.
2. **`test`** — installs Tkinter + `xvfb` on Ubuntu and runs `pytest --tb=short` headlessly.
3. **`build`** — smoke test that `pyinstaller app.spec` produces a binary on Linux.

### Release jobs (only on push to `main`)

4. **`prepare-release`** — inspects the commits since the latest tag, decides the next SemVer version using [Conventional Commits](#conventional-commits-required-for-releases), generates the changelog section, updates `CHANGELOG.md` and `pyproject.toml`, then commits, tags and pushes back to `main`. Skipped automatically when the head commit is the bot's own `chore(release): vX.Y.Z` commit, to avoid loops.
5. **`build-windows-exe`** — checks out the freshly created tag on a `windows-latest` runner, runs `pyinstaller app.spec`, and renames the artifact to `python-tkinter-boilerplate-vX.Y.Z-windows.exe`.
6. **`publish-release`** — creates the GitHub Release for the new tag, attaches the Windows `.exe`, and uses the generated changelog section as the release notes.

### Conventional Commits (required for releases)

Commits merged into `main` must follow [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) so the pipeline can compute the next version and group the changelog entries.

| Commit prefix | Version bump | Example |
|---|---|---|
| `feat:` / `feat(scope):` | **MINOR** | `feat(ui): add dark mode toggle` |
| `fix:` / `fix(scope):` | **PATCH** | `fix: prevent crash on empty username` |
| `perf:`, `refactor:`, `docs:`, `build:`, `ci:`, `chore:`, `style:`, `test:` | **PATCH** | `refactor: extract auth helper` |
| `feat!:` / `fix!:` or `BREAKING CHANGE:` in the body | **MAJOR** | `feat!: rewrite auth API` |

When a push contains multiple commits, the highest applicable bump wins (a single `feat:` among many `fix:` triggers a MINOR bump). If you squash-merge PRs, configure the repo to use the PR title as the squash commit message and write the **PR title** following the convention.

### Skipping a release

If you need to push a change to `main` without producing a release (e.g. tweaking job names in the workflow, fixing a typo in the README), append `[skip release]` to the commit message. The validation jobs (lint, test, build) still run; only `prepare-release`, `build-windows-exe` and `publish-release` are skipped.

```bash
git commit -m "ci: rename build job for clarity [skip release]"
```

To skip **everything** including validation, use GitHub's standard `[skip ci]` marker instead.

### Where the build outputs live

| Output | Location |
|---|---|
| Validation logs (lint, tests) | **Actions** tab on GitHub |
| Linux smoke-build binary | Ephemeral, inside the runner |
| Windows `.exe` per version | **Releases** page (sidebar of the repo) |
| Version history & notes | [`CHANGELOG.md`](CHANGELOG.md) + Releases page |

> **Note:** GitHub's **Packages** section is for package registries (npm, PyPI, Docker, etc.) and does not host PyInstaller executables. Standalone binaries always live under **Releases**.

### Repository setup required for releases

For the release jobs to push tags and commits back to `main`, the repository needs:

1. **Settings → Actions → General → Workflow permissions**: set to *Read and write permissions*.
2. **Branch protection on `main`**: if enabled, allow the `github-actions[bot]` to bypass the PR requirement, or disable the protection for the bot. Otherwise `prepare-release` will fail when pushing the version bump.

### Running the same checks locally

```bash
# lint-and-audit
ruff check .
ruff format --check .
mypy --config-file=pyproject.toml .
pip-audit --skip-editable

# test
pytest --tb=short

# build
pyinstaller app.spec
```

## Production

Before distributing the application, prepare the production environment and run through the following checklist.

1. Set `ENVIRONMENT=production` and all required env keys with real production values in `.env` (see [Env Keys](#env-keys))
2. Verify `.env` is listed in `.gitignore` — **never commit production secrets to version control**
3. Run the [Security Audit](#security-audit) to check for known vulnerabilities in your dependencies
4. Run the [Testing](#testing) suite to verify everything works
5. Generate the standalone executable following the [Build](#build) steps

The output executable in `dist/` bundles `.env` and assets — it runs on any machine without requiring Python to be installed.

> **Warning:** `app.spec` bundles `.env` into the executable. Make sure `.env` contains only the values needed for the target environment before building.

## Known Issues

None at the moment.

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/python-tkinter-boilerplate`](https://www.diegolibonati.com.ar/#/project/python-tkinter-boilerplate)
