import allure
import pytest
import uuid


# Добавление нового товара в разделе администратора
@allure.epic("Администрирование")
@allure.feature("Добавление нового продукта")
@allure.story("Создание уникального продукта")
@pytest.mark.parametrize(
    "product_name, meta_tag, model, keyword",
    [
        (
            f"prod18_{uuid.uuid4().hex[:2]}",
            f"meta_tag_{uuid.uuid4().hex[:2]}",
            f"model13_{uuid.uuid4().hex[:2]}",
            f"keyword17_{uuid.uuid4().hex[:2]}",
        )
    ],
)
def test_add_new_product(administration_page, product_name, meta_tag, model, keyword):
    with allure.step("Клик по кнопке 'Add New'"):
        administration_page.products_click_add_new_product()

    with allure.step("Заполнение формы нового продукта"):
        administration_page.products_add_new_product(
            product_name, meta_tag, model, keyword
        )

    with allure.step("Переход на страницу продуктов"):
        administration_page.administration_go_to_product_page()

    with allure.step("Поиск созданного продукта"):
        product_element = administration_page.find_product_by_name(product_name)

    assert product_element is not None, "Продукт не найден в таблице"

    with allure.step("Проверка названия продукта"):
        actual_text = product_element.text.strip().split("\n")[0]
        assert actual_text == product_name, (
            f"Название продукта не совпадает: {actual_text}"
        )
