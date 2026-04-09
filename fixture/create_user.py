import pytest
from playwright.sync_api import Page, expect
from utils.helpers import generate_user_registration_data

@pytest.fixture()
def get_shopper(page: Page):

     user = generate_user_registration_data()

     page.goto('/register')
     page.get_by_role('link', name='Register').click()

     page.locator("#FirstName").fill(user.first_name)
     page.get_by_role("textbox", name="Last name:").fill(user.last_name)

     page.get_by_role("textbox", name="Email:").fill(user.email)
     #page.get_by_role("textbox", name="Company name:").fill(user.company)
     page.get_by_role("checkbox", name="Newsletter:").uncheck()
     page.get_by_role("textbox", name="Password:", exact=True).fill(user.password)
     page.get_by_role("textbox", name="Confirm password:").fill(user.password)

     page.get_by_role("button", name="register").click()

     '''page.locator("select[name=\"DateOfBirthDay\"]").get_by_text(str(user.birth_date.day))
     page.locator("select[name=\"DateOfBirthMonth\"]").select_option(str(user.birth_date.month))
     page.locator("select[name=\"DateOfBirthYear\"]").select_option(str(user.birth_date.year))'''


     expect(page).not_to_have_url('/registerresult')

     return user.email, user.password
