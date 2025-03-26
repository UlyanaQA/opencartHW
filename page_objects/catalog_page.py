from selenium.common import TimeoutException

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
        self.log_action(f"Открытие страницы каталога: {category_url}")
        self.open(category_url)

    def is_sort_list_present(self):
        self.log_action("Проверка наличия поля сортировки")
        try:
            self.wait_for_element_present(self.SORT_LIST)
            self.log_action("Поле сортировки найдено")
            return True
        except TimeoutException:
            self.log_action("Поле сортировки не найдено")
            return False

    def is_compare_button_present(self):
        self.log_action("Проверка наличия кнопки сравнения")
        try:
            self.wait_for_element_present(self.COMPARE_BUTTON)
            self.log_action("Кнопка сравнения найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка сравнения не найдена")
            return False

    def is_home_button_present(self):
        self.log_action("Проверка наличия кнопки домой")
        try:
            self.wait_for_element_present(self.HOME_BUTTON)
            self.log_action("Кнопка домой найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка домой не найдена")
            return False

    def is_left_menu_present(self):
        self.log_action("Проверка наличия левого меню")
        try:
            self.wait_for_element_present(self.LEFT_MENU)
            self.log_action("Левое меню найдено")
            return True
        except TimeoutException:
            self.log_action("Левое меню не найдено")
            return False

    def get_laptop_category_links(self):
        self.log_action("Получение ссылок на категории ноутбуков")
        return self.find_elements(self.LAPTOP_CATEGORY_LINKS)

    def switch_currency(self, selected_currency):
        self.log_action(f"Переключение валюты на {selected_currency}")
        currency_switcher = self.wait_for_element_visible(self.CURRENCY_SWITCHER)
        currency_switcher.click()

        currency_choice = self.wait_for_element_visible(
            (By.CSS_SELECTOR, f"a[href='{selected_currency}']")
        )
        currency_choice.click()

    def wait_for_product_category(self):
        self.log_action("Ожидание загрузки категории товаров")
        try:
            self.wait_for_element_visible(self.PRODUCT_CATEGORY)
            self.log_action("Страница категории товаров успешно загружена")
            return True
        except TimeoutException:
            self.log_action("Страница категории товаров не загрузилась")
            return False

    def get_desktops_prices(self):
        self.log_action("Получение цен на компьютеры")
        return self.find_elements(self.DESKTOPS_PRICES)
