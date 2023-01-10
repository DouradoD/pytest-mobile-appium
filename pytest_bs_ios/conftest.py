from appium import webdriver
from appium.options.ios import XCUITestOptions
from selenium.webdriver.support.ui import WebDriverWait
import pytest


@pytest.fixture(scope='session')
def driver():
    options = XCUITestOptions().load_capabilities({
        "app": "bs://444bd0308813ae0dc236f8cd461c02d3afa7901d",
        # Specify device and os_version for testing
        "deviceName": "iPhone 11 Pro",
        "platformVersion": "13",
        # Set other BrowserStack capabilities
        "bstack:options": {
            "userName": "diogoaugustodefa1",
            "accessKey": "sWfTic4cnsBxXynsWowh",
            "projectName": "iOS",
            "buildName": "browserstack-build-1 - iOS",
            "sessionName": "BStack first_test"
        }
    })

    # Initialize the remote Webdriver using BrowserStack remote URL
    # and options defined above
    driver = webdriver.Remote("http://hub.browserstack.com/wd/hub", options=options)
    # driver.wait = WebDriverWait(driver=driver, timeout=15)
    return driver


def pytest_bdd_before_scenario():
    """ initial setup """


def pytest_bdd_after_scenario(request):
    """ before scenario """
