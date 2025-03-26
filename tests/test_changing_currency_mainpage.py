import logging

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
    try:
        with allure.step(f"Переключение валюты на {selected_currency}"):
            main_page.switch_currency(selected_currency)

        with allure.step(f"Получение цен товаров с валютой {currency}"):
            product_prices = main_page.get_product_prices(currency)

        with allure.step(f"Проверка наличия символа валюты {currency} в ценах"):
            for price in product_prices:
                assert currency in price.text, (
                    f"Цена {price.text} не содержит {currency}"
                )

    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            main_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))
