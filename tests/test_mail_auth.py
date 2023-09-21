import pytest
from pages.login_page import LoginPage
from config.config_loader import config
from data.data_manager import get_user_credentials
import allure

@allure.title("Test username_mail auth")
@allure.description("Checks auth functionality and elements using mail_username input")
@pytest.mark.parametrize("browser_name", ["Chrome", "Safari"])
def test_mail_auth(driver, browser_name):
    base_url = config.get(browser_name, "BaseURL")
    login_page = LoginPage(driver)
    driver.get(base_url)
    
    # Fetch user credentials from JSON
    email, username, password, phone = get_user_credentials()
    assert email and username and password and phone, "Failed to fetch user credentials from JSON"

    # Check if the login page is available
    assert driver.current_url == base_url, "Login page is not available"

    # Check for email input fields by entering an email
    assert login_page.is_login_input_present(), "Login input field is not present"
    login_page.enter_username(email)
    assert login_page.is_login_button_present(), "Login button is not present"
    login_page.click_login_button()

    # Check for the error message after attempting to login with email
    error_message = login_page.get_mail_error_message()
    assert error_message, "Expected error message after entering email, but none found"

    login_page.clear_username_input()

    # Check for email input fields by entering a username
    login_page.enter_username(username)
    assert login_page.is_login_button_present(), "Login button is not present"
    login_page.click_login_button()

    # Enter password from json
    login_page.enter_password(password)

    # Click login button
    login_page.click_login_button()

    error_message = login_page.get_password_error_message()
    assert "Неверный пароль" in error_message, "Password error message not displayed as expected"

    login_page.click_back_button()

    assert login_page.is_login_input_present(), "Login input field is not present"
