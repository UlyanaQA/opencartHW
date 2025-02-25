import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# автотест переключения валют: цены на товары меняются на странице каталога
@pytest.mark.parametrize(
    "selected_currency, currency", [("EUR", "€"), ("USD", "$"), ("GBP", "£")]
)
def test_changing_currency(browser, selected_currency, currency):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 3)
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
    wait.until(EC.visibility_of_element_located((By.ID, "product-category")))
    desktops_prices = wait.until(
        EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='price']"))
    )
    for price in desktops_prices:
        assert currency in price.text, f"Цена {price.text} не обновилась до {currency}"
