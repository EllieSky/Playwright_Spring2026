import pytest
from playwright.sync_api import Page, expect
@pytest.mark.parametrize ("shoe_size, shoe_color, expected_price",
                              [
                                  (10, "Red", "$27.56"),
                                  (9, "Blue", "$27.56"),
                                  (11, "Silver", "$27.56")
                              ]
                              )


def test_shoe_size_color_price(page: Page, shoe_size, shoe_color, expected_price):
    page.goto("https://nop-qa.portnov.com/adidas-consortium-campus-80s-running-shoes")


    shoe_name = "AD_C80_RS"

    # Select Shoe Size
    size_value_map = {9: "22", 10: "23", 11: "24"}
    page.locator("#product_attribute_9").select_option(size_value_map[shoe_size])


    # select shor color
    page.locator("span.attribute-square")


    # Click Add To Cart
    page.locator("#add-to-cart-button-25").click()

    # Wait for confirmation that item is added
    page.locator(".bar-notification.success").wait_for(state="visible")

    # Click shopping cart
    page.get_by_role("link", name="shopping cart", exact=True).click()

    #Validation
    '''
    page.locator('.header-links .ico-account').click()
    expect(page.get_by_role("textbox", name ="First name:")).to_have_value(user.first_name)
    '''
    expect(page.locator(".sku-number")).to_have_text(shoe_name)
    attributes = page.locator("#shopping-cart-form div.attributes")
    page.wait_for_timeout(1000)
    expect(attributes).to_contain_text(str(shoe_size))
    expect(attributes).to_contain_text(str(shoe_color))
    expect(page.locator(".qty-input")).to_have_value("1")

   # Validate total price in cart
    total_price_locator = page.locator("td.subtotal span.product-subtotal")
    total_price_text = total_price_locator.text_content().strip()
    assert total_price_text == "$27.56", f"Expected total price $27.56 but got {total_price_text}"