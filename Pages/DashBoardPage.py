from selenium.webdriver.common.by import By
from Config.Config import TestData
from Pages.BasePage import BasePage
from Config.Config import TestData
from Pages.PimPage import PimPage

"""this class contains web elements and action for home page(dashboard page)"""


class DashBoardPage(BasePage):
    DASH_BOARD_TITLE = (By.XPATH, "//h6[text()='Dashboard']")
    MENU_PIM = (By.XPATH, "//a[@href='/web/index.php/pim/viewPimModule']")
    LOGOUT_LINK = (By.XPATH, " //i[contains(@class,'userdropdown-icon')]")
    LOGOUT_BTN = (By.XPATH, "//a[text()='Logout']")

    def is_dash_board_title_is_visible(self):
        return self.is_visible(self.DASH_BOARD_TITLE)

    def navigate_to_pim(self):
        self.do_click(self.MENU_PIM)
        return PimPage(self.driver)

    def navigate_to_pim_1(self):
        self.do_click(self.MENU_PIM)

    def validate_logout(self):
        self.do_click(self.LOGOUT_LINK)
        self.do_click(self.LOGOUT_BTN)


def __init__(self, driver):
    super.__init__(driver)
