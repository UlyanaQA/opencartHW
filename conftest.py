import pytest

from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="choose browser"
    )
    parser.addoption("--headless", action="store_true", help="headless_mode")
    parser.addoption("--url", action="store", default="http://192.168.0.173:8081/")


@pytest.fixture()
def browser(request):
    browser_name = request.config.getoption("browser")
    headless = request.config.getoption("headless")
    url = request.config.getoption("--url")

    if browser_name in ["chrome", "ch"]:
        options = ChromeOptions()
        if headless:
            options.add_argument("--headless=new")
        driver = webdriver.Chrome(options=options)
    elif browser_name in ["edge", "ed"]:
        options = EdgeOptions()
        if headless:
            options.add_argument("--headless")
        driver = webdriver.Edge(options=options)
    else:
        raise ValueError(f"Browser {browser_name} not supported")

    driver.maximize_window()
    request.addfinalizer(driver.close)

    driver.get(url)
    driver.url = url

    return driver
