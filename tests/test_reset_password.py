import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.reset_password_page import ResetPasswordPage
from constants import Urls, ResetPasswordData


@allure.feature("Восстановление пароля")
class TestResetPassword:

    @allure.title("Переход на страницу восстановления пароля по кнопке «Восстановить пароль»")
    def test_go_to_reset_password_page(self, driver):
        driver.get(Urls.LOGIN_PAGE)
        reset_page = ResetPasswordPage(driver)
        reset_page.close_modal_if_exists()
        restore_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='Восстановить пароль']"))
        )
        driver.execute_script("arguments[0].click();", restore_link)  # <-- JS клик
        assert driver.current_url == Urls.RESET_PASSWORD_PAGE

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