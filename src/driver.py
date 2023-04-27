"""This module hosts the driver class"""
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

class Driver():
    """Class to initialize the driver"""
    def __init__(self):
        options = webdriver.ChromeOptions()
        options.binary_location = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
        chrome_driver_binary = "/opt/homebrew/bin/chromedriver"
        self.driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    def quit(self,):
        """Method to quit the driver"""
        self.driver.quit()

    def get(self, url):
        """Method to get to a specific webpage"""
        return self.driver.get(url)

    def find_element_by_id(self, identifier):
        """Method to get the element by its id"""
        return self.driver.find_element(By.ID, identifier)

    def find_elements_by_id(self, identifier):
        """Method to get all elements with the specific id"""
        return self.driver.find_elements(By.ID, identifier)

    def find_element_by_class_name(self, identifier):
        """Method to get the element by its class name"""
        return self.driver.find_element(By.CLASS_NAME, identifier)
    
    def find_elements_by_class_name(self, identifier):
        """Method to get all elements with the specific class name"""
        return self.driver.find_elements(By.CLASS_NAME, identifier)

    def scroll_to_element(self, element):
        """Method to scroll to a specific element"""
        ActionChains(self.driver)\
        .scroll_to_element(element)\
        .perform()
        # Then wait for the page to load (1sec)
        sleep(4)
        
    def scroll_to_end_of_page(self,):
        self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')

