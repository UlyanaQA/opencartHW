import allure
import logging
from element_objects.header_element import HeaderElement
import pytest


# Переключение валют из верхнего меню opencart
@allure.epic("Главная страница")
@allure.feature("Изменение валюты")
@allure.story("Проверка изменения валюты из верхнего меню opencart")
@pytest.mark.parametrize(
    "currency_code,expected_symbol", [("EUR", "€"), ("GBP", "£"), ("USD", "$")]
)
def test_change_currency(browser, currency_code, expected_symbol):
    try:
        with allure.step(
            f"Открытие главной страницы для переключения валюты {currency_code}"
        ):
            header = HeaderElement(browser)
            header.open(browser.url)

        with allure.step(f"Переключение валюты на {currency_code}"):
            actual_symbol = header.header_switch_currency(currency_code)

        with allure.step(
            f"Проверка символа валюты после переключения ({currency_code})"
        ):
            assert actual_symbol == expected_symbol, (
                f"Некорректный символ валюты. Ожидалось: {expected_symbol}, "
                f"Получено: {actual_symbol} (для кода {currency_code})"
            )

    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))
