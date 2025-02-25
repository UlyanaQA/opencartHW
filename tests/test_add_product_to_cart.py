import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# автотест добавления в корзину случайного товара с главной страницы и проверка того, что он появился в корзине
def test_add_product_to_cart(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10)
    product_title = browser.find_element(
        By.CSS_SELECTOR, ".product-thumb .content .description h4 a"
    )
    browser.execute_script("arguments[0].scrollIntoView();", product_title)
    time.sleep(0.7)
    add_button = browser.find_element(By.CSS_SELECTOR, "button[formaction*='cart.add']")
    add_button.click()
    wait.until(
        EC.invisibility_of_element(
            (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
        )
    )
    time.sleep(0.7)
    cart_btn = browser.find_element(By.XPATH, '//*[@id="header-cart"]/div/button')
    assert cart_btn.text == "1 item(s) - $602.00", (
        f"Ожидаемая сумма: '1 item(s) - $602.00', Фактическая: '{cart_btn.text}'"
    )
