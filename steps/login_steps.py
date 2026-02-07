from pytest_bdd import scenario, given, when, then
from playwright.sync_api import expect

LOGIN_URL = "https://practicetestautomation.com/practice-test-login/"
SUCCESS_URL = "https://practicetestautomation.com/logged-in-successfully/"


@scenario("features/login.feature", "Successful login with valid credentials")
def test_successful_login():
    pass


@scenario("features/login.feature", "Failed login with invalid username")
def test_invalid_username():
    pass


@scenario("features/login.feature", "Failed login with invalid password")
def test_invalid_password():
    pass


@given("I navigate to the login page")
def navigate_to_login_page(page):
    page.goto(LOGIN_URL)


@when('I enter username "{username}" and password "{password}"')
def enter_credentials(page, username, password):
    page.get_by_role("textbox", name="Username").fill(username)
    page.get_by_role("textbox", name="Password").fill(password)


@when("I click the Submit button")
def click_submit(page):
    page.get_by_role("button", name="Submit").click()


@then('I should see the success message "{message}"')
def verify_success_message(page, message):
    expect(page.get_by_text(message)).to_be_visible()


@then("I should see the logout link")
def verify_logout_link(page):
    expect(page.get_by_role("link", name="Log out")).to_be_visible()


@then("I should be on the logged-in page")
def verify_logged_in_page(page):
    expect(page).to_have_url(SUCCESS_URL)


@then("I should see an error message")
def verify_error_visible(page):
    expect(page.locator("#error")).to_be_visible()


@then('I should see error text "{text}"')
def verify_error_text(page, text):
    expect(page.locator("#error")).to_have_text(text)
