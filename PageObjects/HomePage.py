"""
HomePage contains the methods related to the home page only
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

# import the data and locators
from TestData.data import SauceLabsData
from TestLocators.locators import SauceLabsLocators

class SauceHomePage:
    
    def validate_title(chromedriver):
        if chromedriver.title == SauceLabsData.title:
            return True
    
    def validate_url(chromedriver):
        if chromedriver.current_url == SauceLabsData.url:
            return True
