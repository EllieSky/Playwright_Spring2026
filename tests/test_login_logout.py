import re
from playwright.sync_api import Page, expect


def test_valid_login_and_logout_clean(page: Page, menu):
    page.goto("/")
    # page.get_by_role("link", name="Log in").click()
    menu.user_menu.go_to_login()
    page.get_by_label("Email:").fill("user.shopper@yopmail.com")
    # page.locator("#Password")   # Option 1
    page.locator("input.password").fill("user9900") # Option 2
    page.get_by_role('button', name="Log in").click()
    # expect(page.get_by_role("link", name="My account").first).to_be_visible()
    expect(menu.user_menu.link_myaccount).to_be_visible()
    # expect(page.get_by_role('link', name='Log out')).to_be_visible()
    expect(menu.user_menu.link_logout).to_be_visible()

    # page.get_by_role('link', name='Log out').click()
    menu.user_menu.goto_logout()
    # expect(page.get_by_role("link", name="My account").first).not_to_be_visible()
    expect(menu.user_menu.link_myaccount).not_to_be_visible()
    expect(page.locator('.header-links .ico-account')).to_have_count(0)
    # expect(page.get_by_role('link', name='Log in')).to_be_visible()
    expect(menu.user_menu.link_login).to_be_visible()



