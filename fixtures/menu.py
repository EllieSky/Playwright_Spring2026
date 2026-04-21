from dataclasses import dataclass

import pytest
from playwright.sync_api import Page

from menus.header_menu import HeaderMenu
from menus.user_menu import UserMenu


@dataclass
class Menu:
    user_menu: UserMenu
    header_menu: HeaderMenu



@pytest.fixture
def menu(page: Page):
    return Menu(
        UserMenu(page),
        HeaderMenu(page)
    )