import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Config.Config import TestData
"""global fixtures are defined over here"""
@pytest.fixture(scope="class")
def init_driver(request):
    web_driver = webdriver.Chrome()
    request.cls.driver = web_driver
    yield
    web_driver.quit()
@pytest.fixture(scope="class")
def input_data_for_add_user():
    return["test_first","test_mid","test_last","test_unique_id","Test@123456","test_first test_mid"]
