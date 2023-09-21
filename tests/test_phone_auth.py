import pytest
from pages.login_page import LoginPage
from config.config_loader import config
from data.data_manager import get_user_credentials
import allure

@allure.title("Test phone auth")
@allure.description("Checks auth functionality and elements using phone input")
@pytest.mark.parametrize("browser_name", ["Chrome", "Safari"])
def test_phone_auth(driver, browser_name):
    base_url = config.get(browser_name, "BaseURL")
    login_page = LoginPage(driver)
    driver.get(base_url)
    
    # Fetch user credentials from JSON
    _, _, _, phone = get_user_credentials()  # Unpack the phone from the tuple
    assert phone, "Failed to fetch user phone number from JSON"

    # Check if the login page is available
    assert driver.current_url == base_url, "Login page is not available"

    # Switch to phone authentication
    login_page.click_phone_switch_button()

    # Assert if the phone input is present
    assert login_page.is_phone_input_present(), "Phone input field is not present"
    
    # Enter the incorrect phone number from json
    login_page.enter_phone_number(phone)

    # Click the login button
    login_page.click_login_button()

    # Check for error message
    assert login_page.get_phone_error_message() == "Недопустимый формат номера", "Unexpected error message displayed"

    # Clear the phone input
    login_page.clear_phone_input()

    # Enter a valid phone number
    login_page.enter_phone_number("+17759766794")

    # Click the login button again
    login_page.click_login_button()

    # Check if the SMS code input field is present
    assert login_page.is_sms_code_field_present(), "SMS code input field is not present"
