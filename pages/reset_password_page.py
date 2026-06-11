from pages.base_page import BasePage
from locators import ResetPasswordPageLocators
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        with allure.step(f"Ввод email: {email}"):
            self.send_keys(ResetPasswordPageLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        with allure.step("Клик на кнопку 'Восстановить'"):
            self.close_modal_if_exists()
            element = self.wait.until(EC.element_to_be_clickable(ResetPasswordPageLocators.RESTORE_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)  # <--- JS-клик

    def is_password_field_displayed(self):
        with allure.step("Проверка отображения поля ввода пароля"):
            return self.is_element_displayed(ResetPasswordPageLocators.PASSWORD_INPUT)

    def click_show_password_button(self):
        with allure.step("Клик на кнопку показать/скрыть пароль"):
            self.close_modal_if_exists()
            element = self.wait.until(EC.element_to_be_clickable(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)  # <--- JS-клик

    def is_password_field_active(self):
        with allure.step("Проверка, что поле пароля активно (подсвечено)"):
            active_field = (By.XPATH, "/html/body/div/div/main/div/form/fieldset[1]/div/div/input")
            return self.is_element_displayed(active_field)