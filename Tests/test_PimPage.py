import pytest
from selenium import webdriver
from Config.Config import TestData
from Pages.LoginPage import LoginPage
from Tests.test_Base import BaseTest
from Pages.DashBoardPage import DashBoardPage


class Test_pim(BaseTest):

    def test_pim_page_tab_add_employee(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        self.PimPage.do_click_add_btn()
        flag = self.PimPage.input_data_for_adduser()
        assert flag
        self.PimPage.validate_logout()

    def test_pim_page_tab_search_employee(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        self.PimPage.do_click_employee_list()
        flag=self.PimPage.do_search_new_employee()
        assert flag
        self.PimPage.validate_logout()

    def test_pim_page_tab_delete_employee(self):
        self.LoginPage = LoginPage(self.driver)
        self.DashBoardPage = self.LoginPage.validate_login()
        self.PimPage = self.DashBoardPage.navigate_to_pim()
        self.DashBoardPage.navigate_to_pim_1()
        self.PimPage.do_click_employee_list()
        flag=self.PimPage.do_search_delete_employee()
        assert flag
        self.PimPage.validate_logout()

