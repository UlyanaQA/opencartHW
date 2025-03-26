from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderElement(BasePage):
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")
    POUND = (By.CSS_SELECTOR, "a[href='GBP']")
    USD = (By.CSS_SELECTOR, "a[href='USD']")
    CURRENCY_SIGN = (By.CSS_SELECTOR, ".dropdown>a>strong")

    def header_switch_currency(self, currency_code):
        self.log_action(f"Переключение валюты на {currency_code}")
        currency_dropdown = self.wait_for_element_visible(self.CURRENCY)
        currency_dropdown.click()
        currency_item_locator = (By.CSS_SELECTOR, f"a[href='{currency_code}']")
        currency_item = self.wait_for_element_visible(currency_item_locator)
        currency_item.click()
        currency_sign_element = self.wait_for_element_visible(self.CURRENCY_SIGN)
        return currency_sign_element.text.strip()
