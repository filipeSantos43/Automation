import pytest
from pages.invoice_details_page import InvoiceDetailsPage
from pages.invoice_list_page import InvoiceListPage
from pages.login_page import LoginPage
from utils.data_provider import DataProvider


class TestTC003:

    @pytest.mark.tc003
    def test_validate_invoice_details(self, setup):
        """
        Test case: Validate invoice details for a specific hotel.

        Steps:
            1. Load the login page and perform login.
            2. Navigate to the Invoice List page.
            3. Click on the Invoice Details link for a specified hotel, opening a new tab.
            4. Switch to the new tab and validate invoice details.
        """

        # Load test data
        data = DataProvider.get_invoice_details_data()
        
        # Step 1: Log in
        login_page = LoginPage(setup)
        login_page.load()  # Load the login page
        login_page.enter_username(data['Username'])
        login_page.enter_password(data['Password'])
        login_page.click_login_button()
        
        # Step 2: Verify navigation to the Invoice List page
        invoice_list_page = InvoiceListPage(setup)
        assert invoice_list_page.is_loaded(), "Invoice List page did not load."

        # Step 3: Click on the Invoice Details link for the specified hotel
        invoice_list_page.click_first_invoice_details()

        driver = setup
        original_tab = driver.current_window_handle
        try:
            new_tab = [tab for tab in driver.window_handles if tab != original_tab][0]
            driver.switch_to.window(new_tab)
        except IndexError:
            pytest.fail("Failed to switch to the new tab containing Invoice Details page.")

        # Step 4: Validate that the Invoice Details page is loaded
        invoice_details_page = InvoiceDetailsPage(driver)
        assert invoice_details_page.is_loaded(), "Invoice Details page did not load."

        assert invoice_details_page.get_hotel_name() == data['HotelName'], "Hotel Name mismatch."
        assert invoice_details_page.get_invoice_date() == data['InvoiceDate'], "Invoice Date mismatch."
        assert invoice_details_page.get_due_date() == data['DueDate'], "Due Date mismatch."
        assert invoice_details_page.get_invoice_number() == data['InvoiceNumber'], "Invoice Number mismatch."
        assert invoice_details_page.get_booking_code() == data['BookingCode'], "Booking Code mismatch."
        assert invoice_details_page.get_customer_details() == data['CustomerDetails'], "Customer Details mismatch."
        assert invoice_details_page.get_room() == data['Room'], "Room mismatch."
        assert invoice_details_page.get_check_in() == data['CheckIn'], "Check-In mismatch."
        assert invoice_details_page.get_check_out() == data['CheckOut'], "Check-Out mismatch."
        assert invoice_details_page.get_total_stay_count() == data['TotalStayCount'], "Total Stay Count mismatch."
        assert invoice_details_page.get_total_stay_amount() == data['TotalStayAmount'], "Total Stay Amount mismatch."
        assert invoice_details_page.get_deposit_now() == data['DepositNow'], "Deposit Now mismatch."
        assert invoice_details_page.get_tax_vat() == data['Tax&VAT'], "Tax & VAT mismatch."
        assert invoice_details_page.get_total_amount() == data['TotalAmount'], "Total Amount mismatch."
