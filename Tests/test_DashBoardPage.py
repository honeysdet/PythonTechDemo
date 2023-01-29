import pytest
from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.PimPage import PimPage
from Pages.DashBoardPage import DashBoardPage

"""test for dashboard pages"""
class Test_dashboard(BaseTest):

    def test_dashbord_title(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        flg = self.DashBoardPage.is_dash_board_title_is_visible()
        assert flg




