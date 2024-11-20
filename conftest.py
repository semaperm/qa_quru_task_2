import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_setting_1():
    browser.open("https://www.google.com/ncr")
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()