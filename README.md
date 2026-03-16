# QA API Test Framework

Senior-style API automation testing framework built with Python, Pytest, and Requests.

## Tech Stack
- Python
- Pytest
- Requests
- Pydantic
- PyYAML
- Faker
- GitHub Actions

## Features
- Scalable framework structure
- Smoke, regression, integration layers
- Environment-based config
- Reusable client architecture
- Schema validation
- CI-ready

## Run tests

```bash
pip install -r requirements.txt
pytest -m smoke

---

# Komandalar

## Papkalarni yaratish
Windows terminalda:

```bash
mkdir qa-api-test-framework
cd qa-api-test-framework
mkdir .github
mkdir .github\workflows
mkdir config
mkdir config\environments
mkdir data
mkdir src
mkdir src\clients
mkdir src\schemas
mkdir src\utils
mkdir src\assertions
mkdir tests
mkdir tests\smoke
mkdir tests\regression
mkdir tests\integration

---

# Komandalar

## Papkalarni yaratish
Windows terminalda:

```bash
mkdir qa-api-test-framework
cd qa-api-test-framework
mkdir .github
mkdir .github\workflows
mkdir config
mkdir config\environments
mkdir data
mkdir src
mkdir src\clients
mkdir src\schemas
mkdir src\utils
mkdir src\assertions
mkdir tests
mkdir tests\smoke
mkdir tests\regression
mkdir tests\integration

## Project Structure

- `src/clients` — API client layer
- `src/assertions` — reusable assertion methods
- `src/utils` — logger and config reader
- `tests/smoke` — critical smoke coverage
- `tests/regression` — broader functional checks
- `tests/integration` — end-to-end workflow tests