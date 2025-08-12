from selenium.webdriver.common.by import By

class OrderFeedPageLocators:
    # Заголовок "Выполнено за все время"
    ORDERS_FOR_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]")
    # Количество заказов за всё время
    COUNT_ORDERS_FOR_ALL_TIME = (By.XPATH, ".//p[contains(text(), 'Выполнено за все время')]/following-sibling::p")
    # Количество заказов за сегодня
    COUNT_ORDERS_TODAY = (By.XPATH, ".//p[contains(text(), 'Выполнено за сегодня')]/following-sibling::p")
    # Заголовок "Лента заказов"
    LIST_ORDERS_HEADER = (By.XPATH, ".//div[contains(@class, 'OrderFeed')]/h1[contains(@class, 'mt-10 mb-5')]")
    # верхний заказ в истории заказов
    FIRST_ORDER_IN_LIST = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_list')]/li[1]")
    # Попап с деталями заказа
    ORDER_POPUP_DETAILS = (By.XPATH, ".//p[text() = 'Cостав']/ancestor::div[contains(@class, 'container__Wo2l')]")
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text() = 'Конструктор']")
    # Заказ в разделе "В работе"
    ORDER_IN_PROCESSING = (By.XPATH, ".//ul[contains(@class, 'orderListReady')]/li[contains(@class, 'default mb-2')]")