import time
import allure


# Добавление в корзину товара с главной страницы и проверка того, что он появился в корзине
@allure.epic("Главная страница")
@allure.feature("Добавление товара в корзину")
@allure.story("Проверка добавления товара с главной страницы")
def test_add_product_to_cart(main_page):
    with allure.step("Добавление товара в корзину"):
        main_page.add_product_to_cart()

    with allure.step("Ожидание исчезновения уведомления об успешном добавлении"):
        main_page.wait_for_success_alert_disappear()
        time.sleep(0.7)

    with allure.step("Проверка текста корзины"):
        cart_text = main_page.get_cart_items_count_and_price()
        expected_text = "1 item(s) - $602.00"
        assert cart_text == expected_text, (
            f"Ожидаемая сумма: '{expected_text}', Фактическая: '{cart_text}'"
        )
