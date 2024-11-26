from selenium.webdriver.common.by import By
from .base_page import BasePage
import re

class InvoiceDetailsPage(BasePage):
    """
    Represents the Invoice Details Page and its interactions.
    
    Provides methods to retrieve detailed invoice information for validation purposes.
    """

    # Locators
    HOTEL_NAME = (By.XPATH, "//h4") 
    INVOICE_DATE = (By.XPATH, "//span[text()='Invoice Date:']/parent::li") 
    DUE_DATE = (By.XPATH, "//span[text()='Due Date:']/parent::li")  
    INVOICE_NUMBER = (By.XPATH, "//h6")  
    BOOKING_CODE = (By.XPATH, "//td[text()='Booking Code']/following-sibling::td")  
    ROOM = (By.XPATH, "//td[text()='Room']/following-sibling::td")  
    CHECK_IN = (By.XPATH, "//td[text()='Check-In']/following-sibling::td")  
    CHECK_OUT = (By.XPATH, "//td[text()='Check-Out']/following-sibling::td")  
    TOTAL_STAY_COUNT = (By.XPATH, "//td[text()='Total Stay Count']/following-sibling::td")      
    TOTAL_STAY_AMOUNT = (By.XPATH, "//td[text()='Total Stay Amount']/following-sibling::td") 
    DEPOSIT_NOW = (By.XPATH, "//td[text()='Total Amount']/ancestor::table//tbody//td[1]")  
    TAX_VAT = (By.XPATH, "//td[text()='Total Amount']/ancestor::table//tbody//td[2]")  
    TOTAL_AMOUNT = (By.XPATH, "//td[text()='Total Amount']/ancestor::table//tbody//td[3]")  
    CUSTOMER_DETAILS = (By.XPATH, "//h5[text()='Customer Details']/following-sibling::div")  

    def is_loaded(self):
        """
        Verifies if the Invoice Details page is loaded by checking the current URL.

        Returns:
            bool: True if the page is loaded, False otherwise.
        """
        return "invoice" in self.driver.current_url

    def get_hotel_name(self):
        """
        Retrieves the hotel name displayed on the page.

        Returns:
            str: The hotel name.
        """
        return self.get_text(self.HOTEL_NAME)

    def get_invoice_date(self):
        """
        Extracts and formats the invoice date.

        Returns:
            str: The invoice date in a clean format (e.g., '14/01/2018').
        """
        full_date = self.get_text(self.INVOICE_DATE)
        return full_date.split(':')[1].strip().replace(' ', '')

    def get_due_date(self):
        """
        Extracts and formats the due date.

        Returns:
            str: The due date in a clean format (e.g., '20/01/2018').
        """
        full_date = self.get_text(self.DUE_DATE)
        return full_date.split(':')[1].strip().replace(' ', '')

    def get_invoice_number(self):
        """
        Extracts the numeric part of the invoice number.

        Returns:
            str: The invoice number (e.g., '110').

        Raises:
            ValueError: If the invoice number pattern is not found.
        """
        invoice_number = self.get_text(self.INVOICE_NUMBER)
        match = re.search(r"Invoice #(\d+)", invoice_number)
        if not match:
            raise ValueError("Invoice number not found in the expected format.")
        return match.group(1)

    def get_booking_code(self):
        """
        Retrieves the booking code.

        Returns:
            str: The booking code.
        """
        return self.get_text(self.BOOKING_CODE)

    def get_customer_details(self):
        """
        Retrieves the customer details.

        Returns:
            str: The customer details.
        """
        return self.get_text(self.CUSTOMER_DETAILS)

    def get_room(self):
        """
        Retrieves the room type.

        Returns:
            str: The room type.
        """
        return self.get_text(self.ROOM)

    def get_check_in(self):
        """
        Retrieves the check-in date.

        Returns:
            str: The check-in date.
        """
        return self.get_text(self.CHECK_IN)

    def get_check_out(self):
        """
        Retrieves the check-out date.

        Returns:
            str: The check-out date.
        """
        return self.get_text(self.CHECK_OUT)

    def get_total_stay_count(self):
        """
        Retrieves the total number of stays.

        Returns:
            str: The total stay count.
        """
        return self.get_text(self.TOTAL_STAY_COUNT)

    def get_total_stay_amount(self):
        """
        Retrieves the total amount for the stay.

        Returns:
            str: The total stay amount.
        """
        return self.get_text(self.TOTAL_STAY_AMOUNT)

    def get_deposit_now(self):
        """
        Retrieves the deposit amount.

        Returns:
            str: The deposit now amount.
        """
        return self.get_text(self.DEPOSIT_NOW)

    def get_tax_vat(self):
        """
        Retrieves the tax and VAT amount.

        Returns:
            str: The tax and VAT amount.
        """
        return self.get_text(self.TAX_VAT)

    def get_total_amount(self):
        """
        Retrieves the total amount.

        Returns:
            str: The total amount.
        """
        return self.get_text(self.TOTAL_AMOUNT)
