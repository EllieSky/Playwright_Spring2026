import re
from playwright.sync_api import Page, expect

#page is fixture defaults and helps in browser chrome
def test_has_title(page: Page):
    search_keyword = "macbook"
    page.goto("https://nop-qa.portnov.com/")

    page.get_by_label("Search store").click()
    page.get_by_label("Search store").fill(search_keyword)

    page.get_by_role("button", name="Search").click()


    expect(page.url).to_contain_text(f"search?q={search_keyword}")

    # Expect a title "to contain" a substring.
    #expect(page).to_have_title(re.compile("Playwright"))
    #except(page).to_have_heading(re.compile("Playwright")
    #<h1>

    expect(page.get_by_role("heading", level=1)).to_have_text("Search")



    #expect(page).to_have_title(re.compile("Playwright"))
    #<h2>
    expect(page.get_by_role("heading", level=3).get_by_role("link")).to_contain_text(search_keyword ,re.IGNORECASE)
    expect(page.get_by_role("heading", level=2).locator("a"))


