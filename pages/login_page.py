from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Urls, TestUser
import allure
import time


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def login(self, email=TestUser.EMAIL, password=TestUser.PASSWORD):
        with allure.step(f"Авторизация пользователя {email}"):
            self.open_url(Urls.LOGIN_PAGE)
            
            # Жёсткое закрытие модального окна (для Firefox)
            try:
                self.driver.execute_script("""
                    var modal = document.querySelector('.Modal_modal_opened');
                    if (modal) modal.remove();
                    var overlay = document.querySelector('.Modal_modal_overlay__x2ZCr');
                    if (overlay) overlay.remove();
                """)
                time.sleep(1)
            except:
                pass
            
            email_input = self.wait.until(EC.visibility_of_element_located((By.XPATH, "//label[text()='Email']/following-sibling::input")))
            email_input.send_keys(email)
            password_input = self.driver.find_element(By.XPATH, "//input[@type='password']")
            password_input.send_keys(password)
            
            # Ещё раз закрываем модалку перед кликом (на всякий случай)
            try:
                self.driver.execute_script("""
                    var overlay = document.querySelector('.Modal_modal_overlay__x2ZCr');
                    if (overlay) overlay.remove();
                """)
                time.sleep(0.5)
            except:
                pass
            
            login_button = self.driver.find_element(By.XPATH, "//button[text()='Войти']")
            login_button.click()
            WebDriverWait(self.driver, 10).until(EC.url_to_be(Urls.MAIN_PAGE))