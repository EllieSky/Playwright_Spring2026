import re
from playwright.sync_api import Page, expect


def test_has_title(page: Page):
    page.goto("https://nop-qa.portnov.com")

    # # Expect a title "to contain" a substring.
    # expect(page).to_have_title(re.compile("Playwright"))
    #
    # # Click the get started link.
    # page.get_by_role("link", name="Get started").click()
    #
    # # Expects page to have a heading with the name of Installation.
    # expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    # new tests from Day 15 class
    page.get_by_label("Search store").click()
    page.get_by_label("Search store").fill("macbook")
    page.get_by_role("button", name="Search").click()

    search_keyword = "macbook"
    # expect(page).to_have_url(re.compile(f".*search?q={search_keyword}")) - to treat ? with regex
    expect(page).to_have_url(re.compile(f".*search\?q={search_keyword}"))

    # Create assertions
    # expect(page).to_have_heading("Search")
    expect(page.get_by_role("heading", level = 1)).to_contain_text("Search")


    # expect to see MacBook at the Search page, but ignore case
    expect(page.get_by_role("heading", level=2)
           .get_by_role("link")).to_contain_text(re.compile("macbook", re.IGNORECASE))




