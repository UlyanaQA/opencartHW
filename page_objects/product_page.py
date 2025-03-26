import allure
from selenium.common import TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    NEW_PRICE = (By.CSS_SELECTOR, "span.price-new")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[formaction$='wishlist.add']")
    ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, "button[formaction$='compare.add']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_PHOTO = (By.CSS_SELECTOR, ".image.magnific-popup")

    @allure.step("Проверка наличия новой цены")
    def is_new_price_present(self):
        self.log_action("Проверка наличия новой цены")
        try:
            self.wait_for_element_present(self.NEW_PRICE)
            self.log_action("Новая цена найдена")
            return True
        except TimeoutException:
            self.log_action("Новая цена не найдена")
            return False

    @allure.step("Проверка наличия кнопки 'Добавить в избранное'")
    def is_add_to_wishlist_button_present(self):
        self.log_action("Проверка наличия кнопки 'Добавить в избранное'")
        try:
            self.wait_for_element_present(self.ADD_TO_WISHLIST_BUTTON)
            self.log_action("Кнопка 'Добавить в избранное' найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка 'Добавить в избранное' не найдена")
            return False

    @allure.step("Проверка наличия кнопки 'Добавить к сравнению'")
    def is_add_to_compare_button_present(self):
        self.log_action("Проверка наличия кнопки 'Добавить к сравнению'")
        try:
            self.wait_for_element_present(self.ADD_TO_COMPARE_BUTTON)
            self.log_action("Кнопка 'Добавить к сравнению' найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка 'Добавить к сравнению' не найдена")
            return False

    @allure.step("Проверка наличия кнопки 'Добавить в корзину'")
    def is_add_to_cart_button_present(self):
        self.log_action("Проверка наличия кнопки 'Add to Cart'")
        try:
            self.wait_for_element_present(self.ADD_TO_CART_BUTTON)
            self.log_action("Кнопка 'Добавить в корзину' найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка 'Добавить в корзину' не найдена")
            return False

    @allure.step("Проверка наличия фото продукта")
    def is_product_photo_present(self):
        self.log_action("Проверка наличия фото продукта")
        try:
            self.wait_for_element_present(self.PRODUCT_PHOTO)
            self.log_action("Фото продукта найдено")
            return True
        except TimeoutException:
            self.log_action("Фото продукта не найдено")
            return False
