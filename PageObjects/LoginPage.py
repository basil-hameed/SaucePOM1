"""
LoginPage contains the methods related to the login page only
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# import the data and locators
from TestData.data import SauceLabsData
from TestLocators.locators import SauceLabsLocators

class SauceLoginPage:
    
    def login(chromedriver):
        # Use WebDriverWait to wait for the username input field to be visible and enabled
        username_input = WebDriverWait(chromedriver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.username_locator))
        )
        username_input.send_keys(SauceLabsData.username)

        # Similarly, wait for the password input field to be visible and enabled
        password_input = WebDriverWait(chromedriver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.password_locator))
        )
        password_input.send_keys(SauceLabsData.password)

        # Wait for the login button to be clickable
        login_button = WebDriverWait(chromedriver, 10).until(
            EC.element_to_be_clickable((By.ID, SauceLabsLocators.login_button_locator))
        )
        login_button.click()
        return True
    
