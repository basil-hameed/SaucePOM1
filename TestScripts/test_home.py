"""
test_home file contains all the test cases related to homepage
"""
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from TestData.data import SauceLabsData
from TestLocators.locators import SauceLabsLocators
from PageObjects.HomePage import SauceHomePage
import pytest

class TestSauceHome:

    # Booting Method
    @pytest.fixture(scope="function")
    def booting_function(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        yield
        self.driver.close()
    
    # Test case to validate the title 
    def test_title(self, booting_function):
        self.driver.get(SauceLabsData.url)
        assert SauceHomePage.validate_title(self.driver) == True
        print("SUCCESS : Title Validated !")

    # Test case to validate the URL
    def test_url(self, booting_function):
        self.driver.get(SauceLabsData.url)
        assert SauceHomePage.validate_url(self.driver) == True
        print("SUCCESS : URL Validated !")

    # continue with test cases belongs to homepage scenario
