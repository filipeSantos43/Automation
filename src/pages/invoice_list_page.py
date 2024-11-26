# pages/invoice_list_page.py

from selenium.webdriver.common.by import By
from .base_page import BasePage
from .invoice_details_page import InvoiceDetailsPage

class InvoiceListPage(BasePage):
    """
    Represents the Invoice List Page and its interactions.

    This class provides methods to interact with the Invoice List page,
    such as verifying if the page is loaded and clicking on invoice details links.
    """

    # Locators
    FIRST_INVOICE_DETAILS_LINK = (By.XPATH, "(//a[text()='Invoice Details'])[1]")

    def is_loaded(self):
        """
        Checks if the Invoice List page is loaded by verifying the URL.

        Returns:
            bool: True if the Invoice List page is loaded, False otherwise.
        """
        return "account" in self.driver.current_url

    def click_first_invoice_details(self):
        """
        Clicks on the first 'Invoice Details' link available on the page.

        Returns:
            InvoiceDetailsPage: An instance of the InvoiceDetailsPage.

        Raises:
            Exception: If no 'Invoice Details' link is found on the page.
        """
        try:
            self.click_element(self.FIRST_INVOICE_DETAILS_LINK)
            return InvoiceDetailsPage(self.driver)
        except Exception as e:
            raise Exception("No 'Invoice Details' link found on the page.") from e
