import time
from base.base_class import Base

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login_page(Base):

    url = 'https://www.saucedemo.com/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    user_name = "//input[@id='user-name']"
    password = "//input[@id='password']"
    button_login = "//input[@id='login-button']"

# Getters
    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_button_login(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_login)))

# Actions
    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print("User name entered")

    def input_password(self, password):
        self.get_password().send_keys(password)
        print("Password entered")

    def click_login_button(self):
        self.get_button_login().click()
        print("Login button clicked")



    def authorization(self, user_field, password_field):
        user_name = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='user-name']")))
        user_name.send_keys(user_field)
        print("Login entered")

        password = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='password']")))
        password.send_keys(password_field)
        print("Password entered")
        time.sleep(3)

        button_login = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//input[@id='login-button']")))
        button_login.click()
        print("Login clicked")
