import allure


@allure.epic("Администрирование")
@allure.feature("Форма входа/выхода")
@allure.story("Проверка логина и разлогина пользователя")
def test_login_logout(admin_login_page):
    admin_login_page.login("user", "bitnami")
    admin_login_page.logout()

    assert admin_login_page.is_login_form_displayed(), (
        "Форма входа не отображается после выхода"
    )
