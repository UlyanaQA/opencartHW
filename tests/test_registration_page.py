import allure


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия поля ввода имени пользователя")
def test_username(register_page):
    with allure.step("Проверка наличия поля ввода имени пользователя"):
        assert register_page.is_firstname_field_present(), (
            "На странице не найдено поле ввода имени пользователя"
        )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия кнопки регистрации")
def test_submit(register_page):
    with allure.step("Проверка наличия кнопки регистрации"):
        assert register_page.is_submit_button_present(), (
            "На странице не найдена кнопка регистрации пользователя"
        )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия чекбокса политики конфиденциальности")
def test_read_policy(register_page):
    with allure.step("Проверка наличия чекбокса политики конфиденциальности"):
        assert register_page.is_agree_checkbox_present(), (
            "На странице не найден чекбокс подтверждения прочтения политики конфиденциальности"
        )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка наличия правого меню")
def test_right_menu(register_page):
    with allure.step("Проверка наличия правого меню"):
        assert register_page.is_right_menu_present(), (
            "На странице не найдено меню справа"
        )


@allure.epic("Страница регистрации")
@allure.feature("Элементы страницы регистрации")
@allure.story("Проверка количества обязательных полей")
def test_required_fields(register_page):
    with allure.step("Получение списка обязательных полей"):
        required_fields = register_page.get_required_fields()

    with allure.step("Проверка количества обязательных полей"):
        assert len(required_fields) == 4, "Обязательных полей должно быть 4"
