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

    def open_register_page(self, register_url):
        self.open(register_url)

    def is_firstname_field_present(self):
        return self.wait_for_element_present(self.FIRSTNAME_FIELD)

    def is_submit_button_present(self):
        return self.wait_for_element_present(self.SUBMIT_BTN)

    def is_agree_checkbox_present(self):
        return self.wait_for_element_present(self.AGREE_CHECKBOX)

    def is_right_menu_present(self):
        return self.wait_for_element_present(self.RIGHT_MENU)

    def get_required_fields(self):
        return self.find_elements(self.REQUIRED_FIELDS)

    def registration_add_user(self, firstname, lastname, email, password):
        self.fill_field(self.FIRSTNAME_FIELD, firstname)
        self.fill_field(self.LASTNAME_FIELD, lastname)
        self.fill_field(self.EMAIL_FIELD, email)
        self.fill_field(self.PASSWORD_FIELD, password)
        self.wait_for_element_visible(self.AGREE_CHECKBOX).click()
        self.wait_for_element_visible(self.SUBMIT_BTN).click()
