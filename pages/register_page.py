import datetime
from pages.base_page import BasePage
from playwright.sync_api import Page
from pages.forms.personal_details_form import PersonalDetailsForm


class RegisterPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/register"

        personal = PersonalDetailsForm(page)
        self.first_name = personal.first_name
        self.last_name = personal.last_name
        self.email = personal.email
        self.select_gender_male = personal.select_gender_male
        self.select_gender_female = personal.select_gender_female
        self.select_day = personal.select_day
        self.select_month = personal.select_month
        self.select_year = personal.select_year

        self.company_name = page.get_by_role("textbox", name="Company name:")

        self.newsletter = page.get_by_role("checkbox", name="Newsletter:")

        self.password = page.get_by_role("textbox", name="Password:", exact=True)
        self.confirm_password = page.get_by_role("textbox", name="Confirm password:")

        self.register_button = page.get_by_role("button", name="Register")

        self.registration_completed_msg_box = page.get_by_text("Your registration completed")

        self.registration_completed_msg = page.locator('.registration-result-page .result')

        self.continue_link = page.get_by_role("link", name="Continue")

    def fill_registration_details(self, first_name, last_name, email, password, gender=None, birth_date: datetime.date=None, company=None, newsletter=True, re_pw = None  ):

        if gender.lower() == 'female':
            self.select_gender_female.click()
        else:
            self.select_gender_male.click()

        self.first_name.fill(first_name)
        self.last_name.fill(last_name)

        if birth_date:
            self.select_day.select_option(str(birth_date.day))
            self.select_month.select_option(str(birth_date.month))
            self.select_year.select_option(str(birth_date.year))

        self.email.fill(email)
        self.company_name.fill(company)

        if self.newsletter.is_checked() and newsletter is False:
            self.newsletter.uncheck()
        elif not self.newsletter.is_checked() and newsletter is True:
            self.newsletter.check()

        self.password.fill(password)
        re_pw = password if re_pw is None else re_pw
        self.confirm_password.fill(re_pw)

        self.register_button.click()

        return self.registration_completed_msg_box.is_visible()






