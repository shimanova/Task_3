class Urls:
    BASE_URL = "https://qa-stellarburgers.education-services.ru"
    MAIN_PAGE = f"{BASE_URL}/"
    LOGIN_PAGE = f"{BASE_URL}/login"
    RESET_PASSWORD_PAGE = f"{BASE_URL}/forgot-password"
    PROFILE_PAGE = f"{BASE_URL}/account"
    ORDER_HISTORY_PAGE = f"{BASE_URL}/account/order-history"
    ORDER_FEED_PAGE = f"{BASE_URL}/feed"
    
    API_REGISTER = f"{BASE_URL}/api/auth/register"
    API_LOGIN = f"{BASE_URL}/api/auth/login"
    API_USER = f"{BASE_URL}/api/auth/user"


class TestUser:
    EMAIL = "test_user_auto_123@test.ru"
    PASSWORD = "password123"
    NAME = "TestUserAuto"


class ResetPasswordData:
    EMAIL = "test_user_auto_123@test.ru"