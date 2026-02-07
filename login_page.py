from playwright.sync_api import expect

# implementing Page Object Model for the login page


class LoginPage:
    def __init__(self, page):  # initializing the page object
        self.page = page

    def login(self, username, password):
        self.page.goto(
            "https://practicetestautomation.com/practice-test-login/")
        self.page.get_by_role("textbox", name="Username").click()
        self.page.get_by_role("textbox", name="Username").fill(username)
        self.page.get_by_role("textbox", name="Password").click()
        self.page.get_by_role("textbox", name="Password").fill(password)
        self.page.get_by_role("button", name="Submit").click()

    def verify_valid_login(self, page):
        url = "https://practicetestautomation.com/logged-in-successfully/"
        expect(page).to_have_url(url)
        expect(page.get_by_text("Congratulations student. You")).to_be_visible()
        expect(page.get_by_role("link", name="Log out")).to_be_visible()
