from .base_page import BasePage
from selenium.webdriver.common.by import By


class ProductPage(BasePage):
    NEW_PRICE = (By.CSS_SELECTOR, "span.price-new")
    ADD_TO_WISHLIST_BUTTON = (By.CSS_SELECTOR, "button[formaction$='wishlist.add']")
    ADD_TO_COMPARE_BUTTON = (By.CSS_SELECTOR, "button[formaction$='compare.add']")
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, "#button-cart")
    PRODUCT_PHOTO = (By.CSS_SELECTOR, ".image.magnific-popup")

    def open_product_page(self, product_url):
        self.open(product_url)

    def is_new_price_present(self):
        return self.wait_for_element_present(self.NEW_PRICE)

    def is_add_to_wishlist_button_present(self):
        return self.wait_for_element_present(self.ADD_TO_WISHLIST_BUTTON)

    def is_add_to_compare_button_present(self):
        return self.wait_for_element_present(self.ADD_TO_COMPARE_BUTTON)

    def is_add_to_cart_button_present(self):
        return self.wait_for_element_present(self.ADD_TO_CART_BUTTON)

    def is_product_photo_present(self):
        return self.wait_for_element_present(self.PRODUCT_PHOTO)
