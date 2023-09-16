import os

from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait


class Waits:

    def __init__(self, driver):
        self.driver = driver
        self.timeout = int(os.getenv('AUTOMATION_TIMEOUT'))

    def wait_for_element(self, locator: tuple, timeout=None):
        _timeout = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, _timeout).until(ec.presence_of_element_located(locator))

    def wait_for_element_visibility(self, locator: tuple, timeout=None):
        _timeout = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, _timeout).until(ec.visibility_of_element_located(locator))

    def wait_for_text_to_be_present_in_element(self, locator: tuple, text_: str, timeout=None):
        _timeout = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, _timeout).until(ec.text_to_be_present_in_element(locator, text_))

    def wait_for_element_to_be_clickable(self, locator, timeout=None):
        _timeout = timeout if timeout else self.timeout
        return WebDriverWait(self.driver, _timeout).until(ec.element_to_be_clickable(locator))
