from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_button(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    research_button = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#search button"))
    )
    assert research_button is not None, "На странице не найдена кнопка поиска"


def test_top_navigation(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    top_nav = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#top .float-end ul"))
    )
    assert top_nav is not None, "На странице не найдено верхнее навигационное меню"


def test_currency(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    curr_list = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-currency"))
    )
    assert curr_list is not None, "На странице не найден выбор валюты"


def test_menu(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "ul.nav.navbar-nav")))
    menu_items = browser.find_elements(By.CSS_SELECTOR, "ul.nav.navbar-nav > li")
    for index, item in enumerate(menu_items, start=1):
        item_text = item.text.strip()
        assert item_text, f"Пункт меню #{index} пустой или не содержит видимого текста"


def test_goodscards(browser):
    browser.get(browser.url)
    wait = WebDriverWait(browser, 3)
    goods_cards = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "footer h5"))
    )
    assert goods_cards is not None, "На странице не найден выбор валюты"
