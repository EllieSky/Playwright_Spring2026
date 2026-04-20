import re

from playwright.sync_api import Page, expect

# To test when user log in and log out

def test_valid_login_logout(page: Page):
    # open the page
    page.goto("https://nop-qa.portnov.com")

    # click to the Log in btn at the page
    page.get_by_role('link', name='Log in').click()

    # verify that the next page was opened
    # expected_url = 'https://nop-qa.portnov.com/login?returnUrl=%2F'
    # expect(page).to_have_url(re.compile(f"{expected_url}"))

    # next fill email and password
    # create variables
    email_user = "user.shopper@yopmail.com"
    password_user = "user9900"

    # fill out with that variables
    page.get_by_role('textbox', name='Email').fill(email_user)
    page.get_by_role('textbox', name='Password').fill(password_user)
    # click Log in btn
    page.get_by_role('button', name='Log in').click()

    # verify that user logged in by finding my account at the page
    expect(page.locator('.header').get_by_role('link', name='My account')).to_be_visible()

    # Log out from the account
    page.get_by_role('link', name='Log out').click()

    # Verify user was successfully log out
    expect(page.get_by_role('link', name='Log in')).to_be_visible()

    # when object hidden, but still presents/exists at the page - "not to be visible"
    expect(page.get_by_role('link', name='Log in')).not_to_be_visible()






