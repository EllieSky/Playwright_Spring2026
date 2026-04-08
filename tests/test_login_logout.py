import re
from playwright.sync_api import Page, expect


def test_login_logout(page: Page):
    page.goto('/')

    # Expect a title "to contain" a substring.
    expect(page).to_have_title("Your store. Home page title")

    page.get_by_role("link", name="Log in").click()
    expect(page).to_have_title(re.compile("Login"))

    page.locator("#Email").fill("user.shopper@yopmail.com")
    page.locator("#Password").fill("user9900")
    page.get_by_role("button", name="Log in").click()

    expect(page.get_by_role("link", name="Log out")).to_be_visible()

    page.get_by_role("link", name="Log out").click()

    expect(page.get_by_role("link", name="Log in")).to_be_visible()
    expect(page.get_by_role('link', name='My account')).to_be_visible()





