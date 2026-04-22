from playwright.sync_api import Page

from pages.forms.base_page import BasePage


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/register"

        # locators
        self.radio_btn_male = page.locator("#gender-male")
        self.fld_first_name = page.locator("#FirstName")
        self.fld_last_name = page.locator("#LastName")
        self.fld_birthday_day = page.locator("select[name=\"DateOfBirthDay\"]")
        self.fld_birthday_month = page.locator("select[name=\"DateOfBirthMonth\"]")
        self.fld_birthday_year =page.locator("select[name=\"DateOfBirthYear\"]")

        self.fld_email = page.locator("#Email")
        self.fld_company = page.locator("#Company")
        self.check_box_newsletter = page.locator("#Newsletter")
        self.fld_password = page.locator("#Password")
        self.fld_password_confirm = page.locator("#ConfirmPassword")

        self.btn_register = page.get_by_role("button", name="Register")

        # functions
    def register_user_required_fields(self, first_name, last_name, email, password):

        self.fld_first_name.fill(first_name)
        self.fld_last_name.fill(last_name)
        self.fld_email.fill(email)
        self.fld_password.fill(password)
        self.fld_password_confirm.fill(password)
        self.btn_register.click()