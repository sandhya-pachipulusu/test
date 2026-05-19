# Playwright Demo

This repository contains a small Playwright Python test project for Wikipedia. It includes sample tests, Playwright trace capture, and generated test artifacts.

## Contents

- `tests/test_basic_assertions.py` — Playwright tests using `unittest` and `playwright.sync_api`.
- `tests/Restaurant_Search.py` — Playwright Google Maps search test with tracing enabled.
- `report.html` — Generated HTML report artifact.
- `trace.zip` — Playwright trace file for debugging.
- `wikipedia_homepage.png` — Screenshot captured during test execution.
- `venv1/` — Local Python virtual environment (not recommended to commit).

## Requirements

- Python 3.11+ (or compatible version)
- Playwright installed in a Python environment

## Setup

1. Activate the virtual environment:

```powershell
cd c:\Users\psand\Downloads\playwrightdemo
.\venv1\Scripts\Activate.ps1
```

2. Install dependencies if needed:

```powershell
python -m pip install playwright pytest pytest-html
python -m playwright install
```

## Run Tests

Run the single test file with pytest and generate an HTML report:

```powershell
pytest tests/test_basic_assertions.py --html=report.html --self-contained-html
```

## View Artifacts

- Open `report.html` in a browser to see the test report.
- Use Playwright trace viewer for `trace.zip`:

```powershell
python -m playwright show-trace trace.zip
```

## Notes

- The project currently includes a trace file and screenshot artifact from the latest test run.
- The `venv1/` directory is included in the workspace but should normally be excluded from source control.

## GitHub Upload Instructions

To publish this project to GitHub:

```powershell
cd c:\Users\psand\Downloads\playwrightdemo
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<your-username>/<repo-name>.git
git push -u origin main
```

Replace `<your-username>` and `<repo-name>` with your GitHub account and desired repository name.
