import allure
from pages.main_page import MainPage
from pages.login_page import LoginPage
from constants import Urls


@allure.feature("Основная функциональность")
class TestMainFunctionality:

    @allure.title("Переход по клику на «Конструктор»")
    def test_click_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        current_url_before = main_page.get_current_url()
        
        main_page.click_constructor()
        
        assert main_page.get_current_url() == current_url_before

    @allure.title("Переход по клику на «Лента заказов»")
    def test_click_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.click_order_feed()
        
        main_page.wait_for_url_to_be(Urls.ORDER_FEED_PAGE)
        assert driver.current_url == Urls.ORDER_FEED_PAGE

    @allure.title("Клик на ингредиент открывает всплывающее окно с деталями")
    def test_click_ingredient_opens_modal(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.click_ingredient(0)
        
        assert main_page.is_ingredient_modal_displayed()

    @allure.title("Всплывающее окно с деталями ингредиента закрывается кликом по крестику")
    def test_ingredient_modal_closes_by_cross(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.click_ingredient(0)
        
        assert main_page.is_ingredient_modal_displayed()
        
        main_page.close_ingredient_modal()
        
        assert not main_page.is_ingredient_modal_displayed()

    @allure.title("Залогиненный пользователь может оформить заказ")
    def test_logged_in_user_can_create_order(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        main_page = MainPage(driver)
        main_page.add_bun_to_basket()
        main_page.add_filling_to_basket()
        main_page.click_order_button()
        order_number = main_page.get_order_number_from_modal()
        
        assert order_number > 0