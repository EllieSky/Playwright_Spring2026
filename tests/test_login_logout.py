import re

import pytest
from playwright.sync_api import Page, expect


# @pytest.mark.mobile
def test_valid_login_and_logout(page: Page, menu):
    page.goto("/")
    menu.user_menu.goto_login()   # replaces the line below
    # page.get_by_role("link", name="Log in").click()

    page.get_by_label("Email:").fill("user.shopper@yopmail.com")
    # page.locator("#Password")   # Option 1
    page.locator("input.password").fill("user9900") # Option 2
    page.get_by_role('button', name="Log in").click()
    expect(menu.user_menu.link_my_account).to_be_visible()  # replaces the line below
    # expect(page.get_by_role("link", name="My account").first).to_be_visible()
    expect(menu.user_menu.link_logout).to_be_visible()  # replaces the line below
    # expect(page.get_by_role('link', name='Log out')).to_be_visible()

    menu.user_menu.goto_logout()  # replaces the line below
    # page.get_by_role('link', name='Log out').click()

    # expect(page.get_by_role("link", name="My account").first).not_to_be_visible()
    expect(menu.user_menu.link_my_account).to_have_count(0)  # replaces the line below
    # expect(page.locator('.header-links .ico-account')).to_have_count(0)
    expect(menu.user_menu.link_login).to_be_visible()  # replaces the line below
    # expect(page.get_by_role('link', name='Log in')).to_be_visible()


def test_valid_login_and_logout_clean(page: Page, menu):
    page.goto("/")
    menu.user_menu.goto_login()

    page.get_by_label("Email:").fill("user.shopper@yopmail.com")
    page.locator("input.password").fill("user9900")
    page.get_by_role('button', name="Log in").click()
    expect(menu.user_menu.link_my_account).to_be_visible()
    expect(menu.user_menu.link_logout).to_be_visible()

    menu.user_menu.goto_logout()

    expect(menu.user_menu.link_my_account).to_have_count(0)
    expect(menu.user_menu.link_login).to_be_visible()



