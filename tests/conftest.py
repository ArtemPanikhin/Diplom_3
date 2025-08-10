import pytest
from selenium import webdriver
from selenium.webdriver import FirefoxProfile
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage
from pages.profile_page import ProfilePage
from curl import *


@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    driver = None
    if request.param == 'chrome':
        options = Options()
        options.add_argument('--incognito')
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
    elif request.param == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        profile = FirefoxProfile()
        profile.set_preference("browser.privatebrowsing.autostart", True)
        firefox_options.profile = profile
        driver = webdriver.Firefox(options=firefox_options)
        driver.set_window_size(1920, 1080)
    driver.get(main_page_url)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    return main_page

@pytest.fixture
def profile_page(driver):
    profile_page = ProfilePage(driver)
    return profile_page

@pytest.fixture
def order_feed_page(driver):
    order_feed_page = OrderFeedPage(driver)
    return order_feed_page
