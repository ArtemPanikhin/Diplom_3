import allure
from pages.base_page import BasePage
from locators.order_feed_page_locators import OrderFeedPageLocators


class OrderFeedPage(BasePage):
    @allure.step('Загрузка страницы')
    def wait_list_orders_page(self):
        self.find_and_wait_element_until_visible(OrderFeedPageLocators.ORDERS_FOR_ALL_TIME)

    @allure.step('Получаем текст заголовка "Лента заказов"')
    def get_list_orders_header_text(self):
        self.wait_list_orders_page()
        return self.get_text_on_element(OrderFeedPageLocators.LIST_ORDERS_HEADER)

    @allure.step('Количество заказов')
    def get_count_orders(self, locator):
        self.wait_list_orders_page()
        self.find_and_wait_element_until_visible(locator)
        return self.get_text_on_element(locator)

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.find_and_wait_element_until_clickable(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(OrderFeedPageLocators.CONSTRUCTOR_BUTTON)

    @allure.step('Получаем id заказ, который в разделе "В работе"')
    def get_id_order_in_processing(self):
        self.find_and_wait_element_until_visible(OrderFeedPageLocators.ORDER_IN_PROCESSING)
        return self.get_text_on_element(OrderFeedPageLocators.ORDER_IN_PROCESSING)
