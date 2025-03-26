import allure
from selenium.common import TimeoutException

from .base_page import BasePage
from selenium.webdriver.common.by import By


class RegisterPage(BasePage):
    FIRSTNAME_FIELD = (By.CSS_SELECTOR, "#input-firstname")
    SUBMIT_BTN = (By.CSS_SELECTOR, "#form-register button")
    AGREE_CHECKBOX = (By.CSS_SELECTOR, "input[name='agree']")
    RIGHT_MENU = (By.CSS_SELECTOR, "#column-right")
    REQUIRED_FIELDS = (By.CSS_SELECTOR, "#form-register fieldset div.row.mb-3.required")
    LASTNAME_FIELD = (By.ID, "input-lastname")
    EMAIL_FIELD = (By.ID, "input-email")
    PASSWORD_FIELD = (By.ID, "input-password")

    @allure.step("Проверка наличия поля 'First Name'")
    def is_firstname_field_present(self):
        self.log_action("Проверка наличия поля 'First Name'")
        try:
            self.wait_for_element_present(self.FIRSTNAME_FIELD)
            self.log_action("Поле 'First Name' найдено")
            return True
        except TimeoutException:
            self.log_action("Поле 'First Name' не найдено")
            return False

    @allure.step("Проверка наличия кнопки 'Continue'")
    def is_submit_button_present(self):
        self.log_action("Проверка наличия кнопки 'Continue'")
        try:
            self.wait_for_element_present(self.SUBMIT_BTN)
            self.log_action("Кнопка 'Continue' найдена")
            return True
        except TimeoutException:
            self.log_action("Кнопка 'Continue' не найдена")
            return False

    @allure.step("Проверка наличия чекбокса согласия с условиями")
    def is_agree_checkbox_present(self):
        self.log_action("Проверка наличия радиобаттона согласия с условиями")
        try:
            self.wait_for_element_present(self.AGREE_CHECKBOX)
            self.log_action("Радиобаттон согласия с условиями найден")
            return True
        except TimeoutException:
            self.log_action("Радиобаттон согласия с условиями не найден")
            return False

    @allure.step("Проверка наличия правого меню")
    def is_right_menu_present(self):
        self.log_action("Проверка наличия правого меню")
        try:
            self.wait_for_element_present(self.RIGHT_MENU)
            self.log_action("Правое меню найдено")
            return True
        except TimeoutException:
            self.log_action("Правое меню не найдено")
            return False

    @allure.step("Получение обязательных полей формы регистрации")
    def get_required_fields(self):
        self.log_action("Поиск обязательных полей формы регистрации")
        return self.find_elements(self.REQUIRED_FIELDS)

    @allure.step("Регистрация нового пользователя")
    def registration_add_user(self, firstname, lastname, email, password):
        self.log_action(
            f"Регистрация пользователя: {firstname} {lastname}, email: {email}"
        )
        self.fill_field(self.FIRSTNAME_FIELD, firstname)
        self.fill_field(self.LASTNAME_FIELD, lastname)
        self.fill_field(self.EMAIL_FIELD, email)
        self.fill_field(self.PASSWORD_FIELD, password)
        self.wait_for_element_visible(self.AGREE_CHECKBOX).click()
        self.log_action("Согласие с условиями подтверждено")
        self.wait_for_element_visible(self.SUBMIT_BTN).click()
        self.log_action("Форма регистрации отправлена")
