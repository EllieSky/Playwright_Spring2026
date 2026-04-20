from playwright.sync_api import Page, expect
from utils.helpers import generate_user_registration_data

def test_register_shopper(page: Page):
    user = generate_user_registration_data()

    page.goto("https://nop-qa.portnov.com")
    page.get_by_role('link', name='Register').click()

    # user moved to the Register page
    page.locator("#gender-male").click()
    page.locator("#FirstName").fill(user.first_name)
    page.locator("#LastName").fill(user.last_name)

    # page.get_by_role("combobox", name="DateOfBirthDay").select_option(birth_date.day)
    page.locator("select[name=\"DateOfBirthDay\"]").select_option(str(user.birth_date.day))
    page.locator("select[name=\"DateOfBirthMonth\"]").select_option(str(user.birth_date.month))
    page.locator("select[name=\"DateOfBirthYear\"]").select_option(str(user.birth_date.year))

    page.locator("#Email").fill(user.email)
    page.locator("#Company").fill(user.company)
    page.locator("#Newsletter").uncheck()
    page.locator("#Password").fill(user.password)
    page.locator("#ConfirmPassword").fill(user.password)
    # page.pause()
    # page.get_by_role("button", name="Register").click()

    page.get_by_role("button", name="Register").click()
    #two options below for expected result, just one will be enough
    expect(page.get_by_text("Your registration completed")).to_be_visible()
    expect(page.locator(".registration-result-page .result")).to_contain_text("Your registration completed")
    expect(page.get_by_role("link", name="Continue")).to_be_visible()
    # page.pause()

    # when user successfully registered, then his information should be in account
    # thereby we will check expected information filled in the account info
    page.get_by_role("link", name="Continue").click()
    page.get_by_role("link", name="My account").first.click()
    expect(page.locator("#FirstName")).to_have_value(user.first_name)
    expect(page.locator("#LastName")).to_have_value(user.last_name)
    expect(page.locator("#Email")).to_have_value(user.email)
    # # expect(page.get_by_text("Gender: Male Female First")).to_have_text()
    expect(page.locator("#Company")).to_have_value(user.company)
    expect(page.locator("#Newsletter")).not_to_be_checked()
    # page.get_by_role("button", name="Save").hover()







