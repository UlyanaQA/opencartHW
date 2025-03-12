from page_objects.administration_page import AdministrationPage
from page_objects.admin_login_page import AdminLoginPage


# Удаление товара из списка в разделе администратора
def test_delete_product(browser):
    product_name = "prod7"
    administration_page = AdministrationPage(browser)
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    admin_page.login("user", "bitnami")
    administration_page.administration_go_to_product_page()
    administration_page.find_product_by_name(product_name)
    administration_page.products_select_check_box()
    administration_page.products_delete_product()
    is_product_deleted = administration_page.check_product_absence()
    assert is_product_deleted, "Продукт не удален из таблицы"
