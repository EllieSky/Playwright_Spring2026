from pages.base_page import BasePage
from playwright.sync_api import Page

class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/register"

        self.select_gender_f =  page.get_by_text("Female")
        self.select_gender_m =  page.get_by_text("Male")

        self.select_date =  page.get_by_role('combobox').filter(has_text='Day')
        self.select_month = page.get_by_role('combobox').filter(has_text='Year')
        self.select_year = page.get_by_role('combobox').filter(has_text='Year')


        self.first_name =  page.get_by_role("textbox", name="First name:")
        self.last_name = page.get_by_role("textbox", name="Last name:")
        self.email =  page.get_by_role("textbox", name="Email:")

        self.company_name =  page.get_by_role("textbox", name="Company name:")

        self.newsletter = page.get_by_role("checkbox", name="Newsletter:")
        self.password = page.get_by_role("textbox", name="Password:", exact=True)
        self.confirm_password = page.get_by_role("textbox", name="Confirm password:")

        self.register_button = page.get_by_role("button", name="Register")

        self.registration_completed_msg_box = page.get_by_text("Your registration completed")

        self.registration_completed_msg = page.locator('.registration-result-page .result')

        self.continue_link = page.get_by_role("link", name="Continue")



