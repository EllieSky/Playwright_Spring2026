import pytest
from playwright.sync_api import Page as PlaywrightPage, BrowserType

########################### DO NOT REMOVE #########################
# These imports are registering fixtures with playwright,
# even though they are not being used within this module
from fixtures.new_user import get_shopper
from fixtures.menu import menu
###########################  END  #################################


import config
from fixtures.extended_page import Page

@pytest.fixture(scope="session")
def browser_type(playwright):

    if config.get_browser_type().lower() == 'brave':
        return playwright.chromium

    return getattr(playwright, config.get_browser_type())


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    """Browser launch args from centralized config."""
    if config.get_browser_type().lower() == 'brave':
        return {
            **config.get_browser_launch_options(),
            "executable_path":"/Applications/Brave Browser.app/Contents/MacOS/Brave Browser"
        }
    return config.get_browser_launch_options()


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, playwright):
    mobile = config.get_mobile_device_type()
    browser = config.get_browser_type()

    is_device = playwright.devices.get(mobile, None)
    # is_device = playwright.devices[mobile]

    if is_device and not browser.lower() == 'firefox':
        return {
            **browser_context_args,
            **is_device

        }

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