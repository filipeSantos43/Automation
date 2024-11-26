import pytest
from utils.driver_factory import DriverFactory

@pytest.fixture(scope="function")
def setup():
    """
    Pytest fixture to initialize the WebDriver instance for each test.
    
    - This fixture ensures that a browser session is created before each test
      and is properly closed after the test completes.
    - The scope is set to 'function' by default, meaning it runs once per test.

    Yields:
        WebDriver: An instance of the Selenium WebDriver.
    """
    driver = None
    try:
        # Initialize the WebDriver instance
        driver = DriverFactory.get_driver()
        yield driver
    finally:
        # Ensure the WebDriver is properly closed
        if driver:
            driver.quit()
