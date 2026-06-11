from pages.base_page import BasePage
from locators import OrderFeedPageLocators, MainPageLocators
import allure
from selenium.webdriver.support.ui import WebDriverWait


class OrderFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def get_orders_list(self):
        with allure.step("Получение списка заказов в ленте"):
            return self.driver.find_elements(*OrderFeedPageLocators.ORDER_LIST)

    def get_first_order_number(self):
        with allure.step("Получение номера первого заказа в ленте"):
            numbers = self.driver.find_elements(*OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
            return int(numbers[0].text) if numbers else None

    def get_total_counter(self):
        with allure.step("Получение значения счётчика 'Выполнено за всё время'"):
            text = self.get_text(OrderFeedPageLocators.TOTAL_COUNTER)
            return int(text)

    def get_today_counter(self):
        with allure.step("Получение значения счётчика 'Выполнено за сегодня'"):
            text = self.get_text(OrderFeedPageLocators.TODAY_COUNTER)
            return int(text)

    def get_in_work_orders(self):
        with allure.step("Получение списка заказов 'В работе'"):
            return self.driver.find_elements(*OrderFeedPageLocators.IN_WORK_LIST)

    def wait_for_order_number_in_feed(self, expected_number, timeout=45):
        with allure.step(f"Ожидание появления заказа #{expected_number} в ленте"):
            formatted_number = f"{expected_number:05d}"
            self.wait.until(lambda d: any(
                formatted_number in el.text or str(expected_number) in el.text
                for el in d.find_elements(*OrderFeedPageLocators.ORDER_NUMBER_IN_FEED)
            ))

    def wait_for_order_number_in_work(self, expected_number, timeout=45):
        with allure.step(f"Ожидание появления заказа #{expected_number} в разделе 'В работе'"):
            formatted_number = f"{expected_number:05d}"
            WebDriverWait(self.driver, timeout).until(
                lambda d: any(
                    formatted_number in el.text or str(expected_number) in el.text
                    for el in d.find_elements(*OrderFeedPageLocators.IN_WORK_LIST)
                )
            )

    def click_first_order(self):
        with allure.step("Клик на первый заказ в ленте"):
            self.close_modal_if_exists()  # <--- добавил закрытие модалки перед кликом
            orders = self.get_orders_list()
            if orders:
                orders[0].click()