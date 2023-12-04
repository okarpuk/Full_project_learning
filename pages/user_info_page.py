from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class User_info_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    first_name = "//input[@id='first-name']"
    last_name = "//input[@id='last-name']"
    postal_code = "//input[@id='postal-code']"
    continue_button = "//input[@id='continue']"

# Getters
    def get_first_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.first_name)))

    def get_last_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.last_name)))

    def get_postal_code(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.postal_code)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

# Actions
    def input_first_name(self, first_name):
        self.get_first_name().send_keys(first_name)
        print("First name entered")

    def input_last_name(self, last_name):
        self.get_last_name().send_keys(last_name)
        print("Last name entered")

    def input_postal_codee(self, postal_code):
        self.get_postal_code().send_keys(postal_code)
        print("Postal_code entered")

    def click_continue_button(self):
        self.get_continue_button().click()
        print("Continue button clicked")

    def confirm_user_info(self):
        self.input_first_name("Jack")
        self.input_last_name("Daniels")
        self.input_postal_codee("12345")
        self.click_continue_button()
        self.get_current_url()

        #self.assert_word(self.get_main_word(), "Products")
