from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """
    A base class for all page objects, providing common Selenium interactions.
    """

    def __init__(self, driver, timeout=10):
        """
        Initializes the base page with a driver and default timeout.

        Args:
            driver (WebDriver): The Selenium WebDriver instance.
            timeout (int, optional): Maximum wait time for elements. Defaults to 10 seconds.
        """
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, self.timeout)

    def wait_for_element(self, locator):
        """
        Waits for an element to be visible on the page.

        Args:
            locator (tuple): The locator tuple (By, value) for the element.

        Returns:
            WebElement: The found element.

        Raises:
            TimeoutException: If the element is not found within the timeout.
        """
        return self.wait.until(EC.visibility_of_element_located(locator))

    def click_element(self, locator):
        """
        Waits for an element and clicks on it.

        Args:
            locator (tuple): The locator tuple (By, value) for the element.

        Raises:
            TimeoutException: If the element is not found or clickable within the timeout.
        """
        element = self.wait_for_element(locator)
        element.click()

    def enter_text(self, locator, text):
        """
        Waits for an input field, clears it, and enters the provided text.

        Args:
            locator (tuple): The locator tuple (By, value) for the input field.
            text (str): The text to be entered.

        Raises:
            TimeoutException: If the input field is not found within the timeout.
        """
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_text(self, locator):
        """
        Waits for an element and retrieves its visible text.

        Args:
            locator (tuple): The locator tuple (By, value) for the element.

        Returns:
            str: The text content of the element.

        Raises:
            TimeoutException: If the element is not found within the timeout.
        """
        return self.wait_for_element(locator).text