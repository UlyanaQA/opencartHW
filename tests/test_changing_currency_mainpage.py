import allure
import pytest


# автотест переключения валют: цены на товары меняются на главной


@allure.epic("Главная страница")
@allure.feature("Изменение цены при смене валюты")
@allure.story("Проверка изменения валюты")
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(main_page, selected_currency, currency):
    main_page.switch_currency(selected_currency)
    product_prices = main_page.get_product_prices(currency)
    for price in product_prices:
        assert currency in price.text, f"Цена {price.text} не содержит {currency}"
