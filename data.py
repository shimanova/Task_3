from selenium.webdriver.common.by import By


class OrderData:
    BUN_INGREDIENT = (By.XPATH, "//a[contains(@href, '/ingredient/691577430cc94f001a65b85a')]")
    FILLING_INGREDIENT = (By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient')]")