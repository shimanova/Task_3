import allure
from pages.order_feed_page import OrderFeedPage
from pages.main_page import MainPage
from pages.login_page import LoginPage
from constants import Urls


@allure.feature("Лента заказов")
class TestOrderFeed:

    @allure.title("Заказы пользователя из истории отображаются в ленте")
    def test_user_orders_appear_in_feed(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_order_button()
        order_number = main_page.get_order_number_from_modal()

        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        feed_page.wait_for_order_number_in_feed(order_number)

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    def test_order_number_appears_in_work_section(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_order_button()
        order_number = main_page.get_order_number_from_modal()

        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        feed_page.wait_for_order_number_in_work(order_number)

    @allure.title("При создании заказа счётчик «Выполнено за всё время» увеличивается")
    def test_total_counter_increases_on_new_order(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        initial_total = feed_page.get_total_counter()

        login_page = LoginPage(driver)
        login_page.login()

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_order_button()
        main_page.get_order_number_from_modal()

        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        feed_page.wait_for_total_counter_increase(initial_total)
        
        assert feed_page.get_total_counter() > initial_total

    @allure.title("При создании заказа счётчик «Выполнено за сегодня» увеличивается")
    def test_today_counter_increases_on_new_order(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        initial_today = feed_page.get_today_counter()

        login_page = LoginPage(driver)
        login_page.login()

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_order_button()
        main_page.get_order_number_from_modal()

        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        feed_page.wait_for_today_counter_increase(initial_today)
        
        assert feed_page.get_today_counter() > initial_today

    @allure.title("Если кликнуть на заказ, откроется всплывающее окно с деталями")
    def test_click_order_opens_modal(self, driver):
        feed_page = OrderFeedPage(driver)
        feed_page.open_url(Urls.ORDER_FEED_PAGE)
        feed_page.click_first_order()
        
        assert feed_page.is_order_modal_displayed()