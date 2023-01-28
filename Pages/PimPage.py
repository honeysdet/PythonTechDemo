from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage


class PimPage(BasePage):
    MENU_PIM = (By.XPATH, "// span[text() = 'PIM']")
    TAB_CONF = (By.XPATH, "// span[text() = 'Configuration ']")
    TAB_EMPLOYEE_lIST = (By.XPATH, "// a[text() = 'Employee List']")
    TAB_EMPLOYEE_ADD = (By.XPATH, "// a[text() = 'Add Employee']")
    TAB_REPORT = (By.XPATH, "// a[text() = 'Reports']")
    BTN_ADD = (By.XPATH, "// button[text() = ' Add ']")
    MENU_PIM = (By.XPATH, "//span[text()='PIM']")
    MENU_ADD = (By.XPATH, "// button[text() = ' Add ']")
    INPUT_NAME = (By.XPATH, "// input[ @ name = 'firstName']")
    INPUT_MID_NAME = (By.XPATH, "// input[ @ name = 'middleName']")
    INPUT_LAST_NAME = (By.XPATH, "// input[ @ name = 'lastName']")
    FLG_LOGIN = (By.XPATH, "//input[@type='checkbox']/parent::label/span")
    INPUT_USER_NAME = (By.XPATH, "(//input[@class='oxd-input oxd-input--active'])[3]")
    INPUT_PASSWORD = (By.XPATH, "(//input[@type='password'])[1]")
    INPUT_CONF_PASSWORD = (By.XPATH, "(//input[@type='password'])[2]")
    BTN_CONF_SUBMIT = (By.XPATH, "//button[@type='submit']")
    TOAST_MSG = (By.XPATH, "//p[text()='Successfully Saved']")
    INPUT_SEARCH_EMP = (By.XPATH, "(// input)[2]")
    BTN_SEARCH = (By.XPATH, "// button[ @ type = 'submit']")
    LIST_EMPLOYEE = (By.XPATH, "//div[starts-with(text(),'abc pqr')]")
    BTN_DELETE_EMP = (By.XPATH, "//i[@class='oxd-icon bi-trash']")
    BTN_DELETE_CONF = (By.XPATH, "// button[text() = ' Yes, Delete ']")
    TOAST_MSG_DELETE = (By.XPATH, "//p[text()='Successfully Deleted']")



    LOGOUT_LINK = (By.XPATH, " //i[contains(@class,'userdropdown-icon')]")
    LOGOUT_BTN = (By.XPATH, "//a[text()='Logout']")

    def is_pim_visible(self):
        return self.is_visible(self.MENU_PIM)

    def is_conf_visible(self):
        return self.is_visible(self.TAB_CONF)

    def is_employee_list_visible(self):
        return self.is_visible(self.TAB_EMPLOYEE_lIST)

    def is_employee_add_visible(self):
        return self.is_visible(self.TAB_EMPLOYEE_ADD)

    def is_report_visible(self):
        return self.is_visible(self.TAB_REPORT)

    def do_click_add_btn(self):
        self.do_click(self.BTN_ADD)

    def do_click_employee_list(self):
        self.do_click(self.TAB_EMPLOYEE_lIST)

    def input_data_for_adduser(self):

        self.do_send_key(self.INPUT_NAME,"abc")
        self.do_send_key(self.INPUT_MID_NAME,"pqr")
        self.do_send_key(self.INPUT_LAST_NAME,"xyz")
        self.do_click(self.FLG_LOGIN)
       # self.do_javascript_click(self.FLG_LOGIN)
        self.do_send_key(self.INPUT_USER_NAME, "abc123438")
        self.do_send_key(self.INPUT_PASSWORD, "Abc@1234567")
        self.do_send_key(self.INPUT_CONF_PASSWORD, "Abc@1234567")
        self.do_click(self.BTN_CONF_SUBMIT)
        return self.is_visible(self.TOAST_MSG)

    def do_search_new_employee(self):
        self.do_send_key(self.INPUT_SEARCH_EMP, "abc pqr")
        self.do_click(self.BTN_SEARCH)
        return self.is_visible(self.LIST_EMPLOYEE)

    def do_search_delete_employee(self):
        self.do_send_key(self.INPUT_SEARCH_EMP, "abc pqr")
        self.do_click(self.BTN_SEARCH)
        self.do_click(self.BTN_DELETE_EMP)
        self.do_click(self.BTN_DELETE_CONF)
        return self.is_visible(self.TOAST_MSG_DELETE)


    def validate_logout(self):
        self.do_click(self.LOGOUT_LINK)
        self.do_click(self.LOGOUT_BTN)