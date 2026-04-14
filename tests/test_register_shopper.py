from playwright.sync_api import Page, expect
from utils.helpers import generate_user_registration_data

def test_register_shopper(page: Page, menu, register_page):
    user = generate_user_registration_data()
    password = user.password

    page.goto("/")
    menu.user_menu.goto_register()

    register_page.select_gender_m.click()
    register_page.first_name.fill(user.first_name)
    register_page.last_name.fill(user.last_name)
    register_page.select_day.select_option(str(user.birth_date.day))
    register_page.select_month.select_option(str(user.birth_date.month))
    register_page.select_year.select_option(str(user.birth_date.year))
    register_page.email.fill(user.email)
    register_page.company_name.fill(user.company)
    register_page.newsletter.uncheck()
    register_page.password.fill(password)
    register_page.confirm_password.fill(password)
    register_page.register_button.click()

    expect(register_page.registration_completed_msg_box).to_be_visible()
    expect(register_page.registration_completed_msg).to_contain_text("Your registration completed")
    expect(register_page.continue_link).to_be_visible()

    # after clicking register
    menu.user_menu.goto_my_account()

    expect(register_page.first_name).to_have_value(user.first_name)
    expect(register_page.last_name).to_have_value(user.last_name)
    expect(register_page.select_day).to_have_value(str(user.birth_date.day))
    expect(register_page.select_month).to_have_value(str(user.birth_date.month))
    expect(register_page.select_year).to_have_value(str(user.birth_date.year))
    expect(register_page.email).to_have_value(user.email)
    expect(register_page.company_name).to_have_value(user.company)
    expect(register_page.newsletter).not_to_be_checked()

def test_user_registration_fails_with_mismatched_passwords():
    pass

# @pytest.mark.parametrize()
def test_user_registration_fails_with_missing_required_fields():
    pass



