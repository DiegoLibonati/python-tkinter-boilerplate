# Template Tkinter Program

## Educational Purpose

This project was created primarily for **educational and learning purposes**.  
While it is well-structured and could technically be used in production, it is **not intended for commercialization**.  
The main goal is to explore and demonstrate best practices, patterns, and technologies in software development.

## Getting Started

1. Clone the repository
2. Go to the repository folder and execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.dev.txt`
7. Execute: `pip install -r requirements.test.txt`
8. Use `python app.py` or `python -m src` to execute the program

### Pre-Commit for Development

NOTE: Install **pre-commit** inside the repository folder.

1. Once you're inside the virtual environment, let's install the hooks specified in the pre-commit. Execute: `pre-commit install`
2. Now every time you try to commit, the pre-commit lint will run. If you want to do it manually, you can run the command: `pre-commit run --all-files`

## Description

Personal template for developing a desktop application with a graphical interface using Tkinter and Python.

## Technologies used

1. Python >= 3.11
2. Tkinter

## Libraries used

#### Requirements.txt
```
pydantic==2.11.9
python-dotenv==1.0.1
```

#### Requirements.dev.txt
```
pre-commit==4.3.0
pip-audit==2.7.3
```

#### Requirements.test.txt
```
pytest==8.4.2
pytest-env==1.1.5
pytest-cov==4.1.0
pytest-timeout==2.3.1
pytest-xdist==3.5.0
```

#### Requirements.build.txt
```
pyinstaller==6.16.0
```

## Portfolio Link

[`https://www.diegolibonati.com.ar/#/project/Template-Tkinter-Program`](https://www.diegolibonati.com.ar/#/project/Template-Tkinter-Program)

## Testing

1. Go to the repository folder
2. Execute: `python -m venv venv`
3. Execute in Windows: `venv\Scripts\activate`
4. Execute in Linux/Mac: `source venv/bin/activate`
5. Execute: `pip install -r requirements.txt`
6. Execute: `pip install -r requirements.test.txt`
7. Execute: `pytest --log-cli-level=INFO`

## Build

You can generate a standalone executable (`.exe` on Windows, or binary on Linux/Mac) using **PyInstaller**.

### Windows

1. Go to the repository folder
2. Activate your virtual environment: `venv\Scripts\activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `build.bat`

### Linux / Mac

1. Go to the repository folder
2. Activate your virtual environment: `source venv/bin/activate`
3. Install build dependencies: `pip install -r requirements.build.txt`
4. Create the executable: `pyinstaller app.spec`

Alternatively, you can run the helper script: `./build.sh`

## Security Audit

You can check your dependencies for known vulnerabilities using **pip-audit**.

1. Go to the repository folder
2. Activate your virtual environment
3. Execute: `pip install -r requirements.dev.txt`
4. Execute: `pip-audit -r requirements.txt`

## Env Keys

1. `ENVIRONMENT`: Defines the application environment. Accepts `development`, `production`, or `testing`.
2. `ENV_NAME`: A custom environment variable for template demonstration purposes.

```
ENVIRONMENT=development
ENV_NAME=template_value
```

## Project Structure

```
Template-Tkinter-Program/
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
│   │   ├── error_handler.py
│   │   ├── exceptions_handler.py
│   │   └── __init__.py
│   ├── assets/
│   │   └── images/
│   ├── __init__.py
│   └── __main__.py
├── test/
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
12. `utils` -> Contains **shared utilities** for general-purpose helper functions used across multiple modules.
13. `assets` -> Static files such as **images and icons** used by the application.
14. `test` -> Contains **tests** organized to mirror the `src/` structure.
15. `conftest.py` -> Defines **pytest fixtures** for application setup and test data.
16. `app.py` -> The **application entry point**. Creates the Tkinter root window and initializes the application.
17. `pyproject.toml` -> **Unified project configuration** for pytest, ruff, and project metadata.
18. `requirements.txt` -> Lists **production dependencies**.
19. `requirements.dev.txt` -> Lists **development dependencies** (pre-commit, pip-audit).
20. `requirements.test.txt` -> Lists **testing dependencies** (pytest, pytest-env, etc.).
21. `requirements.build.txt` -> Lists **build dependencies** (PyInstaller).
22. `app.spec` -> **PyInstaller configuration** for generating standalone executables.

## Architecture & Design Patterns

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
        self.ENV_NAME = os.getenv("ENV_NAME", "template tkinter python")

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

## Additional Information

### Adding a Database

If you need to connect a real database, create the appropriate configuration and modify the repository layer:

1. Add your database library to `requirements.txt` (e.g., `sqlite3`, `sqlalchemy`, `pymongo`)
2. Create a database configuration file in `src/configs/` (e.g., `database_config.py`)
3. Update `src/data_access/user_dao.py` to use the database instead of in-memory storage
4. No changes needed in services or UI layers — that's the benefit of the layered architecture

### Adding New Views

1. Create a new view file in `src/ui/views/` (e.g., `settings_view.py`)
2. The view should extend `Frame` (for embedded views) or `Toplevel` (for new windows)
3. Use existing components from `src/ui/components/` or create new ones
4. Register the navigation in `src/ui/interface_app.py`

### Adding New Services

1. Create a new service file in `src/services/` (e.g., `product_service.py`)
2. If it needs data access, create a corresponding dao in `src/data_access/`
3. If it needs a data model, create one in `src/models/`
4. Connect it to the UI through `src/ui/interface_app.py`

## Known Issues

None at the moment.