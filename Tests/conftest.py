import pytest
from selenium import webdriver
from selenium.webdriver.common.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Config.Config import TestData


@pytest.fixture(scope="class")
def init_driver(request):
     web_driver = webdriver.Chrome(executable_path=TestData.CHROME_EXECUTABLE_PATH)
     request.cls.driver = web_driver
     yield
     web_driver.quit()
