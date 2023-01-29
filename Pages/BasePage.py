from selenium.common import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Config.Config import TestData
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
"""this is the base class for all pages"""
"""this contains generic methods and utilities"""


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.get(TestData.BASE_URL)

    """this method is for clicking web elements"""
    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()
        except (ElementClickInterceptedException,StaleElementReferenceException):
            WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)).click()

    """this method is for clicking web elements using javascript"""
    def do_javascript_click(self, by_locator):
        self.driver.execute_script("arguments[0].click",
                                   WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(by_locator)))

    """this method is for inputting values in text box web elements"""
    def do_send_key(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    """this method is getting values from elements and returns element text"""
    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    """this method is for validate visibilty of elements"""
    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    """this method returns page title"""
    def get_title(self):
        # element = WebDriverWait(self.driver, 50).until(EC.e
        return self.driver.title
