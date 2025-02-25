import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# автотест переключения валют: цены на товары меняются на главной
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(browser, selected_currency, currency):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 10)
    currency_switcher = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#form-currency"))
    )
    currency_switcher.click()
    currency_choice = wait.until(
        EC.visibility_of_element_located(
            (By.CSS_SELECTOR, f"a[href='{selected_currency}']")
        )
    )
    currency_choice.click()
    product_prices = wait.until(
        EC.visibility_of_all_elements_located(
            (By.XPATH, f"//span[contains(text(), '{currency}')]")
        )
    )
    for price in product_prices:
        assert currency in price.text, f"Цена {price.text} не содержит {currency}"
