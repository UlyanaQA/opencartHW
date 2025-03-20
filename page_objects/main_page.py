from selenium.webdriver.common.by import By
from .base_page import BasePage


class MainPage(BasePage):
    SEARCH_BUTTON = (By.CSS_SELECTOR, "#search button")
    TOP_NAVIGATION = (By.CSS_SELECTOR, "#top .float-end ul")
    CURRENCY_LIST = (By.CSS_SELECTOR, "#form-currency")
    MENU = (By.CSS_SELECTOR, "ul.nav.navbar-nav > li")
    GOODS_CARDS = (By.CSS_SELECTOR, "footer h5")
    PRODUCT_TITLE = (By.CSS_SELECTOR, ".product-thumb .content .description h4 a")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "button[formaction*='cart.add']")
    CART_BUTTON = (By.XPATH, '//*[@id="header-cart"]/div/button')
    SUCCESS_ALERT = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    CURRENCY_SWITCHER = (By.CSS_SELECTOR, "#form-currency")
    PRODUCT_PRICES = (By.XPATH, "//span[contains(text(), '{}')]")

    def is_search_button_present(self):
        return self.wait_for_element_present(self.SEARCH_BUTTON)

    def is_top_navigation_present(self):
        return self.wait_for_element_present(self.TOP_NAVIGATION)

    def is_currency_list_visible(self):
        return self.wait_for_element_visible(self.CURRENCY_LIST)

    def get_menu_items(self):
        return self.find_elements(self.MENU)

    def is_goods_cards_visible(self):
        return self.wait_for_element_visible(self.GOODS_CARDS)

    def add_product_to_cart(self):
        product_title = self.wait_for_element_visible(self.PRODUCT_TITLE)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", product_title)

        add_button = self.wait_for_element_visible(self.ADD_TO_CART_BUTTON)
        self.browser.execute_script("arguments[0].click();", add_button)

    def wait_for_success_alert_disappear(self):
        self.wait_for_invisibility_of_element(self.SUCCESS_ALERT)

    def get_cart_items_count_and_price(self):
        cart_button = self.wait_for_element_visible(self.CART_BUTTON)
        return cart_button.text

    def switch_currency(self, selected_currency):
        currency_switcher = self.wait_for_element_visible(self.CURRENCY_SWITCHER)
        currency_switcher.click()

        currency_choice = self.wait_for_element_visible(
            (By.CSS_SELECTOR, f"a[href='{selected_currency}']")
        )
        currency_choice.click()

    def get_product_prices(self, currency_symbol):
        prices_locator = (By.XPATH, f"//span[contains(text(), '{currency_symbol}')]")
        return self.find_elements(prices_locator)
