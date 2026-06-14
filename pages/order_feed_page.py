from pages.base_page import BasePage
from locators import OrderFeedPageLocators
from constants import Urls
import allure


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_orders_list(self):
        with allure.step("Получение списка заказов в ленте"):
            return self.get_elements(OrderFeedPageLocators.ORDER_LIST)

    def get_total_counter(self):
        with allure.step("Получение значения счётчика 'Выполнено за всё время'"):
            text = self.get_text(OrderFeedPageLocators.TOTAL_COUNTER)
            return int(text)

    def get_today_counter(self):
        with allure.step("Получение значения счётчика 'Выполнено за сегодня'"):
            text = self.get_text(OrderFeedPageLocators.TODAY_COUNTER)
            return int(text)

    def wait_for_order_number_in_feed(self, expected_number, timeout=120):
        with allure.step(f"Ожидание заказа #{expected_number} в ленте"):
            formatted = f"{expected_number:05d}"
            self.wait_for_element_in_list(OrderFeedPageLocators.ORDER_NUMBER_IN_FEED, formatted, timeout)

    def wait_for_order_number_in_work(self, expected_number, timeout=120):
        with allure.step(f"Ожидание заказа #{expected_number} в разделе 'В работе'"):
            formatted = f"{expected_number:05d}"
            self.wait_for_element_in_list(OrderFeedPageLocators.IN_WORK_LIST, formatted, timeout)

    def click_first_order(self):
        with allure.step("Клик на первый заказ в ленте"):
            self.close_modal_if_exists()
            orders = self.get_orders_list()
            if orders:
                self.scroll_to_element(OrderFeedPageLocators.ORDER_LIST)
                orders[0].click()

    def wait_for_total_counter_increase(self, initial_value, timeout=45):
        with allure.step(f"Ожидание увеличения счётчика 'Выполнено за всё время' > {initial_value}"):
            self.wait_for_element_text_to_change(OrderFeedPageLocators.TOTAL_COUNTER, initial_value, timeout)

    def wait_for_today_counter_increase(self, initial_value, timeout=45):
        with allure.step(f"Ожидание увеличения счётчика 'Выполнено за сегодня' > {initial_value}"):
            self.wait_for_element_text_to_change(OrderFeedPageLocators.TODAY_COUNTER, initial_value, timeout)

    def is_order_modal_displayed(self):
        with allure.step("Проверка отображения модального окна с деталями заказа"):
            return self.is_element_displayed(OrderFeedPageLocators.ORDER_DETAIL_MODAL)