import allure
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from constants import Urls
from locators import MainPageLocators, OrderFeedPageLocators
from helpers import drag_and_drop


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Заказы пользователя из истории отображаются в ленте")
    def test_user_orders_appear_in_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.login()
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        time.sleep(2)
        main_page.add_filling_to_basket()
        time.sleep(2)
        main_page.click_order_button()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )
        order_number = main_page.get_order_number_from_modal()
        main_page.close_modal_if_exists()
        time.sleep(2)

        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        feed_page.wait_for_order_number_in_feed(order_number)
        assert True

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_work_section(self, driver):
        login_page = LoginPage(driver)
        login_page.login()
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        time.sleep(2)
        main_page.add_filling_to_basket()
        time.sleep(2)
        main_page.click_order_button()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )
        order_number = main_page.get_order_number_from_modal()
        main_page.close_modal_if_exists()
        time.sleep(2)

        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        feed_page.wait_for_order_number_in_work(order_number)
        assert True

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_counter_increases_on_new_order(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        initial_total = feed_page.get_total_counter()
        time.sleep(2)

        login_page = LoginPage(driver)
        login_page.login()
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        time.sleep(2)
        main_page.add_filling_to_basket()
        time.sleep(2)
        main_page.click_order_button()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )
        main_page.get_order_number_from_modal()
        main_page.close_modal_if_exists()
        time.sleep(2)

        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        WebDriverWait(driver, 45).until(
            lambda d: feed_page.get_total_counter() > initial_total
        )
        assert feed_page.get_total_counter() > initial_total

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases_on_new_order(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        initial_today = feed_page.get_today_counter()
        time.sleep(2)

        login_page = LoginPage(driver)
        login_page.login()
        time.sleep(2)

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        time.sleep(2)
        main_page.add_filling_to_basket()
        time.sleep(2)
        main_page.click_order_button()
        time.sleep(2)
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_MODAL)
        )
        main_page.get_order_number_from_modal()
        main_page.close_modal_if_exists()
        time.sleep(2)

        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        driver.refresh()
        time.sleep(2)
        WebDriverWait(driver, 45).until(
            lambda d: feed_page.get_today_counter() > initial_today
        )
        assert feed_page.get_today_counter() > initial_today

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        time.sleep(2)
        feed_page.click_first_order()
        time.sleep(2)
        assert feed_page.is_element_displayed((By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]"))