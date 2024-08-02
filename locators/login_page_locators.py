from selenium.webdriver.common.by import By

class LoginPageLocator:

    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    EYE_BUTTON = By.XPATH, "//div[contains(@class, 'input__icon-action')]"
    NEW_PASSWORD_FIELD = By.XPATH, ".//label[text()='Пароль']"
    RECOVERY_PASSWORD_BLOCK = By.XPATH, "//*[contains(@class, 'button_button') and text()='Восстановить']"
    RECOVERY_PASSWORD_BUTTON = By.XPATH, "//*[@href= '/forgot-password']"
    PASSWORD_RECOVERY_FIELD = By.XPATH, "//input[@name= 'name']"
    PASSWORD_RECOVERY_BUTTON = By.XPATH, "//button[text()= 'Восстановить']"
    CODE_FROM_EMAIL = By.XPATH, ".//label[text()= 'Введите код из письма']"
    LAYER_TO_WAIT = By.XPATH, ".//*[contains(@class, 'Modal_modal__loading')]/following::div[@class='Modal_modal_overlay__x2ZCr']"