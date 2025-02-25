from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# автотест логина-разлогина в админку с проверкой, что логин был выполнен
def test_username(browser):
    browser.get(browser.url + "/administration")
    wait = WebDriverWait(browser, 3)
    username = browser.find_element(By.CSS_SELECTOR, "#input-username.form-control")
    username.clear()
    username.send_keys("user")
    password = browser.find_element(By.CSS_SELECTOR, "#input-password.form-control")
    password.clear()
    password.send_keys("bitnami")
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_btn.click()
    logout_btn = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#nav-logout.nav-item"))
    )
    logout_btn.click()
    login_form = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#form-login"))
    )
    assert login_form.is_displayed(), "Форма входа не отображается после выхода"
