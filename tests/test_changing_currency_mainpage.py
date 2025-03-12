import pytest
from page_objects.main_page import MainPage


# автотест переключения валют: цены на товары меняются на главной
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(browser, selected_currency, currency):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    main_page.switch_currency(selected_currency)
    product_prices = main_page.get_product_prices(currency)
    for price in product_prices:
        assert currency in price.text, f"Цена {price.text} не содержит {currency}"
