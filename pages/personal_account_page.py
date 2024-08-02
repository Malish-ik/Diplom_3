import allure
from pages.base_page import BasePage
from locators.personal_account_page_locators import PersonalAccountPageLocator
from data import TestUserData


class PersonalAccountPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Авторизация и переход в личный кабинет')
    def go_to_personal_account_with_auth(self):
        self.click_on_element(PersonalAccountPageLocator.AUTH_BUTTON_MAIN, PersonalAccountPageLocator.LAYER_TO_WAIT)
        self.set_text_to_element(PersonalAccountPageLocator.INPUT_EMAIL, TestUserData.user_email)
        self.set_text_to_element(PersonalAccountPageLocator.INPUT_PASSWORD, TestUserData.user_password)
        self.click_on_element(PersonalAccountPageLocator.AUTH_BUTTON, PersonalAccountPageLocator.LAYER_TO_WAIT)
        self.click_on_element(PersonalAccountPageLocator.PERSONAL_ACCOUNT_BUTTON, PersonalAccountPageLocator.LAYER_TO_WAIT)

    @allure.step('Получение текста по локатору "Профиль" в личном кабинете')
    def check_text_on_button_profile(self):
        return self.get_text_by_element(PersonalAccountPageLocator.ACCOUNT)

    @allure.step('Переход и получение текста по локтору "История заказов')
    def check_history_orders(self):
        self.click_on_element(PersonalAccountPageLocator.ORDERS_HISTORY_BUTTON, PersonalAccountPageLocator.LAYER_TO_WAIT)
        return self.get_text_by_element(PersonalAccountPageLocator.ORDERS_HISTORY_BUTTON)

    @allure.step('Выход из Личного кабинета и получение текста на кнопку входа')
    def check_logout(self):
        self.click_on_element(PersonalAccountPageLocator.LOGOUT_BUTTON, PersonalAccountPageLocator.LAYER_TO_WAIT)
        return self.get_text_by_element(PersonalAccountPageLocator.AUTH_BUTTON)
