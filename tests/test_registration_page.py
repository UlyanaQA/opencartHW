import allure


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия поля ввода имени пользователя")
def test_username(register_page):
    assert register_page.is_firstname_field_present(), (
        "На странице не найдено поле ввода имени пользователя"
    )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия кнопки регистрации")
def test_submit(register_page):
    assert register_page.is_submit_button_present(), (
        "На странице не найдена кнопка регистрации пользователя"
    )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия чекбокса политики конфиденциальности")
def test_read_policy(register_page):
    assert register_page.is_agree_checkbox_present(), (
        "На странице не найден чекбокс подтверждения прочтения политики конфиденциальности"
    )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия правого меню")
def test_right_menu(register_page):
    assert register_page.is_right_menu_present(), "На странице не найдено меню справа"


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка количества обязательных полей")
def test_required_fields(register_page):
    required_fields = register_page.get_required_fields()
    assert len(required_fields) == 4, "Обязательных полей должно быть 4"
