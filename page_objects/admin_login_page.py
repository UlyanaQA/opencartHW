import allure
from selenium.common import TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By


class AdminLoginPage(BasePage):
    USERNAME_FIELD = (By.CSS_SELECTOR, "#input-username.form-control")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#input-password.form-control")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "#nav-logout.nav-item")
    LOGIN_FORM = (By.CSS_SELECTOR, "#form-login")
    LOGIN_BUTTON = (By.CSS_SELECTOR, ".btn.btn-primary")
    FORM_HEADER = (By.CSS_SELECTOR, ".card-header")
    HOME_BUTTON = (By.CSS_SELECTOR, "#header a")

    def __init__(self, browser):
        super().__init__(browser)
        self.browser = browser

    @allure.step("Проверка наличия поля ввода имени пользователя")
    def is_username_field_present(self):
        self.log_action("Проверка наличия поля ввода имени пользователя")
        try:
            self.wait_for_element_present(self.USERNAME_FIELD)
            self.log_action("Поле ввода имени пользователя найдено")
            return True
        except TimeoutException:
            self.log_action("Поле ввода имени пользователя не найдено")
            return False

    @allure.step("Проверка наличия поля ввода пароля")
    def is_password_field_present(self):
        self.log_action("Проверка наличия поля ввода пароля")
        try:
            self.wait_for_element_present(self.PASSWORD_FIELD)
            self.log_action("Поле ввода пароля найдено")
            return True
        except TimeoutException:
            self.log_action("Поле ввода пароля не найдено")
            return False

    @allure.step("Проверка наличия кнопки входа")
    def is_login_button_present(self):
        self.log_action("Проверка наличия кнопки входа")
        try:
            self.wait_for_element_present(self.LOGIN_BUTTON)
            self.log_action("Кнопка входа найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка входа не найдена")
            return False

    @allure.step("Проверка наличия заголовка формы входа")
    def is_form_header_present(self):
        self.log_action("Проверка наличия заголовка формы входа")
        try:
            self.wait_for_element_present(self.FORM_HEADER)
            self.log_action("Заголовок формы входа найден")
            return True
        except TimeoutException:
            self.log_action("Заголовок формы входа не найден")
            return False

    @allure.step("Проверка наличия кнопки возврата на главную страницу")
    def is_home_button_present(self):
        self.log_action("Проверка наличия кнопки возврата на главную страницу")
        try:
            self.wait_for_element_present(self.HOME_BUTTON)
            self.log_action("Кнопка возврата на главную страницу найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка возврата на главную страницу не найдена")
            return False

    @allure.step("Авторизация пользователя")
    def login(self, username, password):
        self.log_action(f"Авторизация пользователя: {username}")
        try:
            username_field = self.wait_for_element_visible(self.USERNAME_FIELD)
            username_field.clear()
            username_field.send_keys(username)

            password_field = self.wait_for_element_visible(self.PASSWORD_FIELD)
            password_field.clear()
            password_field.send_keys(password)

            self.wait_for_element_visible(self.SUBMIT_BUTTON).click()

            self.wait_for_element_visible(self.HOME_BUTTON, timeout=10)
            self.log_action(f"Успешная авторизация пользователя: {username}")
        except Exception as e:
            self.log_action(
                f"Ошибка при авторизации пользователя: {username}. Описание: {e}"
            )
            raise

    @allure.step("Выход из системы")
    def logout(self):
        self.log_action("Выход из системы")
        try:
            self.wait_for_element_visible(self.LOGOUT_BUTTON).click()

            self.wait_for_element_visible(self.LOGIN_FORM, timeout=5)
            self.log_action("Успешный выход из системы")
        except Exception as e:
            self.log_action(f"Ошибка при выходе из системы. Описание: {e}")
            raise

    @allure.step("Проверка отображения формы входа")
    def is_login_form_displayed(self):
        self.log_action("Проверка отображения формы входа")
        try:
            form = self.wait_for_element_visible(self.LOGIN_FORM)
            if form.is_displayed():
                self.log_action("Форма входа отображается")
                return True
            else:
                self.log_action("Форма входа не отображается")
                return False
        except TimeoutException:
            self.log_action("Форма входа не найдена")
            return False
