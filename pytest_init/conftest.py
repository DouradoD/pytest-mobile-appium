import pytest
from appium.webdriver import Remote as MobileRemote
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope='session')
def driver():
    desired_cap = {
        "platformName": "android",
        "os_version": "",
        "device": "",
        "app": "/Users/diogodourado/Downloads/android-testing.apk"
    }
    driver = MobileRemote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
    driver.wait = WebDriverWait(driver=driver, timeout=15)
    return driver


def pytest_bdd_before_scenario():
    """ initial setup """


def pytest_bdd_after_scenario(request):
    driver = request.getfixturevalue('driver')
    driver.quit()
