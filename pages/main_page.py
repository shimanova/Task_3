from pages.base_page import BasePage
from locators import MainPageLocators
from data import OrderData
import allure
import re
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
            self.close_modal_if_exists()
            ingredients = self.get_elements(MainPageLocators.INGREDIENT)
            if ingredients and index < len(ingredients):
                ingredients[index].click()
                self.wait_for_element_visible(MainPageLocators.INGREDIENT_MODAL)

    def is_ingredient_modal_displayed(self):
        with allure.step("Проверка отображения модального окна с деталями ингредиента"):
            return self.is_element_displayed(MainPageLocators.INGREDIENT_MODAL)

    def close_ingredient_modal(self):
        with allure.step("Закрытие модального окна с деталями ингредиента"):
            self.click_element(MainPageLocators.INGREDIENT_MODAL_CLOSE_BUTTON)

    def add_bun_to_basket(self):
        with allure.step("Перетаскивание булки в конструктор"):
            drag_and_drop(self.driver, OrderData.BUN_INGREDIENT, MainPageLocators.BASKET_TOP)

    def add_filling_to_basket(self):
        with allure.step("Перетаскивание начинки/соуса в конструктор"):
            drag_and_drop(self.driver, OrderData.FILLING_INGREDIENT, MainPageLocators.BASKET_TOP)

    def get_counter_value(self, index=0):
        with allure.step(f"Получение значения счётчика ингредиента с индексом {index}"):
            counters = self.get_elements(MainPageLocators.COUNTER)
            return int(counters[index].text) if counters and index < len(counters) else 0

    def click_order_button(self):
        with allure.step("Клик на кнопку 'Оформить заказ'"):
            self.scroll_to_element(MainPageLocators.ORDER_BUTTON)
            self.js_click(MainPageLocators.ORDER_BUTTON)

    def get_order_number_from_modal(self):
        with allure.step("Получение номера заказа из модального окна"):
            self.wait_for_element_visible(MainPageLocators.ORDER_MODAL)
            number_element = self.wait.until(
                EC.presence_of_element_located(MainPageLocators.ORDER_NUMBER)
            )
            # Ждём, пока текст не станет содержать число, отличное от временной заглушки
            self.wait.until(
                lambda d: (text := number_element.text.strip()) != "" and
                          (digits := re.findall(r'\d+', text)) and
                          int(digits[0]) != 9999
            )
            text = number_element.text
            digits = re.findall(r'\d+', text)
            if not digits:
                inner_text = self.driver.execute_script("return arguments[0].innerText;", number_element)
                digits = re.findall(r'\d+', inner_text)
            if not digits:
                raise AssertionError("Не удалось найти номер заказа в модальном окне")
            order_number = int(digits[0])
            self.close_modal_if_exists()
            return order_number