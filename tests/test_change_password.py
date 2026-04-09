import re
from playwright.sync_api import Page, expect


def test_change_password_successfully(page: Page, get_shopper):

    # Expect a title "to contain" a substring.
    expect(page).to_have_url('https://nop-qa.portnov.com/registerresult/1')
    user_email = get_shopper[0]
    user_pswd = get_shopper[1]

    page.goto("https://nop-qa.portnov.com/login")
    page.locator("#Email").fill(user_email)
    page.locator("#Password").fill(user_pswd)
    page.get_by_role("button", name="Log in").click()
    page.locator('.header-links .ico-account').click()
    page.locator('.block-account-navigation').get_by_text('Change password').click()
    # page.get_by_role("link", name="Change password").click()
    page.get_by_role("textbox", name="Old password:").fill(user_pswd)
    page.get_by_role("textbox", name="New password:").fill('123Pass')
    page.get_by_role("textbox", name="Confirm password:").fill('123Pass')
    page.get_by_role("button", name="Change password").click()
    # anywhere on the page
    expect(page.get_by_text('Password was changed')).to_be_visible()

    #specifically in the notification bar
    expect(page.locator('#bar-notification').get_by_text('Password was changed')).to_be_visible()
    page.get_by_title('Close').click()

    page.get_by_role("link", name="Log out").click()

    expect(page.get_by_role("link", name="Log in")).to_be_visible()
    expect(page.get_by_role('link', name='My account')).to_be_visible()

    page.get_by_role("link", name="Log in").click()
    page.locator("#Email").fill(user_email)
    page.locator("#Password").fill("123Pass")
    page.get_by_role("button", name="Log in").click()

    expect(page.get_by_role('link', name='My account').first).to_be_visible()
    expect(page.get_by_role("link", name="Log out")).to_be_visible()
