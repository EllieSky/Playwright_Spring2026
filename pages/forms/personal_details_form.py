from playwright.sync_api import Page, expect

class PersonalDetailsForm:
    def __init__(self, page: Page):
        self.select_gender_female = page.get_by_text("Female", exact=True)
        self.select_gender_male = page.get_by_text("Male", exact=True)

        self.select_day = page.get_by_role('combobox').filter(has_text='Day')
        self.select_month = page.get_by_role('combobox').filter(has_text='Month')
        self.select_year = page.get_by_role('combobox').filter(has_text='Year')

        self.first_name = page.get_by_role("textbox", name="First name:")
        self.last_name = page.get_by_role("textbox", name="Last name:")
        self.email = page.get_by_role("textbox", name="Email:")