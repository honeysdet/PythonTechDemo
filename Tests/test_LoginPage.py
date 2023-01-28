import pytest

from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.DashBoardPage import DashBoardPage


class Test_login(BaseTest):
    def test_login_page_title(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.get_title()
        assert title == TestData.LOGIN_PAGE_TITLE

    def test_login_forgot_password_link(self):
        self.LoginPage = LoginPage(self.driver)
        flag = self.LoginPage.is_forgot_password_is_visible()
        assert flag









