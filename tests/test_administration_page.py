from page_objects.admin_login_page import AdminLoginPage


def test_username(browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    username_field = admin_page.is_username_field_present()
    assert username_field is not None, (
        "На странице не найдено поле ввода имени пользователя"
    )


def test_password(browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    password_field = admin_page.is_password_field_present()
    assert password_field is not None, "На странице не найдено поле ввода пароля"


def test_login_button(browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    login_btn = admin_page.is_login_button_present()
    assert login_btn is not None, "На странице не найдена кнопка логина"


def test_form_header(browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    form_header = admin_page.is_form_header_present()
    assert form_header is not None, "На странице не найден заголовок окна логина"


def test_home_button(browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    home_btn = admin_page.is_home_button_present()
    assert home_btn is not None, (
        "На странице не найдена кнопка возврата на главную страницу"
    )
