import pytest
from pages.invoice_list_page import InvoiceListPage
from pages.login_page import LoginPage
from utils.data_provider import DataProvider

class TestTC001:

    @pytest.mark.tc001
    @pytest.mark.parametrize("username,password", DataProvider.get_positive_login_data())
    def test_login_positive(self, setup, username, password):
        """
        Test Case: Test positive login functionality with valid credentials.

        Steps:
            1. Navigate to the login page.
            2. Enter valid username and password.
            3. Click the login button.
            4. Verify that the Invoice List page is loaded.

        """
        # Step 1: Initialize the LoginPage object and load the login page
        login_page = LoginPage(setup)
        login_page.load()

        # Step 2: Enter valid credentials
        login_page.enter_username(username)
        login_page.enter_password(password)

        # Step 3: Attempt to log in
        login_page.click_login_button()

        # Step 4: Verify that the Invoice List page is loaded
        invoice_list_page = InvoiceListPage(setup)
        assert invoice_list_page.is_loaded(), \
            f"Failed to load Invoice List page for username: {username}."
