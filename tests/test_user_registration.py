import allure
import pytest
import uuid


@allure.epic("Регистрация пользователей")
@allure.feature("Процесс регистрации нового пользователя")
@allure.story("Проверка создания учетной записи с уникальными данными")
@pytest.mark.parametrize(
    "firstname, lastname, email, password",
    [
        (
            f"Test1_{uuid.uuid4().hex[:6]}",
            f"Testov1_{uuid.uuid4().hex[:6]}",
            f"test1_{uuid.uuid4().hex[:6]}@mail.ru",
            "password123",
        )
    ],
)
def test_add_new_user(register_page, firstname, lastname, email, password):
    with allure.step(f"Регистрация пользователя {email}"):
        register_page.registration_add_user(firstname, lastname, email, password)

    with allure.step("Ожидание сообщения об успешной регистрации"):
        success_message_present = register_page.wait_text(
            "Your Account Has Been Created!"
        )
        assert success_message_present, "Сообщение об успешной регистрации не найдено"
