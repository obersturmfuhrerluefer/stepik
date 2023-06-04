python
import time


def test_add_to_cart_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    add_to_cart_button = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert add_to_cart_button.is_displayed(), "Add to cart button is not displayed"
