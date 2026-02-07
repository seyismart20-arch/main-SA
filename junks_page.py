
"""
def test_example():
    with sync_playwright()as p:  # the p is a function that starts a browser
        # function that starts a chrome browser
        browser = p.chromium.launch()  # (headless=true, slow_mo=500)
        page = browser.new_page()  # creates a new browser page
        page.goto("http://example.com")  # triggers the url
        browser.close()  # closes the browser
# by default, playwright test in headless mode, i.e., running the test without having to trigger a browser physically
# useful for CI/CD process where testers run tests in cloud.


def test_example_1():
    with sync_playwright()as p:  # the p is a function that starts a browser
        # function that starts a chrome browser
        # to trigger a physical browser, reduce the speed
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()  # creates a new browser page
        page.goto("https://playwright.dev/")  # triggers the url
        page.get_by_role("link", name="Docs").click()
        page.get_by_role("link", name="Writing tests", exact=True).click()
        page.get_by_role("link", name="actionability").click()
        page.get_by_role("link", name="Visible").first.click()
        # playwright inspector was used
        # page.pause()  # to pause and inspect
        browser.close()  # closes the browser

# test case 1 : positive Login test

 # Using Page Object Model"
        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("student")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").press("CapsLock")
        page.get_by_role("textbox", name="Password").fill("P")
        page.get_by_role("textbox", name="Password").press("CapsLock")
        page.get_by_role("textbox", name="Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()
         url = "https://practicetestautomation.com/logged-in-successfully/"
        expect(page).to_have_url(url)
        expect(page.get_by_text("Congratulations student. You")).to_be_visible()
        expect(page.get_by_role("link", name="Log out")).to_be_visible()

        
# test case 2 : Negative username test


        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("incorrect")
        page.get_by_role("textbox", name="Username").fill("incorrectU")
        page.get_by_role("textbox", name="Username").fill("incorrectUser")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("P")
        page.get_by_role("textbox", name="Password").fill("Password123")
        page.get_by_role("button", name="Submit").click()
         expect(page.locator("#error")).to_be_visible()
        expect(page.locator("#error")).to_have_text(
            "Your username is invalid!")
        # page.pause()
        

# test case 3 : Negative password test

        page.goto("https://practicetestautomation.com/practice-test-login/")
        page.get_by_role("textbox", name="Username").click()
        page.get_by_role("textbox", name="Username").fill("student")
        page.get_by_role("textbox", name="Password").click()
        page.get_by_role("textbox", name="Password").fill("incorrect")
        page.get_by_role("textbox", name="Password").fill("incorrectP")
        page.get_by_role("textbox", name="Password").fill("incorrectPassword")
        page.get_by_role("button", name="Submit").click()
         expect(page.locator("#error")).to_be_visible()
        expect(page.locator("#error")).to_have_text(
            "Your password is invalid!")
"""


# to test from the command line, use the command: pytest -m regression/smoke/integration
# to run specific tests with markers like regression, smoke, integration

"""
markers =
    regression: marks tests as part of regression suite
    smoke: marks tests as part of smoke suite
    integration: marks tests as part of integration suite
    unit: marks tests as part of unit suite
    login: marks tests related to login functionality
    serial: marks tests that must be run seriallyly due to shared state or dependencies

"""