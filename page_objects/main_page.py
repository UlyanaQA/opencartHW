import allure
from selenium.common import TimeoutException
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

    @allure.step("Проверка наличия кнопки поиска")
    def is_search_button_present(self):
        self.log_action("Проверка наличия кнопки поиска")
        try:
            self.wait_for_element_present(self.SEARCH_BUTTON)
            self.log_action("Кнопка поиска найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка поиска не найдена")
            return False

    @allure.step("Проверка наличия верхней навигации")
    def is_top_navigation_present(self):
        self.log_action("Проверка наличия верхней навигации")
        try:
            self.wait_for_element_present(self.TOP_NAVIGATION)
            self.log_action("Верхняя навигация найдена")
            return True
        except TimeoutException:
            self.log_action("Верхняя навигация не найдена")
            return False

    @allure.step("Проверка видимости списка валют")
    def is_currency_list_visible(self):
        self.log_action("Проверка видимости списка валют")
        try:
            self.wait_for_element_visible(self.CURRENCY_LIST)
            self.log_action("Список валют видим")
            return True
        except TimeoutException:
            self.log_action("Список валют не видим")
            return False

    @allure.step("Получение пунктов меню")
    def get_menu_items(self):
        self.log_action("Получение пунктов меню")
        return self.find_elements(self.MENU)

    @allure.step("Проверка видимости карточек товаров")
    def is_goods_cards_visible(self):
        self.log_action("Проверка видимости карточек товаров")
        try:
            self.wait_for_element_visible(self.GOODS_CARDS)
            self.log_action("Карточки товаров видимы")
            return True
        except TimeoutException:
            self.log_action("Карточки товаров не видимы")
            return False

    @allure.step("Добавление товара в корзину")
    def add_product_to_cart(self):
        self.log_action("Добавление товара в корзину")
        product_title = self.wait_for_element_visible(self.PRODUCT_TITLE)
        self.browser.execute_script("arguments[0].scrollIntoView(true);", product_title)
        self.log_action(f"Выбран продукт: {product_title.text}")

        add_button = self.wait_for_element_visible(self.ADD_TO_CART_BUTTON)
        self.browser.execute_script("arguments[0].click();", add_button)
        self.log_action("Товар успешно добавлен в корзину")

    @allure.step("Ожидание исчезновения уведомления об успехе")
    def wait_for_success_alert_disappear(self):
        self.log_action("Ожидание исчезновения уведомления об успехе")
        self.wait_for_invisibility_of_element(self.SUCCESS_ALERT)
        self.log_action("Уведомление об успехе исчезло")

    @allure.step("Получение текста кнопки корзины")
    def get_cart_items_count_and_price(self):
        self.log_action("Получение количества и стоимости товаров в корзине")
        cart_button = self.wait_for_element_visible(self.CART_BUTTON)
        return cart_button.text

    @allure.step("Переключение валюты")
    def switch_currency(self, selected_currency):
        self.log_action(f"Переключение валюты на {selected_currency}")
        currency_switcher = self.wait_for_element_visible(self.CURRENCY_SWITCHER)
        currency_switcher.click()

        currency_choice = self.wait_for_element_visible(
            (By.CSS_SELECTOR, f"a[href='{selected_currency}']")
        )
        currency_choice.click()

    @allure.step("Получение цен продуктов с указанной валютой")
    def get_product_prices(self, currency_symbol):
        self.log_action(f"Поиск цен с валютой {currency_symbol}")
        prices_locator = (By.XPATH, f"//span[contains(text(), '{currency_symbol}')]")
        return self.find_elements(prices_locator)
