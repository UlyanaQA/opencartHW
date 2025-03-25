import allure

# Удаление товара из списка в разделе администратора


@allure.epic("Администрирование")
@allure.feature("Удаление продукта")
@allure.story("Удаление уникального продукта")
def test_delete_product(create_product, administration_page):
    product_name = create_product

    administration_page.find_product_by_name(product_name)

    administration_page.products_select_check_box()

    administration_page.products_delete_product()

    is_product_deleted = administration_page.check_product_absence(product_name)
    assert is_product_deleted, f"Продукт '{product_name}' не удален из таблицы"
