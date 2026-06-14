import allure
from pages.reset_password_page import ResetPasswordPage
from pages.login_page import LoginPage
from constants import Urls, ResetPasswordData


@allure.feature("Восстановление пароля")
class TestResetPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_reset_password_page(self, driver):
        login_page = LoginPage(driver)
        login_page.open_url(Urls.LOGIN_PAGE)
        login_page.close_modal_if_exists()
        login_page.click_restore_password_link()
        
        login_page.wait_for_url_to_be(Urls.RESET_PASSWORD_PAGE)
        assert login_page.get_current_url() == Urls.RESET_PASSWORD_PAGE

    @allure.title("Ввод почты и клик по кнопке «Восстановить»")
    def test_enter_email_and_click_restore(self, driver):
        reset_page = ResetPasswordPage(driver)
        reset_page.open_url(Urls.RESET_PASSWORD_PAGE)
        reset_page.enter_email(ResetPasswordData.EMAIL)
        reset_page.click_restore_button()
        
        assert reset_page.is_password_field_displayed()

    @allure.title("Клик по кнопке показать/скрыть пароль делает поле активным")
    def test_show_password_button_highlights_field(self, driver):
        reset_page = ResetPasswordPage(driver)
        reset_page.open_url(Urls.RESET_PASSWORD_PAGE)
        reset_page.enter_email(ResetPasswordData.EMAIL)
        reset_page.click_restore_button()
        reset_page.click_show_password_button()
        
        assert reset_page.is_password_field_active()