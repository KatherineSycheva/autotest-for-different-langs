link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_basket_button_is_exist(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector("#add_to_basket_form > button")
    print(button.text)
    assert button is not None, "Button not found!"
