import logging
import uuid
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from page_objects.admin_login_page import AdminLoginPage
from page_objects.administration_page import AdministrationPage
from page_objects.catalog_page import CatalogPage
from page_objects.main_page import MainPage
from page_objects.product_page import ProductPage
from page_objects.register_page import RegisterPage


logging.basicConfig(level=logging.INFO)


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="choose browser"
    )
    parser.addoption("--headless", action="store_true", help="headless_mode")
    parser.addoption("--url", action="store", default="http://192.168.31.244:8081/")
    parser.addoption(
        "--log_level", action="store", default="INFO", help="choose log level"
    )


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    url = request.config.getoption("--url")

    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)

    user_data_dir = f"/tmp/{uuid.uuid4().hex}"

    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
            options.add_argument("--disable-dev-shm-usage")
            options.add_argument("--remote-debugging-port=9222")
        else:
            options.add_argument("--window-size=1920,1080")

        options.binary_location = "/usr/bin/chromium"
        options.add_argument(f"--user-data-dir={user_data_dir}")

        service = ChromeService(executable_path="/usr/bin/chromedriver")
        driver = webdriver.Chrome(service=service, options=options)

    elif browser_name in ["firefox", "ff"]:
        options = FirefoxOptions()
        if headless:
            options.add_argument("--headless")
            options.add_argument("--disable-gpu")
            options.add_argument("--no-sandbox")
        else:
            options.add_argument("--width=1920")
            options.add_argument("--height=1080")

        options.add_argument(f"user-data-dir={user_data_dir}")
        options.binary_location = "/usr/bin/firefox"

        service = FirefoxService(executable_path="/usr/bin/geckodriver")
        driver = webdriver.Firefox(service=service, options=options)

    else:
        raise ValueError(f"Браузер {browser_name} не поддерживается")

    driver.maximize_window()
    request.addfinalizer(driver.quit)

    logger.info(f"Открытие адреса: {url}")
    driver.get(url)
    driver.url = url


@pytest.fixture
def logger(request):
    log_level = request.config.getoption("--log_level")
    logger = logging.getLogger(__name__)
    logger.setLevel(level=log_level)
    return logger


@pytest.fixture
def base_url(request, logger) -> str:
    return request.config.getoption("--url")


@pytest.fixture
def admin_login_page(browser, base_url, logger):
    page = AdminLoginPage(browser)
    administration_url = f"{base_url}/administration"

    logger.info(f"Открытие страницы админа: {administration_url}")
    page.open(administration_url)
    return page


@pytest.fixture
def administration_page(browser, base_url, logger):
    administration_page = AdministrationPage(browser)
    admin_page = AdminLoginPage(browser)
    admin_page.open(f"{base_url}/administration")

    logger.info("Авторизация как 'user' с паролем 'bitnami'")
    admin_page.login("user", "bitnami")

    logger.info("Переход на страницу продуктов после логина")
    administration_page.administration_go_to_product_page()

    return administration_page


@pytest.fixture
def catalog_desktops_page(browser, base_url, logger):
    page = CatalogPage(browser)
    catalog_desktops_url = f"{base_url}/en-gb/catalog/desktops"

    logger.info(f"Открытие каталога desktops: {catalog_desktops_url}")
    page.open(catalog_desktops_url)

    return page


@pytest.fixture
def catalog_laptops_page(browser, base_url, logger):
    page = CatalogPage(browser)
    catalog_laptops_url = f"{base_url}/en-gb/catalog/laptop-notebook"

    logger.info(f"Открытие каталога laptops: {catalog_laptops_url}")
    page.open(catalog_laptops_url)

    return page


@pytest.fixture
def main_page(browser, base_url, logger):
    page = MainPage(browser)
    mainpage_url = f"{base_url}"

    logger.info(f"Открытие главной страницы: {mainpage_url}")
    page.open(base_url)

    return page


@pytest.fixture
def product_page(browser, base_url, logger):
    page = ProductPage(browser)
    product_url = f"{base_url}/en-gb/product/desktops/apple-cinema"

    logger.info(f"Открытие каталога: {product_url}")
    page.open(product_url)

    return page


@pytest.fixture
def register_page(browser, base_url, logger):
    page = RegisterPage(browser)
    register_url = f"{base_url}/index.php?route=account/register"

    logger.info(f"Открытие страницы регистрации: {register_url}")
    page.open(register_url)

    return page


@pytest.fixture
def create_product(administration_page, logger):
    product_name = f"prod7_{uuid.uuid4().hex[:6]}"  # Уникальное имя продукта
    meta_tag = f"meta_tag_{uuid.uuid4().hex[:6]}"
    model = f"model_{uuid.uuid4().hex[:6]}"
    keyword = f"keyword_{uuid.uuid4().hex[:6]}"

    logger.info(f"Создание нового продукта: {product_name}")
    administration_page.products_click_add_new_product()
    administration_page.products_add_new_product(product_name, meta_tag, model, keyword)

    administration_page.administration_go_to_product_page()

    yield product_name
