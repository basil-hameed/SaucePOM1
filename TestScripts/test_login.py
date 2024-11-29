"""
test_login file contains all the test cases
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# importing login page
from PageObjects.LoginPage import SauceLoginPage

# importing test data and pytest
from TestData.data import SauceLabsData
import pytest

class TestSauceLogin:

    # Booting Method
    @pytest.fixture()
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()
        yield
        self.driver.close()

    # test case for validating login
    def test_validate_login(self, booting_function):
        self.driver.get(SauceLabsData.url)
        assert SauceLoginPage.login(self.driver) == True
        print("SUCCESS : Logged in !")

    # continue with test cases belongs to login scenario
