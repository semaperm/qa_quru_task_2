import pytest
from selene import browser, be, have


def test_one():
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_two():
    browser.element('[name="q"]').should(be.blank).type('12w3e=-!@#$%%^&$^&*$').press_enter()
    browser.element('#rcnt').should(have.text('Your search - 12w3e=-!@#$%%^&$^&*$ - did not match any documents.'))