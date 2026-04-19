from playwright.sync_api import Page, expect
from fixtures.api_fixtures import api_auth
from pages.my_account_addresses import AddressesPage
from utils.helpers import generate_user_registration_data, generate_address_data


def test_add_new_first_address(api_auth: Page):
    user = generate_user_registration_data()
    address_data = generate_address_data()

    page = api_auth


    page.my_account.addresses.goto()
    page.my_account.addresses.wait_to_load()

    page.my_account.addresses.goto_add_new()


    page.my_account.add_address.fill_address_details(
        user.first_name, user.last_name, user.email, address_data.city,
        address_data.street, address_data.zip, user.phone
    )

    expect(page.locator("body")).to_contain_text("Email: bob.smith@yopmail.com")
    expect(page.locator("body")).to_contain_text("Phone number: 4088126543")
    page.get_by_text("Escuela Ave.").click()
    expect(page.locator("body")).to_contain_text("333 Escuela Ave.")
    expect(page.locator("body")).to_contain_text("Mountain View, California, 94040")
    expect(page.locator("body")).to_contain_text("United States of America")


