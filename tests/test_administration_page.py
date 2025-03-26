import allure
import logging


@allure.epic("Администрирование")
@allure.feature("Страница авторизации")
@allure.story("Проверка наличия поля ввода имени пользователя")
def test_username(admin_login_page):
    try:
        with allure.step("Проверка наличия поля ввода имени пользователя"):
            assert admin_login_page.is_username_field_present(), (
                "На странице не найдено поле ввода имени пользователя"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            admin_login_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))


@allure.epic("Администрирование")
@allure.feature("Страница авторизации")
@allure.story("Проверка наличия поля ввода пароля")
def test_password(admin_login_page):
    try:
        with allure.step("Проверка наличия поля ввода пароля"):
            assert admin_login_page.is_password_field_present(), (
                "На странице не найдено поле ввода пароля"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            admin_login_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))


@allure.epic("Администрирование")
@allure.feature("Страница авторизации")
@allure.story("Проверка наличия кнопки логина")
def test_login_button(admin_login_page):
    try:
        with allure.step("Проверка наличия кнопки логина"):
            assert admin_login_page.is_login_button_present(), (
                "На странице не найдена кнопка логина"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            admin_login_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))


@allure.epic("Администрирование")
@allure.feature("Страница авторизации")
@allure.story("Проверка наличия заголовка формы авторизации")
def test_form_header(admin_login_page):
    try:
        with allure.step("Проверка наличия заголовка формы авторизации"):
            assert admin_login_page.is_form_header_present(), (
                "На странице не найден заголовок формы входа"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            admin_login_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))


@allure.epic("Администрирование")
@allure.feature("Страница авторизации")
@allure.story("Проверка наличия кнопки возврата на главную страницу")
def test_home_button(admin_login_page):
    try:
        with allure.step("Проверка наличия кнопки возврата на главную страницу"):
            assert admin_login_page.is_home_button_present(), (
                "На странице не найдена кнопка возврата на главную страницу"
            )
    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            admin_login_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))
