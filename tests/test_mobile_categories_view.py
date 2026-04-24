import pytest
from playwright.sync_api import Page, expect
# from playwright.async_api import Page, expect


@pytest.mark.mobile
def test_categories_on_mobile(page: Page):
    page.goto("/")
    header_menu = page.locator(".header-menu")
    # if header_menu.locator('.menu-toggle').is_visible():
    #     header_menu.locator('.menu-toggle').click()    # if header_menu.locator('.menu-toggle').is_visible():
    header_menu.locator('.menu-toggle').click()
    expect(header_menu.get_by_role('link', name='Computers')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Electronics')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Apparel')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Digital downloads')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Books')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Jewelry')).to_be_visible()
    expect(header_menu.get_by_role('link', name='Gift Cards')).to_be_visible()

    header_menu.get_by_role('link', name='Electronics').click()
    expect(page.get_by_role('heading', level=1)).to_have_text('Electronics')


def test_categories_on_desktop(page: Page, menu):
    page.goto("/")
    header_menu = page.locator(".header-menu")

    for item in menu.header_menu.categories:
        expect(header_menu.get_by_role('link', name=item)).to_be_visible()

    header_menu.get_by_role('link', name='Electronics').click()
    expect(page.get_by_role('heading', level=1)).to_have_text('Electronics')


