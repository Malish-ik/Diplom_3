from selenium.webdriver.common.by import By


class OrderFeedPageLocator:
    CONSTRUCTOR_BUTTON = By.XPATH, ".//a[contains(@class, 'AppHeader_header__link') and @href= '/']"
    ASSEMBLE_A_BURGER = By.XPATH, ".//h1[text()='Соберите бургер']"
    ORDERS_FEED_BUTTON = By.XPATH, ".//p[text()= 'Лента Заказов']"
    ORDER_1 = By.XPATH, ".//div[contains(@class, 'OrderHistory_dataBox')]"
    ORDER_INFO = By.XPATH, "//p[text()= 'Cостав']"
    ORDER_HISTORY_NUMBER = By.XPATH, "//a[contains(@class, 'OrderHistory_textBox')]"
    ORDERS_NUMBERS = By.XPATH, "//li[contains(@class, 'text_type_digits-default')]"
    ORDERS_NUMBERS_9999 = By.XPATH, "//h2[contains(@class, 'text_type_digits') and text()= 9999]"
    ID_NEW_ORDER = By.XPATH, "//h2[contains(@class, 'text_type_digits')]"
    CLOSE_BUTTON = By.XPATH, ".//button[@type='button']"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//p[text()='Личный Кабинет']"
    ORDERS_HISTORY_BUTTON = By.XPATH, "//a[@href= '/account/order-history']"
    COUNTER_ALL_TIME = By.XPATH, "//*[text()='Выполнено за все время:']/following-sibling::p"
    COUNTER_TODAY = By.XPATH, "//*[text()='Выполнено за сегодня:']/following-sibling::p"
    ORDERS_IN_WORK = By.XPATH, "//*[contains(@class, 'OrderFeed_orderListReady')]"
    LAYER_TO_WAIT = By.XPATH, ".//*[contains(@class, 'Modal_modal__loading')]/following::div[@class='Modal_modal_overlay__x2ZCr']"

