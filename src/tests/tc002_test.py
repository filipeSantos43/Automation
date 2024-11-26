import pytest
from pages.login_page import LoginPage
from utils.data_provider import DataProvider

class TestTC002:

    @pytest.mark.tc002
    @pytest.mark.parametrize("username,password", DataProvider.get_negative_login_data())
    def test_login_negative(self, setup, username, password):
        """
        Test case: Test negative login attempts with invalid credentials.

        Steps:
            1. Navigate to the login page.
            2. Enter invalid username and password.
            3. Click the login button.
            4. Assert that the error message is displayed.
        """
        # Initialize the LoginPage object
        login_page = LoginPage(setup)

        # Step 1: Load the login page
        login_page.load()

        # Step 2: Enter invalid credentials
        login_page.enter_username(username)
        login_page.enter_password(password)

        # Step 3: Attempt to log in
        login_page.click_login_button()

        # Step 4: Verify that the error message is displayed
        try:
            assert login_page.get_error_message() == "Wrong username or password."
        except Exception as e:
            pytest.fail(f"The error message 'Wrong username or password.' was not displayed on the screen.")
