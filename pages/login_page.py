from playwright.sync_api import Page

from pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, page: Page):
        super().__init__(page)
        self.path = "/login"

        self.fld_email = page.get_by_label("Email:")
        self.fld_password = page.locator("input.password")
        self.btn_login = page.get_by_role('button', name="Log in")

    def authenticate(self, email: str, password: str) -> None:
        """Authenticate user with provided credentials."""
        self.fld_email.fill(email)
        self.fld_password.fill(password)  # Option 2
        self.btn_login.click()