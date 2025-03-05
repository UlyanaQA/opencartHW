from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_username(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    username = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-firstname"))
    )
    assert username is not None, (
        "На странице не найдено поле ввода фамилии пользователя"
    )


def test_submit(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    submit_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#form-register button"))
    )
    assert submit_btn is not None, (
        "На странице не найдена кнопка регистрации пользователя"
    )


def test_read_policy(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    read_radiobtn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "input[name='agree']"))
    )
    assert read_radiobtn is not None, (
        "На странице не найден радиобаттон подтверждения прочтения политики конфиденциальности"
    )


def test_right_menu(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    right_menu = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#column-right"))
    )
    assert right_menu is not None, "На странице не найдено меню справа"


def test_required_fields(browser):
    browser.get(browser.url + "/index.php?route=account/register")
    wait = WebDriverWait(browser, 3)
    required_fields = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "#form-register fieldset div.row.mb-3.required")
        )
    )
    assert len(required_fields) == 4, "Обязательных полей должно быть 4"
