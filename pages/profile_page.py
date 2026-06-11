from pages.base_page import BasePage
from locators import ProfilePageLocators
import allure
from selenium.webdriver.support import expected_conditions as EC


class ProfilePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_history(self):
        with allure.step("Клик на 'История заказов'"):
            self.close_modal_if_exists()
            element = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.ORDER_HISTORY_LINK))
            self.driver.execute_script("arguments[0].click();", element)

    def click_logout(self):
        with allure.step("Клик на кнопку 'Выход'"):
            self.close_modal_if_exists()
            element = self.wait.until(EC.element_to_be_clickable(ProfilePageLocators.LOGOUT_BUTTON))
            self.driver.execute_script("arguments[0].click();", element)