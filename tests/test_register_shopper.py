from playwright.sync_api import Page, expect
from utils.helpers import generate_user_registration_data

def test_register_shopper(page: Page, menu, register_page):
    user = generate_user_registration_data()
    password = user.password

    page.goto("/")
    menu.user_menu.goto_register()

    register_page.fill_registration_details(user.first_name, user.last_name, user.email, password,
                                            gender=user.gender, birth_date=user.birth_date, company=user.company,
                                            newsletter=False, re_pw=password)

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



