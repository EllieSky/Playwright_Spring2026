import pytest
from dataclasses import dataclass
from playwright.sync_api import Page, expect

from menus.user_menu import UserMenu


@dataclass
class Menu:
    user_menu: UserMenu

@pytest.fixture
def menu(page: Page):
    return Menu(
        UserMenu(page)
    )