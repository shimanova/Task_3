from pages.base_page import BasePage
from locators import ResetPasswordPageLocators
import allure


class ResetPasswordPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def enter_email(self, email):
        with allure.step(f"Ввод email: {email}"):
            self.send_keys(ResetPasswordPageLocators.EMAIL_INPUT, email)

    def click_restore_button(self):
        with allure.step("Клик на кнопку 'Восстановить'"):
            self.close_modal_if_exists()
            self.js_click(ResetPasswordPageLocators.RESTORE_BUTTON)
            self.wait_for_element_visible(ResetPasswordPageLocators.PASSWORD_INPUT)

    def is_password_field_displayed(self):
        with allure.step("Проверка отображения поля ввода пароля"):
            return self.is_element_displayed(ResetPasswordPageLocators.PASSWORD_INPUT)

    def click_show_password_button(self):
        with allure.step("Клик на кнопку показать/скрыть пароль"):
            self.close_modal_if_exists()
            self.js_click(ResetPasswordPageLocators.SHOW_PASSWORD_BUTTON)

    def is_password_field_active(self):
        with allure.step("Проверка, что поле пароля активно (подсвечено)"):
            return self.is_element_has_class(ResetPasswordPageLocators.PASSWORD_FIELD_CONTAINER, "input_status_active")