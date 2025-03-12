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

    def open_admin_login_page(self, admin_url):
        self.open(admin_url)

    def is_username_field_present(self):
        return self.wait_for_element_present(self.USERNAME_FIELD)

    def is_password_field_present(self):
        return self.wait_for_element_present(self.PASSWORD_FIELD)

    def is_login_button_present(self):
        return self.wait_for_element_present(self.LOGIN_BUTTON)

    def is_form_header_present(self):
        return self.wait_for_element_present(self.FORM_HEADER)

    def is_home_button_present(self):
        return self.wait_for_element_present(self.HOME_BUTTON)

    def login(self, username, password):
        username_field = self.wait_for_element_visible(self.USERNAME_FIELD)
        username_field.clear()
        username_field.send_keys(username)
        password_field = self.wait_for_element_visible(self.PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(password)
        return self.wait_for_element_visible(self.SUBMIT_BUTTON).click()

    def logout(self):
        return self.wait_for_element_visible(self.LOGOUT_BUTTON).click()

    def is_login_form_displayed(self):
        return self.wait_for_element_visible(self.LOGIN_FORM).is_displayed()
