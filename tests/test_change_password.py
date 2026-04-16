from playwright.sync_api import Page, expect
from fixtures.api_fixtures import api_register_user


def test_change_password_successfully(page: Page, api_register_user):
    user_email = api_register_user['email']
    user_pswd = api_register_user['password']

    # Expect a title "to contain" a substring.
    # expect(page).not_to_have_url('/registerresult')
    #
    # user_email = get_shopper[0]
    # user_pswd = get_shopper[1]

    page.goto('/login')
    page.get_by_label("Email:").fill(user_email)
    page.locator("input.password").fill(user_pswd)
    page.get_by_role('button', name="Log in").click()

    page.locator('.header-links .ico-account').click()
    page.locator('.block-account-navigation').get_by_text('Change password').click()

    page.get_by_role("textbox", name="Old password:").fill(user_pswd)
    page.get_by_role("textbox", name="New password:").fill("123Pass")
    page.get_by_role("textbox", name="Confirm password:").fill("123Pass")
    page.get_by_role("button", name="Change password").click()

    # Anywhere on the page
    expect(page.get_by_text('Password was changed')).to_be_visible()

    #Specificly in the notification bar
    expect(page.locator('#bar-notification').get_by_text('Password was changed')).to_be_visible()
    page.get_by_title('Close').click()

    page.get_by_role('link', name='Log out').click()
    expect(page.get_by_role('link', name='Log in')).to_be_visible()

    page.get_by_role("link", name="Log in").click()
    page.get_by_label("Email:").fill(user_email)
    page.locator("input.password").fill("123Pass")
    page.get_by_role('button', name="Log in").click()

    expect(page.get_by_role("link", name="My account").first).to_be_visible()
    expect(page.get_by_role('link', name='Log out')).to_be_visible()