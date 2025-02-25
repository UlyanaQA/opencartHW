from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_new_price(browser):
    browser.get(browser.url + "en-gb/product/desktops/apple-cinema")
    wait = WebDriverWait(browser, 3)
    new_price = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "span.price-new"))
    )
    assert new_price is not None, "На странице не найдена новая цена товара"


def test_add_to_wishlist(browser):
    browser.get(browser.url + "en-gb/product/desktops/apple-cinema")
    wait = WebDriverWait(browser, 3)
    wish_list = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[formaction$='wishlist.add']")
        )
    )
    assert wish_list is not None, "На странице не найдена кнопка добавления в Избранное"


def test_add_to_compare(browser):
    browser.get(browser.url + "en-gb/product/desktops/apple-cinema")
    wait = WebDriverWait(browser, 3)
    add_to_compare = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "button[formaction$='compare.add']")
        )
    )
    assert add_to_compare is not None, (
        "На странице не найдена кнопка добавления в сравнение"
    )


def test_add_to_cart(browser):
    browser.get(browser.url + "en-gb/product/desktops/apple-cinema")
    wait = WebDriverWait(browser, 3)
    add_to_cart = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#button-cart"))
    )
    assert add_to_cart is not None, "На странице не найдена кнопка добавления в корзину"


def test_product_photo(browser):
    browser.get(browser.url + "en-gb/product/desktops/apple-cinema")
    wait = WebDriverWait(browser, 3)
    photo = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".image.magnific-popup"))
    )
    assert photo is not None, "На странице не найдено фото товара"
