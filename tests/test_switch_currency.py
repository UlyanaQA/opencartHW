import allure
from element_objects.header_element import HeaderElement
import pytest


# Переключение валют из верхнего меню opencart
@allure.epic("Главная страница")
@allure.feature("Изменение валюты")
@allure.story("Проверка изменения валюты из верхнего меню opencart")
@pytest.mark.parametrize(
    "currency_code,expected_symbol", [("qEUR", "€"), ("GBP", "£"), ("USD", "$")]
)
def test_change_currency(browser, currency_code, expected_symbol):
    header = HeaderElement(browser)
    header.open(browser.url)
    actual_symbol = header.header_switch_currency(currency_code)
    assert actual_symbol == expected_symbol, (
        f"Некорректный символ валюты. Ожидалось: {expected_symbol}, "
        f"Получено: {actual_symbol} (для кода {currency_code})"
    )
