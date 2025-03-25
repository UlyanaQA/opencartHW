import time

import allure
from selenium.common import TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By


class AdministrationPage(BasePage):
    CATALOG = (By.CSS_SELECTOR, "#menu-catalog>a")
    PRODUCTS = (By.CSS_SELECTOR, "#collapse-1>li:nth-child(2)")
    ADD_NEW_PRODUCT = (By.CSS_SELECTOR, ".float-end>.btn.btn-primary")
    PRODUCT_NAME = (By.ID, "input-name-1")
    META_TAG_TITLE = (By.ID, "input-meta-title-1")
    DATA_TAB = (By.CSS_SELECTOR, ".nav.nav-tabs>.nav-item:nth-child(2)")
    MODEL = (By.ID, "input-model")
    SEO_TAB = (By.CSS_SELECTOR, ".nav.nav-tabs>.nav-item:nth-child(11)")
    KEYWORD = (By.ID, "input-keyword-0-1")
    SAVE_BTN = (By.CSS_SELECTOR, ".float-end>.btn.btn-primary")
    FILTER_NAME_PRODUCT = (By.CSS_SELECTOR, ".mb-3>#input-name")
    FILTER_BTN = (By.CSS_SELECTOR, ".text-end>#button-filter")
    CHECKBOX_PRODUCT = (By.CSS_SELECTOR, "tbody>tr>td>input.form-check-input")
    DELETE_BTN = (By.CSS_SELECTOR, ".btn.btn-danger")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @allure.step("Переход на страницу продуктов")
    def administration_go_to_product_page(self):
        self.log_action("Переход на страницу Catalog -> Products")
        self.wait_for_element_visible(self.CATALOG).click()
        self.wait_for_element_visible(self.PRODUCTS).click()

    @allure.step("Клик по кнопке добавления новго продукта")
    def products_click_add_new_product(self):
        self.log_action("Клик по кнопке 'Add new'")
        self.wait_for_element_visible(self.ADD_NEW_PRODUCT).click()

    @allure.step("Создание нового продукта")
    def products_add_new_product(self, product_name, meta_tag, model, keyword):
        self.log_action(f"Создание продукта: {product_name}")
        self.fill_field(self.PRODUCT_NAME, product_name)
        self.fill_field(self.META_TAG_TITLE, meta_tag)
        self.wait_for_element_visible(self.DATA_TAB).click()
        self.fill_field(self.MODEL, model)
        self.wait_for_element_visible(self.SEO_TAB).click()
        self.fill_field(self.KEYWORD, keyword)
        self.wait_for_element_visible(self.SAVE_BTN).click()

    @allure.step("Поиск продукта по названию")
    def find_product_by_name(self, product_name):
        self.log_action(f"Поиск продукта: {product_name}")

        self.fill_field(self.FILTER_NAME_PRODUCT, "")
        time.sleep(0.5)  # Ждем очистки

        self.fill_field(self.FILTER_NAME_PRODUCT, product_name)
        self.wait_for_element_visible(self.FILTER_BTN).click()

        product_locator = (By.XPATH, f"//td[text()='{product_name}']")
        try:
            element = self.wait_for_element_visible(product_locator, timeout=5)
            self.log_action(f"Продукт найден: {product_name}")
            return element.text()
        except TimeoutException:
            self.log_action(f"Продукт '{product_name}' не найден")
            return None

    @allure.step("Клик по чекбоксу для выбора продукта")
    def products_select_check_box(self):
        self.log_action("Выбор чекбокса для удаления продукта")
        self.wait_for_element_visible(self.CHECKBOX_PRODUCT).click()

    @allure.step("Удаление продукта")
    def products_delete_product(self):
        self.log_action("Удаление выбранного продукта")
        self.wait_for_element_visible(self.DELETE_BTN).click()
        self.browser.switch_to.alert.accept()
        self.wait_for_element_visible(
            (By.CSS_SELECTOR, "#form-product tbody tr td"), timeout=5
        )

    @allure.step("Проверка отсутствия продукта")
    def check_product_absence(self, product_name):
        self.log_action(f"Проверка отсутствия продукта: {product_name}")
        self.fill_field(self.FILTER_NAME_PRODUCT, product_name)
        self.wait_for_element_visible(self.FILTER_BTN).click()
        product_locator = (By.XPATH, f"//td[text()='{product_name}']")
        try:
            self.wait_for_invisibility_of_element(product_locator, timeout=5)
            return True
        except TimeoutException:
            return False
