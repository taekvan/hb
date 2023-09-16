import os
import pytest
import allure
import logging

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FireFoxService
from core.pages.page_factory import PageFactory

logger = logging.getLogger("project")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")


@pytest.fixture(scope='session')
def ui_config(request):
    if request.config.getoption('--browser') == 'chrome':
        browser_name = 'chrome'
    elif request.config.getoption('--browser') == 'firefox':
        browser_name = 'firefox'
    else:
        browser_name = 'chrome'
    return {'browser': browser_name}


@pytest.fixture(scope='function')
def browser(request, ui_config, test_dir):
    browser_name = ui_config['browser']
    match browser_name:
        case 'chrome':
            options = ChromeOptions()
            service = ChromeService()
            driver = webdriver.Chrome(service=service, options=options)
        case 'firefox':
            service = FireFoxService()
            driver = webdriver.Firefox(service=service)

    driver.maximize_window()
    yield driver

    if request.node.rep_call.failed:
        screenshot_path = os.path.join(test_dir, 'failure.png')
        driver.save_screenshot(screenshot_path)
        allure.attach.file(screenshot_path, 'failure.png', attachment_type=allure.attachment_type.PNG)

        browser_log_path = os.path.join(test_dir, 'browser.log')
        with open(browser_log_path, 'w') as f:
            for i in driver.get_log('browser'):
                f.write(f"{i['level']} - {i['source']}\n{i['message']}\n\n")

        with open(browser_log_path, 'r') as f:
            allure.attach(f.read(), 'browser.log', attachment_type=allure.attachment_type.TEXT)
    driver.quit()


@pytest.fixture()
def test_dir(request):
    test_dir = os.path.join(os.path.curdir, 'tmp')
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    return test_dir


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture(scope='function')
def page_factory(browser):
    return PageFactory(browser)


def pytest_sessionstart(session):
    load_dotenv()
