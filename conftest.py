from dataclasses import dataclass

import pytest
from playwright.sync_api import Page

########################### DO NOT REMOVE #########################
# These imports are registering fixtures with playwright,
# even though they are not being used within this module
from fixtures.new_user import get_shopper
from fixtures.menu import menu
###########################  END  #################################


import config
from pages.login_page import LoginPage
from pages.my_account_customer_info_page import CustomerInfo
from pages.register_page import RegisterPage


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    """Browser launch args from centralized config."""
    return config.get_browser_launch_options()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        'viewport': {
            'width': config.get_browser_context_options()['viewport']['width'],
            'height': config.get_browser_context_options()['viewport']['height'],
        }
    }


@pytest.fixture(scope="session")
def base_url() -> str:
    return config.get_base_url()


@dataclass
class MyAccount:
    customer_info_page: CustomerInfo
    # orders_page: OrdersPage
    # change_password_page: ChangePasswordPage


@pytest.fixture
def page(page: Page):
    page.login_page = LoginPage(page)
    page.register_page = RegisterPage(page)
    # page.customer_info_page = CustomerInfo(page)
    page.my_account = MyAccount(
        CustomerInfo(page),
        # OrdersPage(page),
        # ChangePasswordPage(page)
    )

    return page