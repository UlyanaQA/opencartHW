import allure
import logging


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия новой цены товара")
def test_new_price(product_page):
    try:
        with allure.step("Проверка наличия новой цены товара"):
            assert product_page.is_new_price_present(), (
                "На странице не найдена новая цена товара"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            product_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия кнопки добавления в Избранное")
def test_add_to_wishlist(product_page):
    try:
        with allure.step("Проверка наличия кнопки добавления в Избранное"):
            assert product_page.is_add_to_wishlist_button_present(), (
                "На странице не найдена кнопка добавления в Избранное"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            product_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия кнопки добавления в сравнение")
def test_add_to_compare(product_page):
    try:
        with allure.step("Проверка наличия кнопки добавления в сравнение"):
            assert product_page.is_add_to_compare_button_present(), (
                "На странице не найдена кнопка добавления в сравнение"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            product_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия кнопки добавления в корзину")
def test_add_to_cart(product_page):
    try:
        with allure.step("Проверка наличия кнопки добавления в корзину"):
            assert product_page.is_add_to_cart_button_present(), (
                "На странице не найдена кнопка добавления в корзину"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            product_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Страница товара")
@allure.feature("Элементы страницы товара")
@allure.story("Проверка наличия фото товара")
def test_product_photo(product_page):
    try:
        with allure.step("Проверка наличия фото товара"):
            assert product_page.is_product_photo_present(), (
                "На странице не найдено фото товара"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            product_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))
