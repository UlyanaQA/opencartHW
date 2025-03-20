from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def open(self, url):
        self.browser.get(url)

    def wait_for_element_present(self, locator, timeout=3):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def wait_for_element_visible(self, locator, timeout=3):
        return WebDriverWait(self.browser, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def find_elements(self, locator, timeout=3):
        WebDriverWait(self.browser, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )
        return self.browser.find_elements(*locator)

    def wait_for_invisibility_of_element(self, locator, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def fill_field(self, locator, value):
        field = self.wait_for_element_visible(locator)
        field.clear()
        field.send_keys(value)

    def wait_text(self, title, timeout=3):
        return WebDriverWait(self.browser, timeout).until(EC.title_is(title))

    def get_text(self, locator: tuple):
        return self.browser.find_element(*locator).text
