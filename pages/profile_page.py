from pages.base_page import BasePage
from locators import ProfilePageLocators
import allure


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_history(self):
        with allure.step("Клик на 'История заказов'"):
            self.close_modal_if_exists()
            self.js_click(ProfilePageLocators.ORDER_HISTORY_LINK)

    def click_logout(self):
        with allure.step("Клик на кнопку 'Выход'"):
            self.close_modal_if_exists()
            self.js_click(ProfilePageLocators.LOGOUT_BUTTON)