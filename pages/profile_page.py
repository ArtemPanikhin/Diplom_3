import allure

from curl import *
from locators.profile_page_locators import ProfilePageLocators
from pages.base_page import BasePage


class ProfilePage(BasePage):
    @allure.step('Загрузка страница с формой авторизации')
    def wait_profile_page(self):
        self.find_and_wait_element_until_visible(ProfilePageLocators.PASSWORD_RECOVERY_BUTTON)

    @allure.step('Перейти на страницу авторизации')
    def open_login_page(self):
        self.navigate_to(login_site)

    @allure.step('Вводим текст в поле email формы авторизации')
    def set_email(self, email):
        self.find_and_wait_element_until_clickable(ProfilePageLocators.USER_EMAIL_FIELD)
        self.send_keys_to_input(ProfilePageLocators.USER_EMAIL_FIELD, email)

    @allure.step('Вводим текст в поле "Пароль" формы авторизации')
    def set_password(self, password):
        self.find_and_wait_element_until_clickable(ProfilePageLocators.USER_PASSWORD_FIELD)
        self.send_keys_to_input(ProfilePageLocators.USER_PASSWORD_FIELD, password)

    @allure.step('Кликаем по кнопке "Войти" в форме авторизации')
    def click_login_button(self):
        self.click_on_element(ProfilePageLocators.LOGIN_BUTTON)

    @allure.step('Авторизуемся')
    def login_user(self, email, password):
        self.set_email(email)
        self.set_password(password)
        self.click_login_button()

    @allure.step('Кликаем по кнопке "Конструктор"')
    def click_constructor_button(self):
        self.find_and_wait_element_until_clickable(ProfilePageLocators.CONSTRUCTOR_BUTTON)
        self.click_on_element(ProfilePageLocators.CONSTRUCTOR_BUTTON)

