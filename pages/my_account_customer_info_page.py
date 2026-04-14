from pages.base_page import BasePage
from playwright.sync_api import Page

from pages.forms.personal_details_form import PersonalDetailForm


class CustomerInfo(BasePage, PersonalDetailForm):
    def __init__(self, page: Page):
        super().__init__(page)
        PersonalDetailForm.__init__(self, page)

        self.path = "/customer/info"

        self.fld_company = page.get_by_role("textbox", name="Company name:")
        self.chk_newletter = page.get_by_role("checkbox", name="Newsletter:")
