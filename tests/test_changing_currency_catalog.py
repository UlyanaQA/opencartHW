import allure
import pytest
import logging


@allure.epic("Страница каталога")
@allure.feature("Изменение цены при смене валюты")
@allure.story("Проверка изменения цены товара при смене валюты")
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(catalog_desktops_page, selected_currency, currency):
    try:
        with allure.step(f"Переключение валюты на {selected_currency}"):
            catalog_desktops_page.switch_currency(selected_currency)

        with allure.step("Ожидание загрузки категории товаров"):
            catalog_desktops_page.wait_for_product_category()

        with allure.step("Проверка обновления цен товаров"):
            desktops_prices = catalog_desktops_page.get_desktops_prices()
            for price in desktops_prices:
                assert currency in price.text, (
                    f"Цена {price.text} не обновилась до {currency}"
                )

    except AssertionError as e:
        logging.error(f"Ошибка в тесте: {str(e)}")

        allure.attach(
            catalog_desktops_page.browser.get_screenshot_as_png(),
            name="screenshot_on_failure",
            attachment_type=allure.attachment_type.PNG,
        )

        raise AssertionError(str(e))
