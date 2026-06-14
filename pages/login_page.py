from pages.base_page import BasePage
from locators import LoginPageLocators
from constants import Urls, TestUser
import allure


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_restore_password_link(self):
        with allure.step("Клик на ссылку 'Восстановить пароль'"):
            self.js_click(LoginPageLocators.RESTORE_PASSWORD_LINK)

    def login(self, email=TestUser.EMAIL, password=TestUser.PASSWORD):
        with allure.step(f"Авторизация пользователя {email}"):
            self.open_url(Urls.LOGIN_PAGE)
            self.close_modal_if_exists()
            self.send_keys(LoginPageLocators.EMAIL_INPUT, email)
            self.send_keys(LoginPageLocators.PASSWORD_INPUT, password)
            self.close_modal_if_exists()
            self.click_element(LoginPageLocators.LOGIN_BUTTON)
            self.wait_for_url_to_be(Urls.MAIN_PAGE)