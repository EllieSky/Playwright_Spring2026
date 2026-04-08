import pytest

import config


@pytest.fixture(scope="session")
def browser_type_launch_args() -> dict:
    """Browser launch args from centralized config."""
    return config.get_browser_launch_options()

@pytest.fixture(scope="session")
def base_url() -> str:
    return config.get_base_url()
