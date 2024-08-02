import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from seletools.actions import drag_and_drop

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def wait_while_invisible(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(locator))

    @allure.step('Поиск элемента')
    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, layer_to_wait=None):
        if layer_to_wait:
            WebDriverWait(self.driver, 5).until(expected_conditions.invisibility_of_element(layer_to_wait))
        self.wait_and_find_element(locator).click()

    @allure.step('Ожидание пока текст элемента не изменится')
    def wait_invisible(self, locator, value):
        self.wait_and_find_element(locator)
        return WebDriverWait(self.driver, 15).until_not(expected_conditions.text_to_be_present_in_element(locator, value))

    @allure.step('Получение текста элемента')
    def get_text_by_element(self, locator):
        return self.wait_and_find_element(locator).text

    @allure.step('Добавить текст в поле элемента')
    def set_text_to_element(self, locator, text):
        self.wait_and_find_element(locator).send_keys(text)

    @allure.step('Получить значение атрибута элемента')
    def get_attribute(self, locator, value):
        return self.wait_and_find_element(locator).get_attribute(value)

    @allure.step('Перетаскивание элемента в другой элемент')
    def drag_and_drop(self, locator1, locator2):
        ingredient = self.wait_and_find_element(locator1)
        cart = self.wait_and_find_element(locator2)
        drag_and_drop(self.driver, ingredient, cart)

