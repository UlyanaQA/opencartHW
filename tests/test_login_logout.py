import allure


@allure.epic("Администрирование")
@allure.feature("Форма входа/выхода")
@allure.story("Проверка логина и разлогина пользователя")
def test_login_logout(admin_login_page):
    with allure.step("Авторизация пользователя"):
        admin_login_page.login("user", "bitnami")

    with allure.step("Выход из системы"):
        admin_login_page.logout()

    with allure.step("Проверка отображения формы входа после выхода"):
        assert admin_login_page.is_login_form_displayed(), (
            "Форма входа не отображается после выхода"
        )
