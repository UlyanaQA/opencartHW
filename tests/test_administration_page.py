from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_username(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 3)
    username = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-username"))
    )
    assert username is not None, "На странице не найдено поле ввода имени пользователя"


def test_password(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 3)
    password = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-password"))
    )
    assert password is not None, "На странице не найдено поле ввода пароля"


def test_login_button(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 3)
    login_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".btn.btn-primary"))
    )
    assert login_btn is not None, "На странице не найдена кнопка логина"


def test_form_header(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 3)
    header = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, ".card-header"))
    )
    assert header is not None, "На странице не найден заголовок окна логина"


def test_home_button(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 3)
    home_btn = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#header a"))
    )
    assert home_btn is not None, (
        "На странице не найдена кнопка возврата на главную страницу"
    )
