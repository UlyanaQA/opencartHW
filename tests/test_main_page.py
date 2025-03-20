from page_objects.main_page import MainPage


def test_search_button(browser):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    search_button = main_page.is_search_button_present()
    assert search_button is not None, "На странице не найдена кнопка поиска"


def test_top_navigation(browser):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    top_nav = main_page.is_top_navigation_present()
    assert top_nav is not None, "На странице не найдено верхнее навигационное меню"


def test_currency(browser):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    curr_list = main_page.is_currency_list_visible()
    assert curr_list is not None, "На странице не найден выбор валюты"


def test_menu(browser):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    menu_items = main_page.get_menu_items()
    for index, item in enumerate(menu_items, start=1):
        item_text = item.text.strip()
        assert item_text, f"Пункт меню #{index} пустой или не содержит видимого текста"


def test_goodscards(browser):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    goods_cards = main_page.is_goods_cards_visible()
    assert goods_cards is not None, "На странице не найдены карточки товаров"
