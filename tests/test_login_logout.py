import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):

    #Data
    username = "user.shopper@yopmail.com"
    password = "user9900"
    url = "https://nop-qa.portnov.com/"



    #Get to Home page
    page.goto(url)


    # Verify Page title "to contain" a substring.
    expect(page).to_have_title(re.compile("Home page title", re.IGNORECASE))



    # Click LogIn the get started link.
    page.get_by_role("link", name=re.compile("log in", re.IGNORECASE)).click()



    #Verify URL changed to login page
    expect(page).to_have_url("https://nop-qa.portnov.com/login?returnUrl=%2F")
    #expect(page).to_have_url(re.compile("login\\?returnUrl=%2F"))
    #expect(page).to_have_url(lambda url: "login?returnUrl=%2F" in url)


    #Enter Email and Password
    Email = page.get_by_role("textbox", name = "Email")
    Email.click()
    Email.fill(username)
    page.get_by_role("textbox", name = "Password").click()
    page.get_by_role("textbox", name = "Password").fill(password)


    '''
    <input class="password" type="password" id="Password" name="Password" fdprocessedid="ocu4cb">
    page.get_by_label()
    page.get_by_text(, exact=True)
    page.get_by_attribute()
    page.locator("#Password")
    page.locator(".password")
    page.get_attribute(selector='name', name=password)'''



    #Check Login Button visible
    #<button type="submit" class="button-1 login-button">Log in</button>
    #page.get_by_text("Log in", exact=True).click()
    login_btn = page.get_by_role("button", name = "Log in")
    expect(login_btn).to_be_visible()
    login_btn.click()

    expect(page.get_by_role('link', name = 'My account').first).to_be_visible()
    expect(page.get_by_role('link', name ='Log out')).to_be_visible()
    page.get_by_role('link', name='Log out').click()

    #expect(page.get_by_role('link', name = 'My account').first).not_to_be_visible()
    #//div[@class="header-links"]//a[@class='ico-register']
    #store locator validates but not throws error
    expect(page.locator('.header-links .ico-account')).to_have_count(0)


    #expect(page.get_by_role('link', name='Log in')).to_have_count(0)


    '''LogOut
    page.locator(".ico-logout").click()
    expect(page.locator('.header'))
    expect(page).to_have_url(url)'''




