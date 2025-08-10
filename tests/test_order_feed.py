import allure
import pytest

from data import DataForAuth
from locators.order_feed_page_locators import OrderFeedPageLocators

class TestOrderFeed:
    @allure.title('При создании нового заказа счётчик "Выполнено за всё время" и "Выполнено за сегодня" увеличивается')
    @pytest.mark.parametrize('counter', [
        OrderFeedPageLocators.COUNT_ORDERS_FOR_ALL_TIME,
        OrderFeedPageLocators.COUNT_ORDERS_TODAY
    ])
    def test_orders_increasing_with_new_order(self, driver, main_page, profile_page, order_feed_page, counter):
        with allure.step("Авторизация пользователя"):
            main_page.click_sign_in_button()
            profile_page.login_user(DataForAuth.TEST_EMAIL, DataForAuth.TEST_PASSWORD)
        with allure.step("Подготовка к созданию заказа"):
            main_page.wait_make_order_page()
            main_page.click_list_order_button()
            initial_count = order_feed_page.get_count_orders(counter)
        with allure.step("Создание нового заказа"):
            order_feed_page.click_constructor_button()
            main_page.create_order()
        with allure.step("Проверка увеличения счетчика заказов"):
            main_page.click_list_order_button()
            new_count = order_feed_page.get_count_orders(counter)
            assert new_count > initial_count

    @allure.title('После оформления заказа его номер появляется в разделе "В работе"')
    def test_order_displaying_in_progress(self, driver, main_page, profile_page, order_feed_page):
        with allure.step('Авторизация пользователя'):
            main_page.click_sign_in_button()
            profile_page.login_user(DataForAuth.TEST_EMAIL, DataForAuth.TEST_PASSWORD)
        with allure.step('Подготовка к созданию заказа'):
            main_page.wait_make_order_page()
            main_page.drag_and_drop_ingredient()
        with allure.step('Оформление заказа'):
            main_page.click_make_order_button()
            main_page.check_open_popup_with_order()
            id_order = main_page.get_id_order_in_popup()
            main_page.close_popup_with_order_details()
        with allure.step('Проверка отображения заказа в ленте'):
            main_page.click_list_order_button()
            id_order_in_processing = order_feed_page.get_id_order_in_processing()
        with allure.step('Проверка соответствия номеров заказа'):
            assert id_order == id_order_in_processing