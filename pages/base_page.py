from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config.config_loader import wait_time

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait_time = wait_time

    def find_element(self, by_locator):
        """Wait for an element to be visible and then return it."""
        return WebDriverWait(self.driver, self.wait_time).until(EC.visibility_of_element_located(by_locator))

    def click(self, by_locator):
        """Wait for an element to be visible and then click it."""
        self.find_element(by_locator).click()

    def input_text(self, by_locator, text):
        """Wait for an element to be visible and then input text into it."""
        self.find_element(by_locator).send_keys(text)

    def clear_input(self, by_locator):
        """Wait for an input field to be visible and then clear its content."""
        self.find_element(by_locator).clear()

    def get_element_text(self, by_locator):
        """Wait for an element to be visible and then return its text."""
        return self.find_element(by_locator).text

    def wait_for_element_to_be_clickable(self, by_locator):
        """Wait for an element to be clickable."""
        return WebDriverWait(self.driver, self.wait_time).until(EC.element_to_be_clickable(by_locator))

    def is_element_displayed(self, by_locator):
        """Check if an element is displayed."""
        return self.find_element(by_locator).is_displayed()

    def wait_for_element_to_disappear(self, by_locator):
        """Wait for an element to disappear from the page."""
        return WebDriverWait(self.driver, self.wait_time).until_not(EC.visibility_of_element_located(by_locator))
