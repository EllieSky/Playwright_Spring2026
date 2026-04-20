import re

from faker.proxy import Faker
from playwright.sync_api import Page, expect

from fixtures.new_user import get_shopper


def test_has_title(page: Page, get_shopper):
    # expect(page).not_to_have_url('/registerresult')

    f = Faker()
    user_email = get_shopper[0]
    user_pswd = get_shopper[1]
    user_new_pswd = f.password()

    # user log in to the account
    page.goto('/login')
    page.get_by_role('textbox', name='Email').fill(user_email)
    page.get_by_role('textbox', name='Password').fill(user_pswd)
    # click Log in btn
    page.get_by_role('button', name='Log in').click()
    # move to the My Account
    page.get_by_role("link", name="My account").first.click()
    # Select Change password
    page.get_by_role("link", name="Change password").first.click()

    page.get_by_role("textbox", name="Old password:").fill(user_pswd)
    page.get_by_role("textbox", name="New password:").fill(user_new_pswd)
    page.get_by_role("textbox", name="Confirm password:").fill(user_new_pswd)
    page.get_by_role("button", name="Change password").click()
    # page.get_by_role('alert', name='Password was changed').is_visible()
    page.get_by_text("Password was changed").is_visible()
    page.get_by_title("Close").click()
    page.get_by_role("link", name="Log out").click()
    page.get_by_role("link", name="Log in").click()
    page.get_by_role("textbox", name="Email:").fill(user_email)
    page.get_by_role("textbox", name="Password:").fill(user_new_pswd)
    page.get_by_role("button", name="Log in").click()
    # expect
    expect(page.get_by_role("link", name="My account").first).to_be_visible()
    expect(page.get_by_role("link", name="Log out")).to_be_visible()






