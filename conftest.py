import pytest
import json
from selenium import webdriver
import logging
from config.config_loader import config
from data.data_manager import fetch_user_data

# Set up logging
logging.basicConfig(filename="logs/test.log", level=logging.DEBUG)

BROWSERS = {
    'Chrome': webdriver.Chrome,
    'Safari': webdriver.Safari
    # Add other browsers and their corresponding webdriver classes as needed
}

@pytest.fixture(scope="session", autouse=True)
def populate_users_json_fixture():
    """Fixture to populate users.json with data from jsonplaceholder."""
    users = fetch_user_data()
    with open('data/users.json', 'w') as file:
        json.dump(users, file, indent=4)

@pytest.fixture(scope="function")
def driver(browser_name):
    """Fixture to initialize and quit the browser."""
    browser_type = config.get(browser_name, "Browser")
    browser = BROWSERS[browser_type]()
    browser.implicitly_wait(10)
    browser.maximize_window()
    yield browser
    browser.quit()
