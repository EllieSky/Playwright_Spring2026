import re
from operator import add
from os import wait

from playwright.sync_api import Page, expect


def test_basic_store_search(page: Page):
    search_keyword = "macbook"

    page.goto("https://nop-qa.portnov.com/")

    page.get_by_label("Search store").fill(search_keyword)
    page.get_by_role("button", name="Search").click()

    expect(page.url).to_contain_text(f"search?q={search_keyword}")

    expect(page.get_by_role("heading", level=1)).to_have_text("Search")
    (expect(page.get_by_role("heading", level=3)
            .get_by_role("link"))
     .to_contain_text(re.compile(search_keyword, re.IGNORECASE)))
    expect(page.get_by_role("heading", level=2).locator("a"))




