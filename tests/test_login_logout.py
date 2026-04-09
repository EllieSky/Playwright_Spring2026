import re
from playwright.sync_api import Page, expect


def test_valid_login_and_logout(page: Page):
    page.goto("https://nop-qa.portnov.com/")
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").fill("user.shopper@yopmail.com")
    # page.locator("#Password")   # Option 1
    page.locator("input.password").fill("user9900") # Option 2
    page.get_by_role('button', name="Log in").click()
    expect(page.get_by_role("link", name="My account").first).to_be_visible()
    expect(page.get_by_role('link', name='Log out')).to_be_visible()

    page.get_by_role('link', name='Log out').click()
    # expect(page.get_by_role("link", name="My account").first).not_to_be_visible()
    expect(page.locator('.header-links .ico-account')).to_have_count(0)
    expect(page.get_by_role('link', name='Log in')).to_be_visible()





    # Expect a title "to contain" a substring.
    #expect(page).to_have_title(re.compile("Playwright"))
