from page_objects.administration_page import AdministrationPage
from page_objects.admin_login_page import AdminLoginPage


# Добавление нового товара в разделе администратора
def test_add_new_product(browser):
    product_name = "prod7"
    meta_tag = "meta_tag7"
    model = "model7"
    keyword = "keyword7"
    administration_page = AdministrationPage(browser)
    admin_page = AdminLoginPage(browser)
    admin_page.open_admin_login_page(browser.url + "/administration")
    admin_page.login("user", "bitnami")
    administration_page.administration_go_to_product_page()
    administration_page.products_click_add_new_product()
    administration_page.products_add_new_product(product_name, meta_tag, model, keyword)
    administration_page.administration_go_to_product_page()
    administration_page.find_product_by_name(product_name)

    product_element = administration_page.find_product_by_name(product_name)
    assert product_element is not None, "Продукт не найден в таблице"
    assert product_element.text.strip().split("\n")[0] == product_name, (
        f"Название продукта не совпадает: {product_element.text}"
    )
