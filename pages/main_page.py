from pages.base_page import BasePage
from locators import MainPageLocators
from data import OrderData
import allure
from helpers import drag_and_drop
from selenium.webdriver.support import expected_conditions as EC


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_constructor(self):
        with allure.step("Клик на кнопку 'Конструктор'"):
            self.click_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    def click_order_feed(self):
        with allure.step("Клик на кнопку 'Лента заказов'"):
            self.click_element(MainPageLocators.ORDER_FEED_BUTTON)

    def click_profile(self):
        with allure.step("Клик на кнопку 'Личный кабинет'"):
            self.click_element(MainPageLocators.PROFILE_BUTTON)

    def click_ingredient(self, index=0):
        with allure.step(f"Клик на ингредиент с индексом {index}"):
            ingredients = self.driver.find_elements(*MainPageLocators.INGREDIENT)
            if ingredients:
                ingredients[index].click()

    def close_modal(self):
        with allure.step("Закрытие модального окна"):
            self.click_element(MainPageLocators.CLOSE_MODAL_BUTTON)

    def is_modal_displayed(self):
        with allure.step("Проверка отображения модального окна"):
            return self.is_element_displayed(MainPageLocators.ORDER_MODAL)

    def add_bun_to_basket(self):
        with allure.step("Перетаскивание булки в конструктор"):
            drag_and_drop(self.driver, OrderData.BUN_INGREDIENT, MainPageLocators.BASKET_TOP)

    def add_filling_to_basket(self):
        with allure.step("Перетаскивание начинки/соуса в конструктор"):
            drag_and_drop(self.driver, OrderData.FILLING_INGREDIENT, MainPageLocators.BASKET_TOP)

    def get_counter_value(self, index=0):
        with allure.step(f"Получение значения счётчика ингредиента с индексом {index}"):
            counters = self.driver.find_elements(*MainPageLocators.COUNTER)
            return int(counters[index].text) if counters else 0

    def click_order_button(self):
        with allure.step("Клик на кнопку 'Оформить заказ'"):
            button = self.wait.until(EC.presence_of_element_located(MainPageLocators.ORDER_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", button)
            self.driver.execute_script("arguments[0].click();", button)

    def get_order_number_from_modal(self):
        with allure.step("Получение номера заказа из модального окна"):
            self.wait.until(lambda d: d.find_element(*MainPageLocators.ORDER_MODAL).is_displayed())
            order_text = self.get_text(MainPageLocators.ORDER_NUMBER)
            self.close_modal_if_exists()  # <--- Закрываем окно после получения номера
            return int(order_text)