# from playwright.sync_api import sync_playwright  # playwright framework
from playwright.sync_api import expect
from login_page import LoginPage
import pytest  # pytest framework comes with an inbuilt async test runner

# test case 1 : positive Login test


@pytest.mark.regression
def test_login_example(page):
    login_page = LoginPage(page)
    login_page.login("student", "Password123")
    # Using Page Object Model
    login_page.verify_valid_login(page)


# test case 2 : Negative username test

def test_negative_username(page):
    login_page = LoginPage(page)
    login_page.login("incorrectUser", "Password123")
    # Using Page Object Model
    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_have_text(
        "Your username is invalid!")
    # page.pause()

# test case 3 : Negative password test


def test_negative_password(page):
    login_page = LoginPage(page)
    login_page.login("student", "incorrectPassword")
    # Using Page Object Model
    expect(page.locator("#error")).to_be_visible()
    expect(page.locator("#error")).to_have_text(
        "Your password is invalid!")
    # page.pause()


# pytest asyn runner is used to run the tests in parallel and generate the report
# it initiates a chrome browser instance for each test case, to make our code concise and reusable.

 # to test from the command line, use the command: pytest -m regression/smoke/integration
# to run specific tests with markers like regression, smoke, integration, unit, login, serial
# you can use the command: pytest -m <marker_name>
    # Example: pytest -m regression


# to test pytest async runner, from the command line use the command: pytest --headed
