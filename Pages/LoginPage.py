from selenium.webdriver.common.by import By
from Config.Config import TestData
from Pages.BasePage import BasePage
from Config.Config import TestData
from Pages.DashBoardPage import DashBoardPage

"""this class contains web elements and action for Login Page"""


class LoginPage(BasePage):
    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BTN = (By.TAG_NAME, "button")
    LINK_FORGOT_PASSWORD = (By.XPATH, "// p[text() = 'Forgot your password? ']")
    DASH_BOARD_TITLE = (By.XPATH, "//p[text()='Time at Work']")

    def is_forgot_password_is_visible(self):
        return self.is_visible(self.LINK_FORGOT_PASSWORD)

    def validate_login(self):
        self.do_send_key(self.USERNAME, TestData.USER_NAME)
        self.do_send_key(self.PASSWORD, TestData.PASSWORD)
        self.do_click(self.LOGIN_BTN)
        return DashBoardPage(self.driver)


def __init__(self, driver):
    super.__init__(driver)
