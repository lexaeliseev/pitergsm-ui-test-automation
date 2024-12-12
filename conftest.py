from selene import browser
import os
from dotenv import load_dotenv
import pytest


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()


@pytest.fixture(scope='session', autouse=True)
def browser_settings(load_env):
    browser.config.base_url = os.getenv('URL')
    browser.config.window_width = '1920'
    browser.config.window_height = '1080'
    yield
    browser.quit()