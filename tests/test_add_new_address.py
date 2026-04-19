from playwright.sync_api import expect
from fixtures.extended_page import Page
from fixtures.api_fixtures import api_auth
from utils.helpers import generate_user_registration_data, generate_address_data


def test_add_new_first_address(api_auth: Page):
    user = generate_user_registration_data()
    address_data = generate_address_data()

    page = api_auth


    page.my_account.addresses_page.goto()
    page.my_account.addresses_page.wait_to_load()

    page.my_account.addresses_page.goto_add_new()


    page.my_account.add_address_page.fill_address_details(
        user.first_name, user.last_name, user.email, address_data.city,
        address_data.street, address_data.zip, user.phone
    )

    expect(page.my_account.addresses_page.li_email.last).to_contain_text(f"Email: {user.email}")
    expect(page.my_account.addresses_page.li_phone_number.last).to_contain_text(f"Phone number: {user.phone}")
    expect(page.my_account.addresses_page.li_city_state_zip.last).to_contain_text(f"{address_data.city}, {address_data.state}, {address_data.zip}")
    expect(page.my_account.addresses_page.li_name.last).to_contain_text(f"{user.first_name} {user.last_name}")
