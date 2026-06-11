from selenium.webdriver.common.by import By


class MainPageLocators:
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    ORDER_FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']")
    PROFILE_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")
    COUNTER = (By.CLASS_NAME, "counter_counter__num__3nue1")
    BASKET_TOP = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")
    BASKET_BOTTOM = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_bottom')]")
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")
    ORDER_MODAL = (By.XPATH, "//section[contains(@class, 'Modal_modal_opened')]")
    ORDER_NUMBER = (By.XPATH, "//h2[contains(@class, 'Modal_modal__title')]")
    CLOSE_MODAL_BUTTON = (By.XPATH, "//button[contains(@class, 'Modal_modal__close')]")


class ResetPasswordPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[text()='Восстановить']")
    PASSWORD_INPUT = (By.XPATH, "//input[@type='password']")
    SHOW_PASSWORD_BUTTON = (By.XPATH, "//div[contains(@class, 'input__icon-action')]")
    PASSWORD_INPUT_ACTIVE = (By.XPATH, "//input[@type='password']/parent::div[contains(@class, 'input_status_active')]")


class ProfilePageLocators:
    ORDER_HISTORY_LINK = (By.XPATH, "//a[text()='История заказов']")
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")


class OrderFeedPageLocators:
    ORDER_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li")
    ORDER_NUMBER_IN_FEED = (By.XPATH, "//ul[contains(@class, 'OrderFeed_list')]/li//p[contains(@class, 'text_type_digits-default')]")
    TOTAL_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[1]")
    TODAY_COUNTER = (By.XPATH, "(//p[contains(@class, 'OrderFeed_number')])[2]")
    IN_WORK_LIST = (By.XPATH, "//ul[contains(@class, 'OrderFeed_orderList')]/li")