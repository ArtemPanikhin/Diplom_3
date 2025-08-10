import allure
from selenium.webdriver.support.wait import WebDriverWait

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

class MainPage(BasePage):
    @allure.step('Загрузки страницы')
    def wait_main_page(self):
        self.wait_visibility_of_all_elements(MainPageLocators.SIGN_IN_BUTTON)

    @allure.step('Кликаем по кнопке "Войти в аккаунт"')
    def click_sign_in_button(self):
        self.find_and_wait_element_until_visible(MainPageLocators.SIGN_IN_BUTTON)
        self.click_on_element(MainPageLocators.SIGN_IN_BUTTON)

    @allure.step('Загрузка страницы после авторизации')
    def wait_make_order_page(self):
        self.wait_visibility_of_all_elements(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Получаем текст заголовка "Соберите бургер"')
    def get_make_burger_text(self):
        self.wait_main_page()
        return self.get_text_on_element(MainPageLocators.MAKE_BURGER)

    @allure.step('Кликаем по кнопке "Лента Заказов"')
    def click_list_order_button(self):
        self.find_and_wait_element_until_visible(MainPageLocators.LIST_ORDER_BUTTON)
        self.click_on_element(MainPageLocators.LIST_ORDER_BUTTON)

    @allure.step('Кликаем по ингредиенту булка')
    def click_ingredient_bun(self):
        self.find_elements(MainPageLocators.INGREDIENT_R2D3_BUN)
        self.click_on_element(MainPageLocators.INGREDIENT_R2D3_BUN)

    @allure.step('Закрываем окно с деталями ингредиента')
    def close_popup_with_ingredient_details(self):
        self.find_and_wait_element_until_visible(MainPageLocators.CLOSE_INGREDIENT)
        self.click_on_element(MainPageLocators.CLOSE_INGREDIENT)

    @allure.step('Кликнуть по "Конструктору"')
    def click_constructor(self):
        self.click_on_element(MainPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получить счетчик ингредиентов')
    def get_ingredient_counter(self):
        return int(self.get_text_on_element(MainPageLocators.INGREDIENT_COUNTER))

    @allure.step('Ожидаем, когда ингредиент "булка" появится в конструкторе бургера')
    def wait_ingredient_bun_to_constructor_burger(self):
        self.find_and_wait_element_until_visible(MainPageLocators.FLUORESCENT_BUN_IN_BURGER)

    @allure.step('Перенос ингредиентов')
    def drag_and_drop_ingredient(self):
        ingredient_locator = MainPageLocators.INGREDIENT_R2D3_BUN
        target_locator = MainPageLocators.ORDER_TARGET_TOP
        self.drag_and_drop(ingredient_locator, target_locator)

    @allure.step('Кликаем по кнопке "Заказать бургер"')
    def click_make_order_button(self):
        self.wait_make_order_page()
        self.click_on_element(MainPageLocators.MAKE_ORDER_BUTTON)

    @allure.step('Получаем id заказа со всплывающего окна с оформленным заказом')
    def get_id_order_in_popup(self):
        self.wait_text_element_to_change(MainPageLocators.ID_ORDER, '9999')
        id_order = self.get_text_on_element(MainPageLocators.ID_ORDER)
        return f"0{id_order}"

    @allure.step('Закрываем окно с деталями заказа')
    def close_popup_with_order_details(self):
        self.wait_text_element_to_change(MainPageLocators.ID_ORDER, '9999')
        self.find_and_wait_element_until_clickable(MainPageLocators.CLOSE_ORDER_DETAILS)
        self.click_on_element(MainPageLocators.CLOSE_ORDER_DETAILS)

    @allure.step('Создать заказ')
    def create_order(self):
        self.wait_make_order_page()
        self.drag_and_drop_ingredient()
        self.click_make_order_button()
        self.check_open_popup_with_order()
        self.close_popup_with_order_details()

    @allure.step('Проверяем, что появилось всплывающее окно с деталями игридиента')
    def check_open_popup_with_details_ingredient_bun(self):
        self.find_elements(MainPageLocators.INGREDIENT_POPUP_TITLE)
        return self.check_displaying_element(MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что окно с деталями ингредиента закрылось')
    def check_not_displaying_of_popup_details_ingredient(self):
        self.wait_close_element(MainPageLocators.INGREDIENT_POPUP_TITLE)
        return self.check_invisibility(MainPageLocators.INGREDIENT_POPUP_TITLE)

    @allure.step('Проверяем, что появилось всплывающее окно с оформленным заказом')
    def check_open_popup_with_order(self):
        self.find_and_wait_element_until_visible(MainPageLocators.ORDER_IS_PREPARING)
        return self.check_displaying_of_element(MainPageLocators.ORDER_IS_PREPARING)




