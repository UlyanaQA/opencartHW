import allure


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка наличия кнопки поиска")
def test_search_button(main_page):
    assert main_page.is_search_button_present(), "На странице не найдена кнопка поиска"


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка наличия верхнего навигационного меню")
def test_top_navigation(main_page):
    assert main_page.is_top_navigation_present(), (
        "На странице не найдено верхнее навигационное меню"
    )


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка видимости списка выбора валюты")
def test_currency(main_page):
    assert main_page.is_currency_list_visible(), "На странице не найден выбор валюты"


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка наличия пунктов меню")
def test_menu(main_page):
    menu_items = main_page.get_menu_items()
    for index, item in enumerate(menu_items, start=1):
        item_text = item.text.strip()
        assert item_text, f"Пункт меню #{index} пустой или не содержит видимого текста"


@allure.epic("Главная страница")
@allure.feature("Элементы главной страницы")
@allure.story("Проверка видимости карточек товаров")
def test_goodscards(main_page):
    assert main_page.is_goods_cards_visible(), "На странице не найдены карточки товаров"
