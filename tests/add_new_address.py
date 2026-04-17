from playwright.sync_api import Page, expect
from fixtures.api_fixtures import api_auth


def test_add_new_first_address(api_auth):
    page = api_auth
    page.goto("/")
    pass

