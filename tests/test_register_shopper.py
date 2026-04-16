from playwright.sync_api import expect

from fixtures.menu import Menu
from fixtures.extended_page import Page
from utils.helpers import generate_user_registration_data


def test_register_shopper(page: Page, menu: Menu):
    user = generate_user_registration_data()

    page.goto("/")
    menu.user_menu.goto_register()

    page.register_page.fill_registration_details(
        user.first_name, user.last_name, user.email, user.password,
        gender='female', newsletter=False,
        company=user.company, birth_date=user.birth_date
    )

    # todo - make page for confirmation
    expect(page.get_by_text("Your registration completed")).to_be_visible()
    # top OR bottom expect, but NOT both
    expect(page.locator('.registration-result-page .result')).to_contain_text("Your registration completed")
    expect(page.get_by_role("link", name="Continue")).to_be_visible()

    # after clicking register
    menu.user_menu.goto_my_account()

    expect(page.my_account.customer_info_page.fld_first_name).to_have_value(user.first_name)
    expect(page.my_account.customer_info_page.fld_last_name).to_have_value(user.last_name)

    expect(page.my_account.customer_info_page.select_birth_day).to_have_value(str(user.birth_date.day))
    expect(page.my_account.customer_info_page.select_birth_month).to_have_value(str(user.birth_date.month))
    expect(page.my_account.customer_info_page.select_birth_year).to_have_value(str(user.birth_date.year))
    expect(page.my_account.customer_info_page.fld_email).to_have_value(user.email)
    expect(page.my_account.customer_info_page.fld_company).to_have_value(user.company)
    expect(page.my_account.customer_info_page.chk_newletter).not_to_be_checked()

def test_user_registration_fails_with_mismatched_passwords():
    pass

# @pytest.mark.parametrize()
def test_user_registration_fails_with_missing_required_fields():
    pass



