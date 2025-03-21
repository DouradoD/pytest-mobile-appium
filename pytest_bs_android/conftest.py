from appium import webdriver
from appium.options.android import UiAutomator2Options
from selenium.webdriver.support.ui import WebDriverWait
import pytest


# Options are only available since client version 2.3.0

@pytest.fixture(scope='session')
def driver():
    options = UiAutomator2Options().load_capabilities({
        # Set URL of the application under test
        "app": "bs://8b3808506a2b3a3446d61e60f6973e9cb6aaa681",
        # Specify device and os_version for testing
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",
        # Set other BrowserStack capabilities
        'bstack:options': {
            "projectName": "Android",
            "buildName": "browserstack-build-1 - Android",
            "sessionName": "BStack first_test",
            # Set your access credentials
            "userName": "diogoaugustodefa1",
            "accessKey": "sWfTic4cnsBxXynsWowh"
        }
    })
    # Initialize the remote Webdriver using BrowserStack remote URL
    # and options defined above
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    driver.wait = WebDriverWait(driver=driver, timeout=15)
    return driver


def pytest_bdd_before_scenario():
    """ initial setup """


def pytest_bdd_after_scenario(request):
    driver = request.getfixturevalue('driver')
    driver.quit()
