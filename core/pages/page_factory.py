from core.pages.hvac_page import HvacPage
from core.pages.thank_you_page import ThankYouPage

PAGES = {
    'hvac_page': HvacPage,
    'thank_you_page': ThankYouPage,
}


class PageFactory:
    def __init__(self, browser):
        self._browser = browser

    def get_page(self, page_name):
        """Get page name method"""
        page_name = page_name.lower()
        page = PAGES[page_name](browser=self._browser)
        return page

    def get_loaded_page(self, page_name):
        page = self.get_page(page_name)
        page.wait_till_loaded()
        return page
