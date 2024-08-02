import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocator
from locators.personal_account_page_locators import PersonalAccountPageLocator
from data import TestUserData


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Переход в конструктор')
    def go_to_assembler(self):
        self.click_on_element(MainPageLocator.ORDERS_FEED_BUTTON, MainPageLocator.LAYER_TO_WAIT)
        self.click_on_element(MainPageLocator.CONSTRUCTOR_BUTTON, MainPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение текста в блоке "Соберите бургер"')
    def check_assembler_text(self):
        return self.get_text_by_element(MainPageLocator.ASSEMBLE_A_BURGER)

    @allure.step('Переход в ленту заказов')
    def go_to_order_feed(self):
        self.click_on_element(MainPageLocator.ORDERS_FEED_BUTTON, MainPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение текста в блоке Лента заказов')
    def check_order_feed_text(self):
        return self.get_text_by_element(MainPageLocator.ORDERS_FEED)

    @allure.step('Открытие всплывающего окна с инфо об ингредиенте')
    def get_info_ingredient(self):
        self.click_on_element(MainPageLocator.FLUORESCENT_BUN, MainPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение текста в окне с информацией об ингредиенте')
    def check_text_about_ingredient(self):
        return self.get_text_by_element(MainPageLocator.INGREDIENT_INFO)

    @allure.step('Закрытие всплывающего окна с информацией об ингредиенте')
    def close_info_ingredient(self):
        self.click_on_element(MainPageLocator.CLOSE_BUTTON)

    @allure.step('Получение атрибута для проверки закрытия окна с инфо об ингредиенте')
    def check_ingredient_info_closed(self):
        return self.get_attribute(MainPageLocator.WINDOW_INFO_INGREDIENT, 'class')

    @allure.step('Добавление булочки в корзину')
    def add_bun_to_cart(self):
        self.drag_and_drop(MainPageLocator.FLUORESCENT_BUN, MainPageLocator.CART)

    @allure.step('Авторизация')
    def login(self):
        self.click_on_element(PersonalAccountPageLocator.AUTH_BUTTON_MAIN, MainPageLocator.LAYER_TO_WAIT)
        self.set_text_to_element(PersonalAccountPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAccountPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAccountPageLocator.AUTH_BUTTON, MainPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение текста на всплывающем окне с информацией о заказе')
    def check_order(self):
        self.click_on_element(MainPageLocator.ORDER_BUTTON, MainPageLocator.LAYER_TO_WAIT)
        return self.get_text_by_element(MainPageLocator.ID_ORDER)

    @allure.step('Получение количества добавлений в счетчике ингредиента')
    def check_ingredients_counter(self):
        return self.get_text_by_element(MainPageLocator.COUNTER)
