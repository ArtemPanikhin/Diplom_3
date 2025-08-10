import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from seletools.actions import drag_and_drop


class BasePage:
    @allure.step('Инициализация драйвера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Найти элементы по локатору')
    def find_elements(self, locator):
        return self.driver.find_elements(*locator)

    @allure.step('Ожидаем, что элемент появился на странице и его видно')
    def find_and_wait_element_until_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))

    @allure.step('Ожидаем, что элемент на странице кликабелен')
    def find_and_wait_element_until_clickable(self, locator):
        WebDriverWait(self.driver, 20, poll_frequency=1).until(EC.element_to_be_clickable(locator))
        return self.driver.find_elements(*locator)

    @allure.step('Клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Ввод текста')
    def send_keys_to_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Получить текст на элементе')
    def get_text_on_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('Сменить вкладку')
    def switch_to_next_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('Проверить отображение элемента')
    def check_displaying_element(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    @allure.step('Ждем получения всех элементов')
    def wait_visibility_of_all_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Смена URL')
    def navigate_to(self, url):
        self.driver.get(url)

    # @allure.step('Перемещение элемента на другой элемент')
    # def move_element(self, locator_element, locator_target):
    #     element = self.find_and_wait_element_until_visible(locator_element)
    #     target = self.find_and_wait_element_until_visible(locator_target)
    #     drag_and_drop(self.driver, element, target)

    @allure.step('Подождать изменение текста элемента')
    def wait_text_element_to_change(self, test_locator, value):
        return WebDriverWait(self.driver, 15).until_not(EC.text_to_be_present_in_element(test_locator, value))

    @allure.step('Ждем закрытие элемента')
    def wait_close_element(self, locator):
        WebDriverWait(self.driver, 15).until_not(EC.visibility_of_element_located(locator))

    @allure.step('Проверить невидимость элемента')
    def check_invisibility(self, locator) -> object:
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element(locator))

    @allure.step('Проверить отображение элемента')
    def check_displaying_of_element(self, locator):
        return self.find_and_wait_element_until_visible(locator).is_displayed()

    @allure.step('Перенос ингредиента в корзину')
    def drag_and_drop(self, source_locator, target_locator):
        self.find_and_wait_element_until_visible(source_locator)
        self.find_and_wait_element_until_visible(target_locator)
        element_from = self.driver.find_element(*source_locator)
        element_to = self.driver.find_element(*target_locator)
        self.driver.execute_script("""
            var source = arguments[0];
            var target = arguments[1];
            var evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragstart", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragenter", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragover", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("drop", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            target.dispatchEvent(evt);
            evt = document.createEvent("DragEvent");
            evt.initMouseEvent("dragend", true, true, window, 0, 0, 0, 0, 0, false, false, false, false, 0, null);
            source.dispatchEvent(evt);
        """, element_from, element_to)