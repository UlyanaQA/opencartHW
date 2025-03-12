from page_objects.base_page import BasePage
from selenium.webdriver.common.by import By


class HeaderElement(BasePage):
    CURRENCY = (By.CSS_SELECTOR, "form>.dropdown>a>.d-none.d-md-inline")
    EURO = (By.CSS_SELECTOR, "a[href='EUR']")
    POUND = (By.CSS_SELECTOR, "a[href='GBP']")
    USD = (By.CSS_SELECTOR, "a[href='USD']")
    CURRENCY_SIGN = (By.CSS_SELECTOR, ".dropdown>a>strong")

    def header_switch_currency(self, currency_code):
        self.wait_for_element_present(self.CURRENCY).click()

        # Динамически формируем локатор для выбранной валюты
        currency_item_locator = (By.CSS_SELECTOR, f"a[href='{currency_code}']")
        self.wait_for_element_present(currency_item_locator).click()
        return self.get_text(self.CURRENCY_SIGN)
