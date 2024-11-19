import pytest
from selene import browser

@pytest.fixture(autouse=True)
def browser_setting_1():
    browser.open("https://www.google.com/ncr")


@pytest.fixture()
def browser_setting_2(browser_setting_1):
    browser.config.window_height = 1080
    browser.config.window_width = 1920

    yield

    browser.quit()