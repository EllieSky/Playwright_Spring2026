import os
import pytest
import config
from fixture.create_user import get_shopper

'''def get_base_url()
    return os.getenv('BASE_URL').lower()
'''


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args, base_url) -> dict:
    return {
        **browser_context_args,
        "base_url": base_url,
        'viewport': {
            'width': config.get_browser_context_options()['viewport']['width'],
            'height': config.get_browser_context_options()['viewport']['height'],

        }
    }



@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    """Browser launch args from centralized config."""
    return config.get_browser_launch_options()


@pytest.fixture(scope="session")
def base_url() -> str:
    return config.get_base_url()

