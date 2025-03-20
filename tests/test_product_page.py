from page_objects.product_page import ProductPage


def test_new_price(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page(browser.url + "en-gb/product/desktops/apple-cinema")
    new_price = product_page.is_new_price_present()
    assert new_price is not None, "На странице не найдена новая цена товара"


def test_add_to_wishlist(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page(browser.url + "en-gb/product/desktops/apple-cinema")
    wish_list = product_page.is_add_to_wishlist_button_present()
    assert wish_list is not None, "На странице не найдена кнопка добавления в Избранное"


def test_add_to_compare(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page(browser.url + "en-gb/product/desktops/apple-cinema")
    add_to_compare = product_page.is_add_to_compare_button_present()
    assert add_to_compare is not None, (
        "На странице не найдена кнопка добавления в сравнение"
    )


def test_add_to_cart(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page(browser.url + "en-gb/product/desktops/apple-cinema")
    add_to_cart = product_page.is_add_to_cart_button_present()
    assert add_to_cart is not None, "На странице не найдена кнопка добавления в корзину"


def test_product_photo(browser):
    product_page = ProductPage(browser)
    product_page.open_product_page(browser.url + "en-gb/product/desktops/apple-cinema")
    photo = product_page.is_product_photo_present()
    assert photo is not None, "На странице не найдено фото товара"
