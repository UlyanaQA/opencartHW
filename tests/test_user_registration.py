from page_objects.register_page import RegisterPage


# Регистрация нового пользователя в магазине opencart
def test_add_new_user(browser):
    firstname = "Test12"
    lastname = "Testov12"
    email = "test12@mail.ru"
    password = "12345678"
    register_page = RegisterPage(browser)
    register_page.open_register_page(browser.url + "/index.php?route=account/register")
    register_page.registration_add_user(firstname, lastname, email, password)
    success_message_present = register_page.wait_text("Your Account Has Been Created!")
    assert success_message_present, "Сообщение об успешной регистрации не найдено"
