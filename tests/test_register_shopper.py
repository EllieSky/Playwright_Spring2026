import re
from playwright.sync_api import Page, expect
from faker import Faker

import config
from utils.helpers import generate_user_registration_data


def test_has_title(page: Page):
    user = generate_user_registration_data()
    # page.goto(config.get_base_url())
    page.goto("/")
    page.get_by_role("link", name="Register").click()
    page.locator(".male").click()
    page.get_by_role("textbox", name="First name:").fill(user.first_name)
    page.get_by_role("textbox", name="Last name:").fill(user.last_name)
    page.locator("select[name=\"DateOfBirthDay\"]").select_option(user.date_of_birth_day)
    page.locator("select[name=\"DateOfBirthMonth\"]").select_option(user.date_of_birth_month)
    page.locator("select[name=\"DateOfBirthYear\"]").select_option(user.date_of_birth_year)
    page.get_by_role("textbox", name="Email:").fill(user.email)
    page.get_by_role("textbox", name="Company name:").fill(user.company_name)
    page.get_by_role("textbox", name="Password:", exact=True).fill(user.password)
    page.get_by_role("textbox", name="Confirm password:").fill(user.confirm_password)
    page.get_by_role("button", name="Register").click()
    expect(page.get_by_text("Your registration completed")).to_be_visible()

    expect(page.locator('.registration-result-page .result')).to_contain_text('Your registration completed')



    page.locator('.header-links .ico-account').click()

    expect(page.get_by_role("textbox", name="First name:")).to_have_value(user.first_name)
    expect(page.get_by_role("textbox", name="Last name:")).to_have_value(user.last_name)
    expect(page.get_by_role("textbox", name="Email:")).to_have_value(user.email)
    expect(page.get_by_role("textbox", name="Company name:")).to_have_value(user.company_name)
    expect(page.get_by_role("checkbox", name="Newsletter:")).to_be_checked()






