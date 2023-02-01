import pytest
from selenium import webdriver
from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.DashBoardPage import DashBoardPage

"""test for PIM pages"""


class Test_pim(BaseTest):
    """test for PIM pages tabs are displayed"""

    def test_home_page_menu_pim(self):
        self.LoginPage = LoginPage(self.driver)
        self.DasBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DasBoardPage.navigate_to_pim()
        flag = self.PimPage.is_pim_visible()
        self.PimPage.validate_logout()
        assert flag

    def test_home_page_tab_employee(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        flag = self.PimPage.is_employee_add_visible()
        assert flag
        self.PimPage.validate_logout()

    def test_home_page_tab_conf(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        flag = self.PimPage.is_conf_visible()
        self.DashBoardPage.validate_logout()
        assert flag

    def test_home_page_tab_report(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        flag = self.PimPage.is_report_visible()
        self.DashBoardPage.validate_logout()
        assert flag

    def test_home_page_tab_add(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        flag = self.PimPage.is_employee_add_visible()
        self.DashBoardPage.validate_logout()
        assert flag

    """test for add employee functionality"""

    def test_pim_page_tab_add_employee(self, input_data_for_add_user):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        self.PimPage.do_click_add_btn()
        flag = self.PimPage.input_data_for_adduser(input_data_for_add_user[0], input_data_for_add_user[1],
                                                   input_data_for_add_user[2], input_data_for_add_user[3],
                                                   input_data_for_add_user[4])
        assert flag
        self.PimPage.validate_logout()

    """test for search employee functionality"""

    def test_pim_page_tab_search_employee(self, input_data_for_add_user):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        self.PimPage.do_click_employee_list()
        flag = self.PimPage.do_search_new_employee(input_data_for_add_user[5])
        assert flag
        self.PimPage.validate_logout()

    """test for delete employee functionality"""

    def test_pim_page_tab_delete_employee(self, input_data_for_add_user):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        self.PimPage.do_click_employee_list()
        flag = self.PimPage.do_search_delete_employee(input_data_for_add_user[5])
        assert flag
        self.PimPage.validate_logout()


