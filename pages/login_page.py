from playwright.sync_api import Page

from pages.forms.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"

        self.fld_email = page.get_by_role('textbox', name='Email')
        self.fld_password = page.get_by_role('textbox', name='Password')
        self.btn_login = page.get_by_role('button', name='Log in')

    def authenticate(self, email, password):
        self.fld_email.fill(email)
        self.fld_password.fill(password)
        self.btn_login.click()