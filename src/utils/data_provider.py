import json

class DataProvider:
    """
    A utility class to provide test data for various test cases.
    This class reads data from a JSON file and organizes it into easily
    consumable formats for test cases.
    """

    @staticmethod
    def load_data():
        """
        Loads test data from the JSON file located at `src/data/data.json`.

        Returns:
            dict: A dictionary containing all the test data from the JSON file.
        """
        with open('src/data/data.json', 'r') as file:
            data = json.load(file)
        return data

    @staticmethod
    def get_positive_login_data():
        """
        Retrieves test data for positive login scenarios (TC001).

        Returns:
            list of tuples: Each tuple contains a valid (username, password) pair.
        """
        data = DataProvider.load_data()
        return [(item['Username'], item['Password']) for item in data['TC001']]

    @staticmethod
    def get_negative_login_data():
        """
        Retrieves test data for negative login scenarios (TC002).

        Returns:
            list of tuples: Each tuple contains an invalid (username, password) pair.
        """
        data = DataProvider.load_data()
        return [(item['Username'], item['Password']) for item in data['TC002']]

    @staticmethod
    def get_invoice_details_data():
        """
        Retrieves test data for invoice details validation (TC003).

        Returns:
            dict: A dictionary containing the data for a specific test case
                  related to invoice details.
        """
        data = DataProvider.load_data()
        return data['TC003'][0]
