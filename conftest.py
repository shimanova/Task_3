import pytest
import requests
from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Urls, TestUser
import allure


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")


@pytest.fixture
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture
def driver(browser):
    with allure.step(f"Запуск браузера: {browser}"):
        if browser == "chrome":
            driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        elif browser == "firefox":
            driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
        else:
            raise ValueError(f"Unsupported browser: {browser}")
        driver.maximize_window()
        yield driver
        driver.quit()


@pytest.fixture
def auth_driver(driver):
    with allure.step("Создание пользователя через API"):
        payload = {
            "email": TestUser.EMAIL,
            "password": TestUser.PASSWORD,
            "name": TestUser.NAME
        }
        response = requests.post(Urls.API_REGISTER, json=payload)
        if response.status_code != 200:
            response = requests.post(Urls.API_LOGIN, json=payload)
        
        token = response.json().get("accessToken") if response.status_code == 200 else None
        
        if token:
            driver.get(Urls.MAIN_PAGE)
            driver.execute_script(f"window.localStorage.setItem('accessToken', '{token}')")
            driver.refresh()
            WebDriverWait(driver, 10).until(
                lambda d: "account" in d.current_url or d.find_elements(By.XPATH, "//p[text()='Личный Кабинет']")
            )
    
    yield driver