import re
from playwright.sync_api import Page, expect


def test_valid_login_and_logout(page: Page):
    page.goto("https://nop-qa.portnov.com")
    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").fill("user.shopper@yopmail.com")
    page.locator("input.password").fill("user9900")
    page.get_by_text("Log in", exact=True).click()
    expect(page.get_by_role('link', 'My account')).to_be_visible()
    expect(page.get_by_role('link', 'Log out')).to_be_visible()