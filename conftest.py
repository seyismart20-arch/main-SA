import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def browser(request):
    pw = sync_playwright().start()
    headless = not request.config.getoption("--headed", default=False)
    browser = pw.chromium.launch(headless=headless)
    yield browser
    browser.close()
    pw.stop()


@pytest.fixture(scope="function")
def page(browser):
    ctx = browser.new_context()
    p = ctx.new_page()
    yield p
    p.close()
    ctx.close()
