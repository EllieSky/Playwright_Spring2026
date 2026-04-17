from playwright.sync_api import Page, expect

def add_new_first_address(api_auth):
    page = api_auth # api auth handing over the page
    page.goto("/")
    pass