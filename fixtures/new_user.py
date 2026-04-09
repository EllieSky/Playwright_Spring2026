import pytest
from playwright.sync_api import Page, expect
from utils.helpers import generate_user_registration_data
import config


@pytest.fixture
def get_shopper(page: Page):
    user = generate_user_registration_data()
    page.goto(f"{config.get_base_url().rstrip('/')}/register")
    page.get_by_role("textbox", name="First name:").fill(user.first_name)
    page.get_by_role("textbox", name="Last name:").fill(user.last_name)
    page.get_by_role("textbox", name="Email:").fill(user.email)
    page.get_by_role("checkbox", name="Newsletter").uncheck()
    page.get_by_role("textbox", name="Password:", exact=True).fill(user.password)
    page.get_by_role("textbox", name="Confirm password:").fill(user.confirm_password)
    page.get_by_role("button", name="Register").click()

    # expect(page).to_have_url("https://nop-qa.portnov.com/registerresult/1")

    return user.email, user.password
