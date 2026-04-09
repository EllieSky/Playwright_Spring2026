import pytest
from fixtures.new_user import get_shopper
import config


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    """Browser launch args from centralized config."""
    return config.get_browser_launch_options()

@pytest.fixture(scope="session")
def base_url() -> str:
    return config.get_base_url()

@pytest.fixture(scope="session")
def browser_context_args():
    return {
        'viewport': {'width': config.get_viewport_width(), 'height': config.get_viewport_height()},
    }
