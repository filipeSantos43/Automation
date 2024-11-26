# Automation Test Project

## Overview
This project is a Selenium-based test automation framework designed to validate the functionality of a sample web application. The framework utilizes Python, Selenium WebDriver, and Pytest, following the Page Object Model (POM) design pattern. It is designed for maintainability, scalability, and ease of use.

## Project Structure

project_root/
│
├── src/               
│   ├── data/                           
│   │   └── data.json                   # Data for test cases
|   │   │
│   ├── pages/                          
│   │   ├── base_page.py                # Base page with reusable methods
│   │   ├── invoice_details_page.py     # Page Object for the Invoice Details page
│   │   ├── invoice_list_page.py        # Page Object for the Invoice List page
│   │   └── login_page.py               # Page Object for the Login page
│   │
│   ├── utils/                          
│   │   ├── data_provider.py            # Data provider for test cases
│   │   └── driver_factory.py           # Factory class for initializing the WebDriver
│   │
│   ├── tests/                          
│   │   ├── test_tc001.py               # Positive login test
│   │   ├── test_tc002.py               # Negative login tests
│   │   └── test_tc003.py               # Invoice Details validation
│   │
│   └── conftest.py                     # Pytest configuration and WebDriver setup
│
├── chromedriver/                       
│   └── chromedriver                    # ChromeDriver executable
│
├── reports/                            
│   └── report.html                     # Generated HTML test report
│
├── .env                                # Environment variables (e.g., ChromeDriver path)
├── .gitignore                          # Ignored files and directories for Git
├── requirements.txt                    # Python dependencies
├── README.md                           # Project documentation
└── docs/                              
    └── readme.md                       # Detailed documentation (optional)
## Prerequisites

Before running the tests, ensure you have the following installed on your machine:

- Python 3.11+
- Google Chrome (latest stable version)
- ChromeDriver (matching the installed Chrome version)    

You can check your Chrome version by navigating to chrome://settings/help in your browser.

## Setup Instructions

1. Clone the Repository

```bash
git clone <repository_url>
cd project_root
```

2. Install Dependencies

```bash
pip install -r requirements.txt
```

3. Set ChromeDriver Path in .env file (if you have chromedriver on the project root folder, just type CHROMEDRIVER_PATH=./chromedriver)

4. Validate the Setup Verify that all dependencies are installed, and the ChromeDriver is correctly configured:

## Running the Tests

### Run All Tests
To execute all the test cases:

```bash
pytest src/tests --tb=short --html=reports/report.html
```

### Run a Specific Test
To execute a specific test file:

```bash
pytest src/tests/<test_file_name>.py --tb=short --html=reports/report.html
```

Example:

```bash
pytest src/tests/test_tc001.py --tb=short --html=reports/report.html
```

Test Report
After the tests run, an HTML report will be generated at reports/report.html

## Test Descriptions

### TestTC001: Positive Login
File: src/tests/test_tc001.py
Description: Validates a successful login using valid credentials.
Data Source: data.json (under src/data/)
Expected Outcome: User lands on the Invoice List page after logging in.

### TestTC002: Negative Login
File: src/tests/test_tc002.py
Description: Validates login failure with invalid credentials.
Data Source: data.json (under src/data/)
Expected Outcome:  An error message is displayed on the Login page.

### TestTC003: Invoice Details Validation
File: src/tests/test_tc003.py
Description: Validates the invoice details displayed on the Invoice Details page.
Data Source: data.json (under src/data/)
Expected Outcome: The invoice details are displayed correctly on the Invoice Details page.



