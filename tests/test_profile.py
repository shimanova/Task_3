import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
        main_page.click_profile()
        assert "login" in driver.current_url or "account" in driver.current_url

    @allure.title("Переход в раздел «История заказов» для авторизованного пользователя")
    def test_go_to_order_history(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        profile_page = ProfilePage(driver)
        profile_page.open_url(Urls.PROFILE_PAGE)
        profile_page.close_modal_if_exists()  # <--- добавить
        profile_page.click_order_history()
        assert "order-history" in driver.current_url

    @allure.title("Выход из аккаунта для авторизованного пользователя")
    def test_logout(self, driver):
        login_page = LoginPage(driver)
        login_page.login()

        profile_page = ProfilePage(driver)
        profile_page.open_url(Urls.PROFILE_PAGE)
        profile_page.click_logout()
        WebDriverWait(driver, 20).until(
            EC.url_to_be(Urls.LOGIN_PAGE)
        )
        assert driver.current_url == Urls.LOGIN_PAGE