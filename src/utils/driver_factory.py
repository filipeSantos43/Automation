import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from dotenv import load_dotenv 

class DriverFactory:

    @staticmethod
    def get_driver():
        """
        Creates and returns an instance of Selenium WebDriver.

        - Loads the chromedriver path from the .env file.
        - Maximizes the browser window on startup.
        
        Returns:
            WebDriver: An instance of Selenium WebDriver.
        """
        # Load environment variables from .env file
        load_dotenv()

        # Get the chromedriver path from the .env file
        chromedriver_path = os.getenv("CHROMEDRIVER_PATH")
        if not chromedriver_path:
            raise FileNotFoundError("CHROMEDRIVER_PATH not found in the .env file.")

        # Set up WebDriver
        service = Service(chromedriver_path)
        options = webdriver.ChromeOptions()
        options.add_argument('--start-maximized')
        driver = webdriver.Chrome(service=service, options=options)
        return driver
