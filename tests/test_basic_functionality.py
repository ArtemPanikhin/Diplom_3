import allure

from pages.main_page import MainPage


@allure.feature("Проверка основного функционала")
class TestCoreFunctionality:
    @allure.title('Переход по клику на "Конструктор"')
    def test_open_constructor(self, driver, main_page, order_feed_page):
        with allure.step('Открываем ленту заказов'):
            main_page.click_list_order_button()
        with allure.step('Кликаем на кнопку "Конструктор"'):
            order_feed_page.click_constructor_button()
        with allure.step('Проверяем отображение заголовка конструктора'):
            assert main_page.get_make_burger_text() == "Соберите бургер"

    @allure.title('Переход по клику на "Лента Заказов"')
    def test_open_list_orders(self, driver, main_page, order_feed_page):
        with allure.step('Ожидаем загрузки главной страницы'):
            main_page.wait_main_page()
        with allure.step('Кликаем на кнопку "Лента заказов"'):
            main_page.click_list_order_button()
        with allure.step('Проверяем отображение заголовка ленты заказов'):
            assert order_feed_page.get_list_orders_header_text() == "Лента заказов"

    @allure.title('Если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_details_ingredient(self, driver, main_page):
        with allure.step('Ожидаем загрузки главной страницы'):
            main_page.wait_main_page()
        with allure.step('Кликаем на ингредиент "булку"'):
            main_page.click_ingredient_bun()
        with allure.step('Проверяем отображение попапа с деталями'):
            assert main_page.check_open_popup_with_details_ingredient_bun()

    @allure.title('Всплывающее окно закрывается кликом по крестику')
    def test_close_details_ingredient(self, driver, main_page):
        with allure.step('Ожидаем загрузки главной страницы'):
             main_page.wait_main_page()
        with allure.step('Открываем попап с деталями ингредиента'):
            main_page.click_ingredient_bun()
        with allure.step('Закрываем попап кликом по крестику'):
            main_page.close_popup_with_ingredient_details()
        with allure.step('Проверяем, что попап закрылся'):
            assert main_page.check_not_displaying_of_popup_details_ingredient()

    @allure.title('При добавлении ингредиента в заказ счётчик этого ингредиента увеличивается')
    def test_ingredient_counter_increases(self, driver, profile_page, main_page):
        with allure.step('Открываем страницу входа'):
            profile_page.open_login_page()
        with allure.step('Нажимаем на "Конструктор"'):
            main_page.click_constructor()
        with allure.step('Получаем начальное значение каунтера ингредиентов'):
            initial_counter = main_page.get_ingredient_counter()
        with allure.step('Добавляем ингредиент в заказ'):
            main_page.drag_and_drop_ingredient()
        with allure.step('Проверяем, что каунтер увеличился'):
            updated_counter = main_page.get_ingredient_counter()
        assert updated_counter == initial_counter + 2