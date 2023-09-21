from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):

    # Locators
    LOGIN_INPUT = (By.XPATH, "(//*[@id='passp-field-login'])")
    PASSWORD_INPUT = (By.ID, "passp-field-passwd")
    PHONE_INPUT = (By.ID, "passp-field-phone")
    LOGIN_BUTTON = (By.ID, "passp:sign-in")
    MAIL_ERROR_MESSAGE = (By.ID, "field:input-login:hint")
    PASSWORD_ERROR_MESSAGE = (By.ID, "field:input-passwd:hint")
    PHONE_ERROR_MESSAGE = (By.ID, "field:input-phone:hint")
    EMAIL_SWITCH_BUTTON = (By.CSS_SELECTOR, "button[data-t='button:default'][data-type='login']")
    PHONE_SWITCH_BUTTON = (By.CSS_SELECTOR, "button[data-t='button:clear'][data-type='phone']")
    SMS_CODE_FIELD = (By.ID, "passp-field-phoneCode")
    BACK_BUTTON = (By.CSS_SELECTOR, "a[data-t='backpane']")

    # Username related methods
    def enter_username(self, username):
        """Enter the username in the username input field."""
        self.input_text(self.LOGIN_INPUT, username)

    def clear_username_input(self):
        """Clear the content of the username input field using JavaScript."""
        element = self.find_element(self.LOGIN_INPUT)
        element.click()  # Focus on the input
        self.driver.execute_script("arguments[0].value = '';", element)

    def is_login_input_present(self):
        """Check if the login input field is present."""
        return self.is_element_displayed(self.LOGIN_INPUT)

    # Password related methods
    def enter_password(self, password):
        """Enter the password in the password input field."""
        self.input_text(self.PASSWORD_INPUT, password)

    def get_password_error_message(self):
        """Get the error message related to the password input."""
        return self.get_element_text(self.PASSWORD_ERROR_MESSAGE)

    # Phone related methods
    def enter_phone_number(self, phone_number):
        """Enter the phone number in the phone input field."""
        self.input_text(self.PHONE_INPUT, phone_number)

    def clear_phone_input(self):
        """Clear the content of the phone input field."""
        self.clear_input(self.PHONE_INPUT)

    def get_phone_error_message(self):
        """Get the error message related to the phone input."""
        return self.get_element_text(self.PHONE_ERROR_MESSAGE)

    def is_phone_input_present(self):
        """Check if the phone input field is present."""
        return self.is_element_displayed(self.PHONE_INPUT)

    # General methods
    def click_login_button(self):
        """Click the login button."""
        self.click(self.LOGIN_BUTTON)

    def is_login_button_present(self):
        """Check if the login button is present."""
        return self.is_element_displayed(self.LOGIN_BUTTON)

    def get_mail_error_message(self):
        """Get the error message related to the email input."""
        return self.get_element_text(self.MAIL_ERROR_MESSAGE)

    def click_phone_switch_button(self):
        """Click the button to switch to phone login."""
        self.click(self.PHONE_SWITCH_BUTTON)

    def click_email_switch_button(self):
        """Click the button to switch to email login."""
        self.click(self.EMAIL_SWITCH_BUTTON)

    def enter_sms_code(self, sms_code):
        """Enter the SMS code in the SMS code input field."""
        self.input_text(self.SMS_CODE_FIELD, sms_code)

    def is_sms_code_field_present(self):
        """Check if the SMS code input field is present."""
        return self.is_element_displayed(self.SMS_CODE_FIELD)

    def click_back_button(self):
        """Click the back button."""
        self.click(self.BACK_BUTTON)
