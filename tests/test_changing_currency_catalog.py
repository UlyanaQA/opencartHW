import pytest
from page_objects.catalog_page import CatalogPage


# автотест переключения валют: цены на товары меняются на странице каталога
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(browser, selected_currency, currency):
    catalog_page = CatalogPage(browser)
    catalog_page.open_catalog_page(browser.url + "/en-gb/catalog/desktops")
    catalog_page.switch_currency(selected_currency)
    catalog_page.wait_for_product_category()
    desktops_prices = catalog_page.get_desktops_prices()
    for price in desktops_prices:
        assert currency in price.text, f"Цена {price.text} не обновилась до {currency}"
