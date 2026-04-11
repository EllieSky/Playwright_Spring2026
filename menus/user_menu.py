from playwright.sync_api import Page

class UserMenu:
    def __init__(self, page):
        super().__init__(page)
        self.page = page
        self.link_register =  page.get_by_role("link", name="Register")
        self.link_login =   page.get_by_role("link", name="Log in")
        self.link_wishlist =   page.get_by_role("link", name="Wishlist (0)")
        self.link_shopping_cart = page.get_by_role("link", name="Shopping cart (0)")
        self.fld_search_store = page.get_by_role("textbox", name="Search store")
        self.btn_search =  page.get_by_role("button", name="Search")
        self.link_myaccount = page.get_by_role("link", name="My account")
        self.link_logout = page.get_by_role("link", name="Log out")

    def goto_login(self):
        self.link_login.click()
        self.page.wait_for_load_state('networkidle')

    def goto_register(self):
        self.link_register.click()
        self.page.wait_for_load_state('networkidle')

    def goto_wishlist(self):
        self.link_wishlist.click()
        self.page.wait_for_load_state('networkidle')

    def goto_myaccount(self):
        self.link_myaccount.click()
        self.page.wait_for_load_state('networkidle')

    def goto_logout(self):
        self.link_logout.click()
        self.page.wait_for_load_state('networkidle')


