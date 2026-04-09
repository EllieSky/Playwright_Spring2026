import re
from playwright.sync_api import Page, expect


def test_shoe_shopping(page: Page):
    page.goto("https://nop-qa.portnov.com/adidas-consortium-campus-80s-running-shoes")
    page.get_by_role('combobox').select_option('8')
    page.locator('.attribute-square').first.click()
    # page.locator("#product_attribute_9").select_option("21")
    # page.locator("li:nth-child(2) > label > .attribute-square-container > .attribute-square").click()

    page.get_by_role("textbox", name="Enter a quantity").fill("2")
    # page.get_by_role("button", name="Add to cart").click()
    page.locator("#add-to-cart-button-25").click()
    page.get_by_role("link", name="Shopping cart (2)").click()
    # page.locator("#shopping-cart-form").get_by_text("Size: 8Color: Blue").click()
    attributes_div = page.locator("#shopping-cart-form .attributes")
    raw_text = attributes_div.inner_text()

    # 3. Parse the text and store the values in a list
    extracted_values = []

    # Split the text into lines based on the newline character
    lines = raw_text.split('\n')

    for line in lines:
        if ':' in line:
            # Split by the colon, take the second part (the value), and strip extra spaces
            value = line.split(':')[1].strip()
            extracted_values.append(value)

    # print(extracted_values)
    # Output: ['8', 'Blue']

    # expect(extracted_values[0]).to_be('8')
    assert extracted_values[0] == "8"
    assert extracted_values[1] == "Red"

    # expect(extracted_values[1]).to_be('Blue')

    # page.get_by_role("row", name="Total: $165.36", exact=True).get_by_role("strong").click()
    # Expect a title "to contain" a substring.
    # 1. Locate the element
    total_locator = page.locator(".order-total .value-summary")

    # 2. Extract the text
    raw_text = total_locator.inner_text()
    # raw_text is now "$55.12"

    # 3. Clean the text and store it in a variable
    # Replace the dollar sign with nothing, and strip any accidental whitespace
    clean_total_string = raw_text.replace('$', '').strip()

    # Optional: Convert it to a float if you need to do math with it later
    total_value = float(clean_total_string)
    # expect(total_value).to_be(55.12)
    assert total_value == 55.12
    # print(total_value)
    # Output: 55.12
