import os
from core.utilities.waits import Waits


class BasePage:
    def __init__(self, browser):
        self.page_url = os.getenv('APP_URL')
        self.browser = browser
        self.waits = Waits(self.browser)

    def _open_page(self, url):
        self.browser.get(url)

    def _get_page_url(self):
        return self.page_url

    def _get_current_url(self):
        return self.browser.current_url
