import allure
import pytest


# автотест переключения валют: цены на товары меняются на странице каталога


@allure.epic("Страница каталога")
@allure.feature("Изменение цены при смене валюты")
@allure.story("Проверка изменения цены товара при смене валюты")
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(catalog_desktops_page, selected_currency, currency):
    catalog_desktops_page.switch_currency(selected_currency)
    catalog_desktops_page.wait_for_product_category()
    desktops_prices = catalog_desktops_page.get_desktops_prices()
    for price in desktops_prices:
        assert currency in price.text, f"Цена {price.text} не обновилась до {currency}"
