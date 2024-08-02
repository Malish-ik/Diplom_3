import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocator
from locators.personal_account_page_locators import PersonalAccountPageLocator
from locators.main_page_locators import MainPageLocator
from data import TestUserData


class OrdersFeedPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход на старницу Лента заказов')
    def go_to_order_feed(self):
        self.click_on_element(OrderFeedPageLocator.ORDERS_FEED_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение текста на всплывающем окне информации о заказе')
    def get_order_info(self):
        self.click_on_element(OrderFeedPageLocator.ORDER_1, OrderFeedPageLocator.LAYER_TO_WAIT)
        return self.get_text_by_element(OrderFeedPageLocator.ORDER_INFO)

    @allure.step('Переход на страницу авторизации, ввод почты и пароля, авторизация')
    def login(self):
        self.click_on_element(PersonalAccountPageLocator.AUTH_BUTTON_MAIN, OrderFeedPageLocator.LAYER_TO_WAIT)
        self.set_text_to_element(PersonalAccountPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAccountPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAccountPageLocator.AUTH_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)

    @allure.step('Добавление ингредиента в корзину,создание заказа')
    def create_order(self):
        self.drag_and_drop(MainPageLocator.FLUORESCENT_BUN, MainPageLocator.CART)
        self.click_on_element(MainPageLocator.ORDER_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)
    def add_bun_to_cart(self):
        self.drag_and_drop(MainPageLocator.FLUORESCENT_BUN, MainPageLocator.CART)


    @allure.step('Переход в Конструктор')
    def go_to_constructor(self):
        self.click_on_element(OrderFeedPageLocator.CONSTRUCTOR_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение номера оформленного заказа')
    def get_order_number(self):
        self.wait_invisible(OrderFeedPageLocator.ID_NEW_ORDER, '9999')
        return self.get_text_by_element(OrderFeedPageLocator.ID_NEW_ORDER)

    @allure.step('Получение номера готового заказа')
    def get_orders_numbers(self):
        self.click_on_element(OrderFeedPageLocator.CLOSE_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)
        self.click_on_element(OrderFeedPageLocator.ORDERS_FEED_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)
        return self.get_text_by_element(OrderFeedPageLocator.ORDERS_NUMBERS)

    @allure.step('Звкрытие всплывающего окна с инфо о заказе и переход в Ленту заказов')
    def go_to_orders_feed_from_order_info(self):
        self.click_on_element(OrderFeedPageLocator.CLOSE_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)
        self.click_on_element(OrderFeedPageLocator.ORDERS_FEED_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение количества заказов за все время')
    def get_count_all_time(self):
        return self.get_text_by_element(OrderFeedPageLocator.COUNTER_ALL_TIME)

    @allure.step('Получение количества заказов за сегодня')
    def get_count_today(self):
        return self.get_text_by_element(OrderFeedPageLocator.COUNTER_TODAY)

    @allure.step('Получение номера заказа в блоке "Заказы в работе"')
    def get_orders_in_work(self):
        self.click_on_element(OrderFeedPageLocator.CLOSE_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)
        self.click_on_element(OrderFeedPageLocator.ORDERS_FEED_BUTTON, OrderFeedPageLocator.LAYER_TO_WAIT)
        self.wait_invisible(OrderFeedPageLocator.ORDERS_IN_WORK, 'Все текущие заказы готовы!')
        return self.get_text_by_element(OrderFeedPageLocator.ORDERS_IN_WORK)


