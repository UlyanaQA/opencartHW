from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_sort_list(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 3)
    sort_list = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#input-sort"))
    )
    assert sort_list is not None, "На странице не найдено поле сортировки"


def test_compare_button(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 3)
    sort_list = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#compare-total"))
    )
    assert sort_list is not None, "На странице не найдена кнопка сравнения"


def test_home_button(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 3)
    home_button = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#product-category > ul > li:nth-child(1)")
        )
    )
    assert home_button is not None, (
        "На странице не найдена кнопка возвращения на главную страницу"
    )


def test_left_menu(browser):
    browser.get(browser.url + "/en-gb/catalog/desktops")
    wait = WebDriverWait(browser, 3)
    left_menu = wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "#column-left > div.list-group.mb-3")
        )
    )
    assert left_menu is not None, "На странице не найден список категорий товаров"


def test_laptop_category(browser):
    wait = WebDriverWait(browser, 3)
    browser.get(browser.url + "/en-gb/catalog/laptop-notebook")
    wait.until(
        EC.presence_of_element_located(
            (By.CSS_SELECTOR, "div.list-group.mb-3 > a[href*='laptop-notebook/']")
        )
    )
    laptop_category = browser.find_elements(
        By.CSS_SELECTOR, "div.list-group.mb-3 > a[href*='laptop-notebook/']"
    )
    assert len(laptop_category) == 2, (
        "В каталоге Laptops & Notebooks должно быть 2 категории"
    )
