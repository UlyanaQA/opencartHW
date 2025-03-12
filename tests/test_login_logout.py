from page_objects.admin_login_page import AdminLoginPage


def test_login_logout(browser):
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    admin_page.login("user", "bitnami")
    admin_page.logout()
    assert admin_page.is_login_form_displayed(), (
        "Форма входа не отображается после выхода"
    )
