import pytest
from playwright.sync_api import Page, expect

from utils.helpers import generate_user_registration_data

@pytest.fixture
def get_shopper(page: Page):
    user = generate_user_registration_data()

    page.goto("/register")
    page.get_by_role('link', name='Register').click()

    # user moved to the Register page
    page.locator("#FirstName").fill(user.first_name)
    page.locator("#LastName").fill(user.last_name)

    page.locator("#Email").fill(user.email)
    page.locator("#Newsletter").uncheck()
    page.locator("#Password").fill(user.password)
    page.locator("#ConfirmPassword").fill(user.password)
    page.get_by_role("button", name="Register").click()
    #two options below for expected result, just one will be enough
    expect(page).not_to_have_url('/registerresult')

    return user.email, user.password