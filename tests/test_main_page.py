import allure
import logging


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка наличия кнопки поиска")
def test_search_button(main_page):
    try:
        with allure.step("Проверка наличия кнопки поиска"):
            assert main_page.is_search_button_present(), (
                "На странице не найдена кнопка поиска"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            main_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка наличия верхнего навигационного меню")
def test_top_navigation(main_page):
    try:
        with allure.step("Проверка наличия верхнего навигационного меню"):
            assert main_page.is_top_navigation_present(), (
                "На странице не найдено верхнее навигационное меню"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            main_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка видимости списка выбора валюты")
def test_currency(main_page):
    try:
        with allure.step("Проверка видимости списка выбора валюты"):
            assert main_page.is_currency_list_visible(), (
                "На странице не найден выбор валюты"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            main_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка наличия пунктов меню")
def test_menu(main_page):
    try:
        with allure.step("Получение пунктов меню"):
            menu_items = main_page.get_menu_items()

        with allure.step("Проверка текста каждого пункта меню"):
            for index, item in enumerate(menu_items, start=1):
                item_text = item.text.strip()
                assert item_text, (
                    f"Пункт меню #{index} пустой или не содержит видимого текста"
                )

    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            main_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка видимости карточек товаров")
def test_goodscards(main_page):
    try:
        with allure.step("Проверка видимости карточек товаров"):
            assert main_page.is_goods_cards_visible(), (
                "На странице не найдены карточки товаров"
            )

    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")
        allure.attach(
            main_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )
        raise AssertionError(str(e))
