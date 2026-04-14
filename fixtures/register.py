import pytest
from playwright.sync_api import Page


@pytest.fixture
def register_page(page: Page):
    from pages.register_page import RegisterPage
    return RegisterPage(page)