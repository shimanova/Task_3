import allure
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from pages.login_page import LoginPage
from constants import Urls


@allure.feature("Личный кабинет")
class TestProfile:

    @allure.title("Переход по клику на «Личный кабинет»")
    def test_go_to_profile(self, driver):
        main_page = MainPage(driver)
        main_page.open_url(Urls.MAIN_PAGE)
        main_page.close_modal_if_exists()   # закрываем возможное модальное окно (особенно для Firefox)
        main_page.click_profile()
        
        main_page.wait_for_url_contains("login")
        current_url = main_page.get_current_url()
        assert "login" in current_url or "account" in current_url

    @allure.title("Переход в раздел «История заказов» для авторизованного пользователя")
    def test_go_to_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        profile_page = ProfilePage(driver)
        profile_page.open_url(Urls.PROFILE_PAGE)
        profile_page.close_modal_if_exists()
        profile_page.click_order_history()
        
        profile_page.wait_for_url_contains("order-history")
        assert "order-history" in profile_page.get_current_url()

    @allure.title("Выход из аккаунта для авторизованного пользователя")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        profile_page = ProfilePage(driver)
        profile_page.open_url(Urls.PROFILE_PAGE)
        profile_page.click_logout()
        
        profile_page.wait_for_url_to_be(Urls.LOGIN_PAGE)
        assert profile_page.get_current_url() == Urls.LOGIN_PAGE