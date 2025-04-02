import allure
import pytest


@allure.epic("Каталог товаров")
@allure.feature("Изменение валюты")
@allure.story("Проверка обновления цен товаров после смены валюты")
@pytest.mark.parametrize(
    "selected_currency, currency_symbol",
    [
        ("EUR", "€"),
        ("GBP", "£"),
        ("USD", "$"),
    ],
)
def test_changing_currency(catalog_desktops_page, selected_currency, currency_symbol):
    with allure.step(f"Переключение валюты на {selected_currency}"):
        catalog_desktops_page.switch_currency(selected_currency)

    with allure.step("Ожидание загрузки категории товаров"):
        catalog_desktops_page.wait_for_product_category()

    with allure.step("Проверка обновления цен товаров"):
        desktops_prices = catalog_desktops_page.get_desktops_prices()
        for price in desktops_prices:
            assert currency_symbol in price.text, (
                f"Цена {price.text} не обновилась до {currency_symbol}"
            )
