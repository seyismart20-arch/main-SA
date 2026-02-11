# Playwright Automation

[![CI](https://github.com/seyismart20-arch/main-SA/actions/workflows/ci.yml/badge.svg)](https://github.com/seyismart20-arch/main-SA/actions/workflows/ci.yml)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

UI test automation using Playwright + Pytest, with both POM-style tests and BDD scenarios. The sample tests cover login success and failure flows on Practice Test Automation.

## Tech Stack

- Python
- Playwright (sync API)
- Pytest
- Pytest-bdd
- Allure (optional reporting)

## Project Structure

- conftest.py: Pytest fixtures for browser/page lifecycle.
- login_page.py: Page Object Model for the login page.
- test_playwright.py: POM tests.
- features/login.feature: BDD scenarios.
- steps/login_steps.py: BDD step definitions.
- pytest.ini: Pytest config and markers.

## Setup

1) Create and activate a virtual environment (optional but recommended).

2) Install dependencies:

```powershell
pip install -r requirements.txt
```

Or install manually:

```powershell
pip install playwright pytest pytest-bdd allure-pytest
```

3) Install Playwright browsers:

```powershell
playwright install
```

## Run Tests

Run all tests:

```powershell
pytest
```

Run in headed mode:

```powershell
pytest --headed
```

Run by marker:

```powershell
pytest -m regression
```

## Run BDD Scenarios Only

```powershell
pytest -k "login.feature"
```

## Allure Report (Optional)

Generate results:

```powershell
pytest --alluredir=allure-results
```

Create the HTML report:

```powershell
allure generate allure-results --clean -o allure-report
```

Open the report locally (optional):

```powershell
allure open allure-report
```

## Browser Notes

By default, Playwright launches its bundled Chromium. If you want to use installed Chrome or Edge, update the launch call in conftest.py:

```python
browser = pw.chromium.launch(channel="chrome", headless=headless)
# or
browser = pw.chromium.launch(channel="msedge", headless=headless)
```

## Troubleshooting

- If PowerShell complains about line breaks, use the backtick for continuation:

```powershell
allure generate allure-results `
	--clean -o allure-report
```

## CI (GitHub Actions)

A basic CI workflow is included at .github/workflows/ci.yml. It runs tests on push and pull requests using Python and Playwright.
