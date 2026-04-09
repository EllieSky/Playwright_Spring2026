import re
from faker import Faker
import pytest
from playwright.sync_api import Page, expect
from utils.helpers import generate_user_registration_data


def test_register_shopper(page: Page):

   user = generate_user_registration_data()




   ''' f = Faker()
    first_name = f.first_name_female()
    last_name = f.last_name()
    birth_date = f.date_of_birth()
    email = f.free_email()
    password = f.password(8)
    company = f.company()'''


    page.goto("https://nop-qa.portnov.com/")
    page.get_by_role('link', name = 'Register').click()

    page.locator("#FirstName").fill(user.first_name)
    page.get_by_role("textbox", name = "Last name:").fill(user.last_name)


    page.locator("select[name=\"DateOfBirthDay\"]").get_by_text(str(user.birth_date.day))
    page.locator("select[name=\"DateOfBirthMonth\"]").select_option(str(user.birth_date.month))
    page.locator("select[name=\"DateOfBirthYear\"]").select_option(str(user.birth_date.year))



    page.get_by_role("textbox", name="Email:").fill(user.email)
    page.get_by_role("textbox", name="Company name:").fill(user.company)
    page.get_by_role("checkbox", name="Newsletter:").uncheck()
    page.get_by_role("textbox", name="Password:", exact=True).fill(user.password)
    page.get_by_role("textbox", name="Confirm password:").fill(user.password)

    page.pause()

    page.get_by_role("button", name="Register").click()

    expect(page.get_by_text("Your registration completed")).to_be_visible()
    expect(page.locator('.registration-result-page .result')).to_contain_text("Your registration completed")



    #After clicking register
    page.locator('.header-links .ico-account').click()
    expect(page.get_by_role("textbox", name ="First name:")).to_have_value(user.first_name)
    expect(page.get_by_role("textbox", name ="Last name:")).to_have_value(user.last_name)
    expect(page.get_by_role("textbox", name ="Email:")).to_have_value(user.email)
    expect(page.get_by_role("textbox", name ="Company name:")).to_have_value(user.company)
    expect(page.get_by_role("checkbox", name="Newsletter:")).not_to_be_checked()


def test_user_registration_fails_with_mismatched_password():
   pass



@pytest.mark.parametrize()
def test_user_registration_fails_with_missing_required_fields():














