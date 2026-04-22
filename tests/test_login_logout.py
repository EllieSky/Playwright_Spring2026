import re

from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from utils.helpers import generate_user_registration_data


# To test when user log in and log out

def test_valid_login_logout(page: Page, menu):
    # open the page
    # page.goto("https://nop-qa.portnov.com")
    page.goto('/login')

    # click to the Log in btn at the page
    # page.get_by_role('link', name='Log in').click()
    menu.user_menu.goto_login()

    # verify that the next page was opened
    # expected_url = 'https://nop-qa.portnov.com/login?returnUrl=%2F'
    # expect(page).to_have_url(re.compile(f"{expected_url}"))

    # next fill email and password
    # create variables
    # email_user = "user.shopper@yopmail.com"
    # password_user = "user9900"
    email_user = "nicksmith@google.com"
    password_user = "password1"


    # fill out with that variables
    page.get_by_role('textbox', name='Email').fill(email_user)
    page.get_by_role('textbox', name='Password').fill(password_user)
    # click Log in btn
    page.get_by_role('button', name='Log in').click()

    # verify that user logged in by finding my account at the page
    expect(page.locator('.header').get_by_role('link', name='My account')).to_be_visible()
    # if the user already logged in
    page.get_by_title("Close").click()

    # Log out from the account
    # page.get_by_role('link', name='Log out').click()
    menu.user_menu.goto_logout()

    # Verify user was successfully log out
    # expect(page.get_by_role('link', name='Log in')).to_be_visible()
    expect(menu.user_menu.link_login).to_be_visible()
    expect(menu.user_menu.link_my_account).to_have_count(0)

    # when object hidden, but still presents/exists at the page - "not to be visible"
    # expect(page.get_by_role('link', name='Log in')).not_to_be_visible()


def test_valid_login_logout_clean_with_login(page: Page, menu):
    login_page = LoginPage(page)

    page.goto('/login')
    menu.user_menu.goto_login()

    email_user = "nicksmith@google.com"
    password_user = "password1"

    login_page.authenticate(email_user, password_user)

    expect(menu.user_menu.link_my_account).to_be_visible()
    page.get_by_title("Close").click()
    menu.user_menu.goto_logout()

    expect(menu.user_menu.link_login).to_be_visible()
    expect(menu.user_menu.link_my_account).to_have_count(0)






