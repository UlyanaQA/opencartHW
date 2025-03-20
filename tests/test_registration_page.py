from page_objects.register_page import RegisterPage


def test_username(browser):
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.url + "/index.php?route=account/register")
    username_field = register_page.is_firstname_field_present()
    assert username_field is not None, (
        "На странице не найдено поле ввода имени пользователя"
    )


def test_submit(browser):
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.url + "/index.php?route=account/register")
    submit_btn = register_page.is_submit_button_present()
    assert submit_btn is not None, (
        "На странице не найдена кнопка регистрации пользователя"
    )


def test_read_policy(browser):
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.url + "/index.php?route=account/register")
    read_radiobtn = register_page.is_agree_checkbox_present()
    assert read_radiobtn is not None, (
        "На странице не найден чекбокс подтверждения прочтения политики конфиденциальности"
    )


def test_right_menu(browser):
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.url + "/index.php?route=account/register")
    right_menu = register_page.is_right_menu_present()
    assert right_menu is not None, "На странице не найдено меню справа"


def test_required_fields(browser):
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.url + "/index.php?route=account/register")
    required_fields = register_page.get_required_fields()
    assert len(required_fields) == 4, "Обязательных полей должно быть 4"
