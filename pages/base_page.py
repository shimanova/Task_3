from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
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
            WebDriverWait(self.driver, timeout).until(EC.url_to_be(url))

    def wait_for_url_contains(self, text, timeout=20):
        with allure.step(f"Ожидание URL содержит: {text}"):
            WebDriverWait(self.driver, timeout).until(lambda d: text in d.current_url)

    def wait_for_element_visible(self, locator, timeout=20):
        with allure.step(f"Ожидание видимости элемента: {locator}"):
            return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_elements(self, locator):
        with allure.step(f"Получение списка элементов: {locator}"):
            return self.driver.find_elements(*locator)

    def get_elements_text_list(self, locator):
        with allure.step(f"Получение текстов всех элементов: {locator}"):
            elements = self.get_elements(locator)
            return [el.text for el in elements]

    def wait_for_element_in_list(self, locator, expected_text, timeout=120):
        with allure.step(f"Ожидание номера заказа '{expected_text}' в списке: {locator}"):
            # Форматируем номер с ведущими нулями для поиска (например, 7350 -> "07350")
            formatted_text = f"{expected_text:05d}" if isinstance(expected_text, int) else str(expected_text)

            def condition(driver):
                try:
                    elements = driver.find_elements(*locator)
                    for el in elements:
                        if formatted_text in el.text:
                            return True
                except StaleElementReferenceException:
                    return False
                return False

            try:
                WebDriverWait(self.driver, timeout, poll_frequency=0.5).until(condition)
            except TimeoutException:
                raise TimeoutException(f"Номер заказа {expected_text} не появился в списке за {timeout} секунд")

    def wait_for_element_text_to_change(self, locator, initial_value, timeout=45):
        with allure.step(f"Ожидание изменения текста элемента: {locator} > {initial_value}"):
            WebDriverWait(self.driver, timeout).until(
                lambda d: int(self.get_text(locator)) > initial_value
            )

    def close_modal_if_exists(self):
        with allure.step("Закрытие модального окна, если оно открыто"):
            try:
                close_button = self.driver.find_element(By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")
                if close_button.is_displayed():
                    close_button.click()
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

    def js_click(self, locator):
        with allure.step(f"JavaScript клик на элемент: {locator}"):
            element = self.wait.until(EC.element_to_be_clickable(locator))
            self.driver.execute_script("arguments[0].click();", element)

    def scroll_to_element(self, locator):
        with allure.step(f"Прокрутка к элементу: {locator}"):
            element = self.wait.until(EC.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            return element

    def is_element_has_class(self, locator, class_name):
        with allure.step(f"Проверка наличия класса '{class_name}' у элемента: {locator}"):
            element = self.wait_for_element_visible(locator)
            return class_name in element.get_attribute("class")