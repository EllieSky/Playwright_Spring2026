from playwright.sync_api import Page, expect

class HeaderMenu:

    def __init__(self, page: Page):
        self.page = page
        self.header_menu = page.locator(".header-menu")
        self.menu_toggle = self.header_menu.locator('.menu-toggle')
        self.link_computers = self.header_menu.get_by_role('link', name='Computers')
        self.link_electronics = self.header_menu.get_by_role('link', name='Electronics')
        self.link_apparel = self.header_menu.get_by_role('link', name='Apparel')
        self.link_digital_downloads = self.header_menu.get_by_role('link', name='Digital downloads')
        self.link_books = self.header_menu.get_by_role('link', name='Books')
        self.link_jewelry = self.header_menu.get_by_role('link', name='Jewelry')
        self.link_gift_cards = self.header_menu.get_by_role('link', name='Gift Cards')

    @property
    def categories(self):
        """Return the set of available category names"""
        return {
            'Computers',
            'Electronics',
            'Apparel',
            'Digital downloads',
            'Books',
            'Jewelry',
            'Gift Cards'
        }

    def toggle_menu(self):
        """Click the menu toggle button (for mobile view)"""
        self.menu_toggle.click()
        self.page.wait_for_load_state("networkidle")

    def goto_computers(self):
        self.link_computers.click()
        self.page.wait_for_load_state("networkidle")

    def goto_electronics(self):
        self.link_electronics.click()
        self.page.wait_for_load_state("networkidle")

    def goto_apparel(self):
        self.link_apparel.click()
        self.page.wait_for_load_state("networkidle")

    def goto_digital_downloads(self):
        self.link_digital_downloads.click()
        self.page.wait_for_load_state("networkidle")

    def goto_books(self):
        self.link_books.click()
        self.page.wait_for_load_state("networkidle")

    def goto_jewelry(self):
        self.link_jewelry.click()
        self.page.wait_for_load_state("networkidle")

    def goto_gift_cards(self):
        self.link_gift_cards.click()
        self.page.wait_for_load_state("networkidle")
