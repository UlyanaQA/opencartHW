import allure


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия новой цены товара")
def test_new_price(product_page):
    assert product_page.is_new_price_present(), (
        "На странице не найдена новая цена товара"
    )


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия кнопки добавления в Избранное")
def test_add_to_wishlist(product_page):
    assert product_page.is_add_to_wishlist_button_present(), (
        "На странице не найдена кнопка добавления в Избранное"
    )


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия кнопки добавления в сравнение")
def test_add_to_compare(product_page):
    assert product_page.is_add_to_compare_button_present(), (
        "На странице не найдена кнопка добавления в сравнение"
    )


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия кнопки добавления в корзину")
def test_add_to_cart(product_page):
    assert product_page.is_add_to_cart_button_present(), (
        "На странице не найдена кнопка добавления в корзину"
    )


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия фото товара")
def test_product_photo(product_page):
    assert product_page.is_product_photo_present(), "На странице не найдено фото товара"
