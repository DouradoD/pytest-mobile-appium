from pytest_bdd import given, when, scenarios, parsers
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as exp_conditions

scenarios('../features/search.feature')


@given('the user is in the numerade home screen')
def impl(driver):
    pass


@given(parsers.parse('He fills the search filed with the following word "{word}"'))
def impl(driver, word):
    pass


@when('He clicks on search button')
def impl(driver):
    pass
