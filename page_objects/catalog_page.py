from .base_page import BasePage
from selenium.webdriver.common.by import By


class CatalogPage(BasePage):
    SORT_LIST = (By.CSS_SELECTOR, "#input-sort")
    COMPARE_BUTTON = (By.CSS_SELECTOR, "#compare-total")
    HOME_BUTTON = (By.CSS_SELECTOR, "#product-category > ul > li:nth-child(1)")
    LEFT_MENU = (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3")
    LAPTOP_CATEGORY_LINKS = (
        By.CSS_SELECTOR,
        "div.list-group.mb-3 > a[href*='laptop-notebook/']",
    )
    CURRENCY_SWITCHER = (By.CSS_SELECTOR, "#form-currency")
    DESKTOPS_PRICES = (By.XPATH, "//div[@class='price']")
    PRODUCT_CATEGORY = (By.ID, "product-category")

    def open_catalog_page(self, category_url):
        self.open(category_url)

    def is_sort_list_present(self):
        return self.wait_for_element_present(self.SORT_LIST)

    def is_compare_button_present(self):
        return self.wait_for_element_present(self.COMPARE_BUTTON)

    def is_home_button_present(self):
        return self.wait_for_element_present(self.HOME_BUTTON)

    def is_left_menu_present(self):
        return self.wait_for_element_present(self.LEFT_MENU)

    def get_laptop_category_links(self):
        return self.find_elements(self.LAPTOP_CATEGORY_LINKS)

    def switch_currency(self, selected_currency):
        currency_switcher = self.wait_for_element_visible(self.CURRENCY_SWITCHER)
        currency_switcher.click()

        currency_choice = self.wait_for_element_visible(
            (By.CSS_SELECTOR, f"a[href='{selected_currency}']")
        )
        currency_choice.click()

    def wait_for_product_category(self):
        return self.wait_for_element_visible(self.PRODUCT_CATEGORY)

    def get_desktops_prices(self):
        return self.find_elements(self.DESKTOPS_PRICES)
