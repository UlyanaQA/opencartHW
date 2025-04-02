import allure


@allure.epic("Каталог товаров")
@allure.feature("Элементы страницы каталога")
@allure.story("Проверка наличия поля сортировки")
def test_sort_list(catalog_desktops_page):
    with allure.step("Проверка наличия поля сортировки"):
        assert catalog_desktops_page.is_sort_list_present(), (
            "На странице не найдено поле сортировки"
        )


@allure.epic("Каталог товаров")
@allure.feature("Элементы страницы каталога")
@allure.story("Проверка наличия кнопки сравнения")
def test_compare_button(catalog_desktops_page):
    with allure.step("Проверка наличия кнопки сравнения"):
        assert catalog_desktops_page.is_compare_button_present(), (
            "На странице не найдена кнопка сравнения"
        )


@allure.epic("Каталог товаров")
@allure.feature("Элементы страницы каталога")
@allure.story("Проверка наличия кнопки возврата на главную страницу")
def test_home_button(catalog_desktops_page):
    with allure.step("Проверка наличия кнопки возврата на главную страницу"):
        assert catalog_desktops_page.is_home_button_present(), (
            "На странице не найдена кнопка возврата на главную страницу"
        )


@allure.epic("Каталог товаров")
@allure.feature("Элементы страницы каталога")
@allure.story("Проверка наличия левого меню")
def test_left_menu(catalog_desktops_page):
    with allure.step("Проверка наличия левого меню"):
        assert catalog_desktops_page.is_left_menu_present(), (
            "На странице не найдено левое меню"
        )


@allure.epic("Каталог товаров")
@allure.feature("Ссылки категорий ноутбуков")
@allure.story("Проверка наличия двух категорий ноутбуков")
def test_laptop_category_links(catalog_laptops_page):
    with allure.step("Получение ссылок категорий ноутбуков"):
        laptop_category = catalog_laptops_page.get_laptop_category_links()

    with allure.step("Проверка количества категорий ноутбуков"):
        assert len(laptop_category) == 2, (
            "В каталоге Laptops & Notebooks должно быть 2 категории"
        )
