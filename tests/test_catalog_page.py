from page_objects.catalog_page import CatalogPage


def test_sort_list(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page(browser.url + "/en-gb/catalog/desktops")
    sort_list = catalog_page.is_sort_list_present()
    assert sort_list is not None, "На странице не найдено поле сортировки"


def test_compare_button(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page(browser.url + "/en-gb/catalog/desktops")
    compare_btn = catalog_page.is_compare_button_present()
    assert compare_btn is not None, "На странице не найдена кнопка сравнения"


def test_home_button(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page(browser.url + "/en-gb/catalog/desktops")
    home_btn = catalog_page.is_home_button_present()
    assert home_btn is not None, (
        "На странице не найдена кнопка возвращения на главную страницу"
    )


def test_left_menu(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page(browser.url + "/en-gb/catalog/desktops")
    left_menu = catalog_page.is_left_menu_present()
    assert left_menu is not None, "На странице не найден список категорий товаров"


def test_laptop_category(browser):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page(browser.url + "/en-gb/catalog/laptop-notebook")
    laptop_category = catalog_page.get_laptop_category_links()
    assert len(laptop_category) == 2, (
        "В каталоге Laptops & Notebooks должно быть 2 категории"
    )
