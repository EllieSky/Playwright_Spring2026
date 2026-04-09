import pytest

from fixtures.new_user import get_shopper

from playwright.sync_api import Page, expect

def test_change_password_successfully(page: Page, get_shopper):

    expect(page).not_to_have_url('/registerresult')

    user_email = get_shopper[0]
    user_pswd = get_shopper[1]

    page.goto('/login')
    page.get_by_label("Email:").fill(user_email)
    page.locator("input.password").fill(user_pswd)
    page.get_by_role('button', name="Log in").click()

    page.locator('.header-links .eco-account').click()
    page.locator('.block-account-navigation').get_by_text('Change password').click()
    page.get_by_role("textbox", name="Old password:").fill("abc")
    page.get_by_role("textbox", name="New password").fill("123Pass")
    page.get_by_role("textbox", name= "Confirm password:").fill("123Pass")
    page.get_by_role("button", name="Change password").click()

    expect(page.get_by_text("Password was changed")).to_be_visible()
    expect(page.locator())

