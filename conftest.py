from selene import browser
import os
from dotenv import load_dotenv
import pytest
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def browser_settings(load_env):
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.driver_options = driver_options

    browser.config.base_url = os.getenv('URL')
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    yield
    browser.quit()