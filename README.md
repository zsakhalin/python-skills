# Python Skills
A repo for learning Python - from basics to confident Junior+ lvl. Each block contains theory notes, examples and practice tasks.

##Contents:
block_01_types
# Python Junior+ Developer Roadmap

A structured, hands-on learning roadmap designed to guide you from foundational Python syntax to a production-ready Junior+ Backend / Python Engineer.

Each block in this repository follows a modular layout:
- `theory.md`: Deep dives into core concepts, best practices, and interview-level questions.
- `examples.py`: Real-world code patterns, clean idioms, and edge cases.
- `tasks.py`: Practical coding exercises, challenges, and unit tests to validate mastery.

---

## Curriculum Overview

### Block 01: Core Python — Types & Data Structures
- **Primitive Types:** `int`, `float`, `str`, `bool`, `None`.
- **Built-in Collections:** `list`, `tuple`, `dict`, `set`, and asymptotic complexity ($O(1)$ vs $O(n)$).
- **Memory Model:** Mutability, references, `id()`, shallow vs. deep copy (`copy`, `deepcopy`).
- **Data Manipulation:** Slicing, comprehensions (list/dict/set), unpacking (`*args`, `**kwargs`), and generator expressions.

---

### Block 02: Control Flow & Logic
- **Conditionals:** `if`, `elif`, `else`, ternary expressions, truthy/falsy semantics.
- **Loops:** `for`, `while`, loop control with `break` and `continue`, loop `else` clauses.
- **Pattern Matching:** Structural pattern matching (`match` / `case`) introduced in Python 3.10+.

---

### Block 03: Functions & Functional Constructs
- **Scoping Rules:** LEGB rule (Local, Enclosing, Global, Built-in), `global` and `nonlocal` keywords.
- **Function Signatures:** Positional, default, keyword-only (`*`), and positional-only (`/`) parameters.
- **Functional Tools:** Lambdas, `map`, `filter`, `zip`, `enumerate`, and standard library modules (`itertools`, `functools`).
- **Iteration Protocol:** Iterables vs iterators, `__iter__`, `__next__`, generator functions, and `yield`.

---

### Block 04: Closures & Decorators
- **Closures:** Inner functions, free variables, and cell objects (`__closure__`).
- **Function Decorators:** Parameterless decorators and parameterized decorator factories.
- **Metadata Preservation:** Using `functools.wraps`.
- **Production Use Cases:** Execution timing, logging, rate limiting, and memoization (`functools.lru_cache`).

---

### Block 05: Exception Handling & Resource Management
- **Exception Hierarchy:** Built-in exception tree, `try` / `except` / `else` / `finally` control flow.
- **Custom Exceptions:** Domain-specific exceptions, exception chaining (`raise ... from ...`).
- **Context Managers:** Resource cleanup, `with` statements, the context manager protocol (`__enter__`, `__exit__`), and `contextlib.contextmanager`.

---

### Block 06: Filesystem, Serialization & Configuration
- **Filesystem Operations:** Modern file path manipulation with `pathlib.Path`.
- **File I/O:** Reading, writing, and streaming text and binary files.
- **Data Serialization:** Parsing and dumping `json` and `csv`.
- **Environment Management:** Twelve-Factor App principles, `os.environ`, `.env` files via `python-dotenv`.

---

### Block 07: Object-Oriented Programming (OOP)
- **Object Fundamentals:** Classes, instances, `__init__`, instance methods, `self`.
- **OOP Pillars:** Encapsulation, inheritance, polymorphism, and composition vs inheritance.
- **Dunder Methods:** String representation (`__repr__`, `__str__`), equality & hashing (`__eq__`, `__hash__`), item access (`__getitem__`), and callable instances (`__call__`).
- **Advanced Attributes:** `@property`, `@classmethod`, `@staticmethod`.
- **Modern Data Modeling:** `dataclasses` and schema validation with Pydantic v2.

---

### Block 08: Static Typing & Type Hinting
- **Type Annotations:** Modern `typing` module syntax (`Union`, `Optional`, `Any`, `Callable`, `Literal`).
- **Generics & Polymorphism:** `TypeVar`, generic classes and functions.
- **Structural Subtyping:** Duck typing formalization via `typing.Protocol`.
- **Static Analysis:** Configuring and running `mypy` for strict type safety.

---

### Block 09: Tooling, Clean Code & Git Workflow
- **Code Standards:** PEP 8 conventions, modern linters and formatters (`ruff`, `black`).
- **Dependency Management:** Virtual environments and deterministic lockfiles using `uv` or `poetry`.
- **Version Control Discipline:** Git branching workflows, Conventional Commits, and `.gitignore` hygiene.

---

### Block 10: Automated Testing
- **Test Frameworks:** Writing automated tests using `pytest`.
- **Test Organization:** Assertions, test discovery, and organizing the `tests/` directory.
- **Parametrization:** Data-driven testing with `@pytest.mark.parametrize`.
- **Fixtures:** Fixture scopes, teardown (`yield` fixtures), and dependency injection in tests.
- **Test Isolation:** Mocking external dependencies with `unittest.mock` and `pytest-mock`.

---

### Block 11: Databases & Persistence
- **Relational Databases:** SQL foundations, normalization, indexes, queries with PostgreSQL / SQLite.
- **Database Drivers:** Low-level connectivity (`psycopg` / `asyncpg`).
- **ORM / Query Builders:** `SQLAlchemy 2.0` (Declarative models, Core expressions, sessions, relationships).
- **Database Migrations:** Schema version control using `Alembic`.

---

### Block 12: Asynchronous Programming (Asyncio)
- **Concurrency Models:** Threads vs Processes vs Asynchronous Event Loop (I/O-bound vs CPU-bound).
- **Core Primitives:** The Event loop, coroutines, `async` / `await` syntax.
- **Task Orchestration:** `asyncio.create_task`, `asyncio.gather`, `asyncio.TaskGroup`.
- **Common Pitfalls:** Preventing blocking calls inside the event loop, handling cancellation and timeouts.

---

### Block 13: Web APIs with FastAPI
- **HTTP Foundations:** Methods (`GET`, `POST`, `PUT`, `DELETE`), status codes, headers, request bodies.
- **RESTful API Design:** Resource naming conventions, idempotency, and standard error handling.
- **FastAPI Framework:** Routing, request validation with Pydantic, and dependency injection (`Depends`).
- **API Documentation:** Interactive OpenAPI and Swagger UI generation.

---

### Block 14: Containerization & CI/CD
- **Docker Fundamentals:** Building clean, multi-stage `Dockerfile`s for Python apps.
- **Multi-Container Orchestration:** Setting up local environments with `docker-compose` (App + PostgreSQL + Redis).
- **Continuous Integration:** GitHub Actions pipelines for automated linting, type checks, and running tests on push / PR.