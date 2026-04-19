from playwright.sync_api import Page
from pages.base_page import BasePage


class AddAddressPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/customer/addressadd"

        self.fld_first_name = page.get_by_role("textbox", name="First name:")
        self.fld_last_name = page.get_by_role("textbox", name="Last name:")
        self.fld_email = page.get_by_role("textbox", name="Email:")
        self.fld_street = page.get_by_role("textbox", name="Address 1:")
        self.fld_city = page.get_by_role("textbox", name="City:")
        self.fld_zipcode = page.get_by_role("textbox", name="Zip / postal code:")
        self.phone_number = page.get_by_role("textbox", name="Phone number:")
        self.btn_save = page.get_by_role("button", name="Save")



    def fill_address_details(self, first_name, last_name, email, city, street, zipcode, phone):
        self.fld_first_name.fill(first_name)
        self.fld_last_name.fill(last_name)
        self.fld_email.fill(email)
        self.page.get_by_label("Country:").select_option("237")  # United States of America
        self.page.get_by_label("State / province:").select_option("1677")  # CA
        self.fld_city.fill(city)
        self.fld_street.fill(street)
        self.fld_zipcode.fill(zipcode)
        self.phone_number.fill(phone)
        self.btn_save.click()