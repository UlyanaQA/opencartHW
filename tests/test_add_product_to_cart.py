import time
from page_objects.main_page import MainPage


# Добавление в корзину товара с главной страницы и проверка того, что он появился в корзине
def test_add_product_to_cart(browser):
    main_page = MainPage(browser)
    main_page.open(browser.url)
    main_page.add_product_to_cart()
    main_page.wait_for_success_alert_disappear()
    time.sleep(0.7)
    cart_text = main_page.get_cart_items_count_and_price()
    expected_text = "1 item(s) - $602.00"
    assert cart_text == expected_text, (
        f"Ожидаемая сумма: '{expected_text}', Фактическая: '{cart_text}'"
    )
