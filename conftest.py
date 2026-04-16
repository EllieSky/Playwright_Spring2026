import pytest
from playwright.sync_api import Page as PlaywrightPage

########################### DO NOT REMOVE #########################
# These imports are registering fixtures with playwright,
# even though they are not being used within this module
from fixtures.new_user import get_shopper
from fixtures.menu import menu
###########################  END  #################################


import config
from fixtures.extended_page import Page


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


@pytest.fixture
def page(page: PlaywrightPage) -> Page:
    """Returns a typed Page wrapper with page objects for IDE autocomplete."""
    return Page(page)