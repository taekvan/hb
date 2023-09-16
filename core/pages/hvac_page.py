import os

from core.pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


class HvacPageLocators:
    HEADER_CONTENT: str = '//div[@class="header__content"]'
    ZIP_CODE_INPUT = HEADER_CONTENT + '//input[@id="zipCode"]'
    GET_ESTIMATE_BTN = HEADER_CONTENT + '//button[@class="customButton customButton_primary customButton_large"]'
    TYPE_OF_PROJECT_LIST_WRAPPER = '//ul[contains(@class, "typeOfProject__list")]'
    HVAC_WINDOW_TITLE = '//div[@Id="StepBodyId"]//h4'

    # PROJECT TYPES
    REPLACEMENT_INSTALLATION_TYPE = (TYPE_OF_PROJECT_LIST_WRAPPER +
                                     '//input[@value="replacementOrInstallation"]/../label')
    REPAIR_TYPE = TYPE_OF_PROJECT_LIST_WRAPPER + '//input[@value="repair"]/../label'
    NOT_SURE_TYPE = TYPE_OF_PROJECT_LIST_WRAPPER + '//input[@value="replacementOrInstallation"]/../label'

    # INVOLVED EQUIPMENT
    INVOLVED_EQUIPMENT_AC_CHECKBOX = '//*[@data-autotest-checkbox-equipment-airconditioner]/..'

    # EQUIPMENT AGE
    AGE_LESS_5 = '//*[@data-autotest-radio-equipmentage-5]/..'

    # TYPE OF PROPERTY
    PROPERTY_TYPE_DETACHED = '//*[@data-autotest-radio-propertytype-detached]/../label'

    # PROPERTY SIZE
    PROPERTY_SIZE_INPUT = '//*[@data-autotest-input-squarefeet-tel]'

    # PROPERTY CHANGES
    PROPERTY_CHANGES_YES_BTN = '//*[@data-autotest-radio-owner-yes]/..'

    # OWNER INFO
    OWNER_INFO_NAME_INPUT = '//*[@data-autotest-input-fullname-text]'
    OWNER_INFO_EMAIL_INPUT = '//*[@data-autotest-input-email-email]'
    OWNER_INFO_EMAIL_ERROR = OWNER_INFO_EMAIL_INPUT + '/../../../../div[@class="customInput__message"]'

    # PHONE NUMBER
    PHONE_NUMBER_INPUT = '//*[@data-autotest-input-phonenumber-tel]'
    PHONE_NUMBER_SUBMIT = '//*[@data-autotest-button-submit-submit-my-request]'
    PHONE_NUMBER_CORRECT_BTN = '//*[@data-autotest-button-submit-phone-number-is-correct]'

    # HVAC REPLACEMENT AND INSTALLATION SECTION
    HVAC_SURPRISE_SECTION = '//section[contains(@class, "surpriseBlock")]'

    NEXT_BTN = '//*[@data-autotest-button-submit-next]'
    CLOSE_PROJECT_BTN = '//*[@data-autotest-button-close]'
    CANCEL_ESTIMATION_BTN = '//*[@data-autotest-button-submit-cancel-project]'


class HvacPage(BasePage):
    def __init__(self, browser):
        super().__init__(browser)
        self.timeout = int(os.getenv('AUTOMATION_TIMEOUT'))

    def element_clickable_or_none(self, locator, timeout=None):
        _timeout = timeout if timeout else self.timeout
        element = None
        try:
            element = self.waits.wait_for_element_to_be_clickable((By.XPATH, locator), timeout=_timeout)
        except TimeoutException:
            pass
        finally:
            return element

    def zip_code_input(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.ZIP_CODE_INPUT, timeout)

    def get_estimate_btn(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.GET_ESTIMATE_BTN, timeout)

    def project_type_replacement_item(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.REPLACEMENT_INSTALLATION_TYPE, timeout)

    def equipment_ac_checkbox(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.INVOLVED_EQUIPMENT_AC_CHECKBOX, timeout)

    def age_less_5(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.AGE_LESS_5, timeout)

    def property_type_detached(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.PROPERTY_TYPE_DETACHED, timeout)

    def property_size_input(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.PROPERTY_SIZE_INPUT, timeout)

    def property_changes_yes_btn(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.PROPERTY_CHANGES_YES_BTN, timeout)

    def owner_info_name_input(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.OWNER_INFO_NAME_INPUT, timeout)

    def owner_info_email_input(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.OWNER_INFO_EMAIL_INPUT, timeout)

    def phone_number_input(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.PHONE_NUMBER_INPUT, timeout)

    def submit_btn(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.PHONE_NUMBER_SUBMIT, timeout)

    def phone_number_is_correct_btn(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.PHONE_NUMBER_CORRECT_BTN, timeout=timeout)

    def next_btn(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.NEXT_BTN, timeout)

    def surprise_section(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.HVAC_SURPRISE_SECTION, timeout=timeout)

    def get_email_error(self, timeout=None):
        return self.element_clickable_or_none(HvacPageLocators.OWNER_INFO_EMAIL_ERROR, timeout=timeout)

    def set_email(self, email_value):
        email_input = self.owner_info_email_input()
        email_input.clear()
        email_input.send_keys(email_value)

    def stop_estimation_process(self):
        self.waits.wait_for_element_to_be_clickable((By.XPATH, HvacPageLocators.CLOSE_PROJECT_BTN),
                                                    timeout=self.timeout).click()
        self.waits.wait_for_element_to_be_clickable((By.XPATH, HvacPageLocators.CANCEL_ESTIMATION_BTN),
                                                    timeout=self.timeout).click()

    def get_email_error_text(self):
        return self.get_email_error().text

    def open_page(self):
        self._open_page(f'{self.page_url}/hvac')

    def get_page_url(self):
        return f'{self._get_page_url}/hvac'

    def get_url(self):
        return self._get_current_url()
