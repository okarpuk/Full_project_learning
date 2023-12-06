from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Main_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators
    add_to_cart_button = "//button[@id='add-to-cart-sauce-labs-backpack']"
    cart_button = "//div[@id='shopping_cart_container']"
    menu_button = "//button[@id='react-burger-menu-btn']"
    about_button = "//a[@id='about_sidebar_link']"

# Getters
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

    def get_menu_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.menu_button)))

    def get_about_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.about_button)))

# Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Add to cart button clicked")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Cart button clicked")

    def click_menu_button(self):
        self.get_menu_button().click()
        print("Menu button clicked")

    def click_about_button(self):
        self.get_about_button().click()
        print("About button clicked")

# Methods
    def select_product(self):
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_cart_button()
        self.get_current_url()

    def select_menu_about(self):
        self.get_current_url()
        self.click_menu_button()
        self.click_about_button()
        self.get_current_url()
        self.assert_url('https://saucelabs.com/')
