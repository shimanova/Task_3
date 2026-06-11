from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def open_url(self, url):
        with allure.step(f"Открытие URL: {url}"):
            self.driver.get(url)

    def click_element(self, locator):
        with allure.step(f"Клик на элемент: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            element.click()

    def send_keys(self, locator, text):
        with allure.step(f"Ввод текста '{text}' в поле: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            element.clear()
            element.send_keys(text)

    def get_text(self, locator):
        with allure.step(f"Получение текста из элемента: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            return element.text

    def is_element_displayed(self, locator):
        with allure.step(f"Проверка отображения элемента: {locator}"):
            try:
                return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
            except:
                return False

    def get_current_url(self):
        with allure.step("Получение текущего URL"):
            return self.driver.current_url

    def wait_for_url_to_be(self, url, timeout=20):
        with allure.step(f"Ожидание URL: {url}"):
            WebDriverWait(self.driver, timeout).until(
                EC.url_to_be(url)
            )

    def close_modal_if_exists(self):
        with allure.step("Закрытие модального окна, если оно открыто"):
            try:
                close_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
                if close_button.is_displayed():
                    close_button.click()
                    time.sleep(0.5)
            except:
                pass
            try:
                self.driver.execute_script("""
                    var modal = document.querySelector('.Modal_modal_opened');
                    if (modal) modal.remove();
                    var overlay = document.querySelector('.Modal_modal_overlay__x2ZCr');
                    if (overlay) overlay.remove();
                """)
            except:
                pass