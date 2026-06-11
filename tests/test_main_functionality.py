import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from pages.login_page import LoginPage
from constants import Urls
from locators import MainPageLocators


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_order_button()
        order_number = main_page.get_order_number_from_modal()  # здесь уже закрывается окно
        assert order_number > 0