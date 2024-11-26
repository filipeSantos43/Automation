from selenium.webdriver.common.by import By
from .base_page import BasePage
from .invoice_list_page import InvoiceListPage

class LoginPage(BasePage):
    """
    Represents the Login Page and its interactions.
    Provides methods to perform login actions, handle input fields, and validate error messages.
    """

    URL = "https://automation-sandbox-python-mpywqjbdza-uc.a.run.app"

    # Locators for Login Page elements
    EMAIL_INPUT = (By.NAME, "username")  
    PASSWORD_INPUT = (By.NAME, "password")  
    LOGIN_BUTTON = (By.ID, "btnLogin")  
    ERROR_MESSAGE = (By.CSS_SELECTOR, "[role='alert']") 

    def load(self):
        """
        Loads the login page in the browser.
        """
        self.driver.get(self.URL)

    def enter_username(self, username):
        """
        Enters the username in the email field.

        Args:
            username (str): The username to input.
        """
        self.enter_text(self.EMAIL_INPUT, username)

    def enter_password(self, password):
        """
        Enters the password in the password field.

        Args:
            password (str): The password to input.
        """
        self.enter_text(self.PASSWORD_INPUT, password)

    def click_login_button(self):
        """
        Clicks the login button to submit the form.
        """
        self.click_element(self.LOGIN_BUTTON)

    def get_error_message(self):
        """
        Verifies if the specified error message is displayed on the page.

        Args:
            message (str): The error message to check.

        Returns:
            bool: True if the message is displayed, False otherwise.
        """
        error_text = self.get_text(self.ERROR_MESSAGE)
        return error_text

    def is_login_successful(self):
        """
        Validates if the login attempt was successful by checking the current URL.

        Returns:
            bool: True if redirected to the Invoice List page, False otherwise.
        """
        return "account" in self.driver.current_url
