from selenium.webdriver.common.by import By

class MainPageLocators:
    # кнопка "Войти в аккаунт"
    SIGN_IN_BUTTON = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # кнопка "Личный кабинет"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, ".//a[@href = '/account']")
    # кнопка "Оформить заказ"
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    # заголовок "Cоберите бургер"
    MAKE_BURGER = (By.XPATH, ".//section[contains(@class, 'BurgerIngredients')]/h1")
    # кнопка "Лента заказов"
    LIST_ORDER_BUTTON = (By.XPATH, ".//p[text() = 'Лента Заказов']")
    # заголовок "Детали ингредиента" в попапе
    INGREDIENT_POPUP_TITLE = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(text(), 'Детали')]")
    # кнопка (крестик) в окне с деталями ингредиента
    CLOSE_INGREDIENT = (By.XPATH, ".//section[contains(@class, 'Modal_modal_open')]//button[contains(@class, 'close')]")
    # счетчик ингредиента "Флюоресцентная булка R2-D3"
    COUNTER_FLUORESCENT_BUN = (By.XPATH, ".//*[@alt='Флюоресцентная булка R2-D3']/preceding-sibling::div/p")
    # конструктор бургера
    CONSTRUCTOR_BURGER = (By.CLASS_NAME, 'BurgerConstructor_basket__list__l9dp_')
    # "Флюоресцентная булка R2-D3" в конструкторе бургера
    FLUORESCENT_BUN_IN_BURGER = (By.XPATH, '//*[@id="root"]/div/main/section[2]/ul/li[1]/div/span/img')
    # сообщение "Ваш заказ начали готовить" в попапе оформленного заказа
    ORDER_IS_PREPARING = (By.XPATH, ".//p[contains(text(), 'заказ начали готовить')]")
    # id заказа в попапе оформленного заказа
    ID_ORDER = (By.XPATH, ".//div[contains(@class, 'container__Wo2l')]//h2[contains(@class, 'title_shadow__3ikwq Mod')]")
    # кнопка закрытия попапа с деталями оформленного заказа
    CLOSE_ORDER_DETAILS = (By.XPATH, ".//button[contains(@class, 'modal__close__TnseK')]")
    # Перенос булки
    ORDER_TARGET_TOP = (By.XPATH, "//img[@alt='Перетяните булочку сюда (верх)']")
    # Ингредиент "Флюоресцентная булка R2-D3"
    INGREDIENT_R2D3_BUN = (By.XPATH, "//img[@alt='Флюоресцентная булка R2-D3']")
    # Кнопка "Конструктор"
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(),'Конструктор')]")
    # Счетчик ингредиентов
    INGREDIENT_COUNTER = (By.XPATH, "//p[@class='counter_counter__num__3nue1']")



