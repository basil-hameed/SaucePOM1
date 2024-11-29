# SaucePOM

Website Link: https://www.saucedemo.com/v1/

## Test Objective
Launching sauce demo website and testing start automation, login functionality and shutdown using pytest framework with a page object model POM Pattern. 
Here's a professional `README.md` template for the GitHub repository of a project titled **"E-Commerce Site using pytest and Selenium"**.

---

# E-Commerce Site using pytest and Selenium

## Project Overview

This project is a test automation suite for an e-commerce website, developed using `pytest` and `Selenium`. The main objective is to automate functional testing for various critical flows in an e-commerce application, such as user authentication, product search, adding items to cart, and checkout. By using `pytest` and `Selenium`, the suite ensures that the site operates as expected and offers a seamless experience to users.

## Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Setup and Installation](#setup-and-installation)
- [Running Tests](#running-tests)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated Login Tests**: Verifies user login functionality, including positive and negative scenarios.
- **Product Search Tests**: Ensures accurate search functionality and proper display of search results.
- **Add to Cart and Checkout Tests**: Checks the add-to-cart functionality and ensures the checkout process is smooth and bug-free.
- **Responsive Testing**: Ensures that key functionalities work well across various screen sizes (desktop, tablet, mobile).

## Tech Stack

- **Programming Language**: Python
- **Test Framework**: pytest
- **Automation Tool**: Selenium WebDriver
- **Reporting**: pytest-html
- **Browser Compatibility**: Chrome, Firefox, and optionally, Edge
- **CI/CD Integration**: GitHub Actions

## Setup and Installation

To set up and run this project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/username/ecommerce-site-pytest-selenium.git
   cd ecommerce-site-pytest-selenium
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory to store sensitive information such as login credentials and URLs. Example:
     ```
     BASE_URL=https://example.com
     USER_EMAIL=test@example.com
     USER_PASSWORD=yourpassword
     ```

## Running Tests

To execute tests, use the following commands:

1. **Run All Tests**:
   ```bash
   pytest
   ```

2. **Generate HTML Report**:
   ```bash
   pytest --html=report.html
   ```

3. **Run Tests by Marker** (e.g., only "login" tests):
   ```bash
   pytest -m login
   ```

4. **Headless Browser Execution**:
   - You can set up tests to run in headless mode by configuring the `pytest.ini` file or directly in your test script.

## Project Structure

```
ecommerce-site-pytest-selenium/
├── tests/                     # All test cases
│   ├── test_login.py          # Login tests
│   ├── test_search.py         # Product search tests
│   ├── test_cart.py           # Add to cart and checkout tests
├── pages/                     # Page Object Models for each page
│   ├── login_page.py
│   ├── search_page.py
│   ├── cart_page.py
├── utils/                     # Utility scripts
│   ├── config.py              # Configuration management
│   ├── helpers.py             # Helper functions
├── .env                       # Environment variables
├── pytest.ini                 # pytest configuration
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```
