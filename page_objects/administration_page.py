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

    def administration_go_to_product_page(self):
        self.wait_for_element_visible(self.CATALOG).click()
        self.wait_for_element_visible(self.PRODUCTS).click()

    def products_click_add_new_product(self):
        self.wait_for_element_visible(self.ADD_NEW_PRODUCT).click()

    def products_add_new_product(self, product_name, meta_tag, model, keyword):
        self.fill_field(self.PRODUCT_NAME, product_name)
        self.fill_field(self.META_TAG_TITLE, meta_tag)
        self.wait_for_element_visible(self.DATA_TAB).click()
        self.fill_field(self.MODEL, model)
        self.wait_for_element_visible(self.SEO_TAB).click()
        self.fill_field(self.KEYWORD, keyword)
        self.wait_for_element_visible(self.SAVE_BTN).click()

    def find_product_by_name(self, product_name):
        self.fill_field(self.FILTER_NAME_PRODUCT, product_name)
        self.wait_for_element_visible(self.FILTER_BTN).click()
        product_locator = (By.CSS_SELECTOR, "#form-product tbody td.text-start")
        return self.wait_for_element_visible(product_locator, timeout=2)

    def products_select_check_box(self):
        self.wait_for_element_visible(self.CHECKBOX_PRODUCT).click()

    def products_delete_product(self):
        self.wait_for_element_visible(self.DELETE_BTN).click()
        self.browser.switch_to.alert.accept()
        self.wait_for_element_visible(
            (By.CSS_SELECTOR, "#form-product tbody tr td"), timeout=5
        )

    def check_product_absence(self):
        no_results_locator = (
            By.CSS_SELECTOR,
            "#form-product > div.table-responsive > table > tbody > tr > td",
        )
        try:
            text = self.wait_for_element_visible(
                no_results_locator, timeout=3
            ).text.strip()
            return text == "No results!"
        except Exception:
            return False
