# AegisAI Development Standards

## Python

AegisAI uses Python 3.11 as its primary Python version.

Supported Python versions are:

- Python 3.11
- Python 3.12

Python dependencies are managed through `pyproject.toml` and `uv.lock`.

## Code Quality

All Python code should pass:

- Ruff linting
- Ruff formatting
- Pyright type checking

Run:

```powershell
ruff check .
ruff format --check .
pyright
