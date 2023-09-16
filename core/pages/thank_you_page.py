from core.pages.base_page import BasePage
from selenium.webdriver.common.by import By


class ThankYouPageLocators:
    BODY_CONTAINER = '//div[@id="StepBodyId"]'
    TITLE: str = BODY_CONTAINER + '//h4'


class ThankYouPage(BasePage):

    def wait_till_loaded(self):
        self.waits.wait_for_text_to_be_present_in_element((By.XPATH, ThankYouPageLocators.BODY_CONTAINER), 'Thank you')

    def title(self):
        return self.waits.wait_for_element_to_be_clickable((By.XPATH, ThankYouPageLocators.TITLE))

    def get_title_text(self):
        return self.title().text

    def get_page_url(self):
        return f'{self._get_page_url()}/thank-you'
