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

# Getters
    def get_add_to_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_to_cart_button)))

    def get_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.cart_button)))

# Actions
    def click_add_to_cart_button(self):
        self.get_add_to_cart_button().click()
        print("Add to cart button clicked")

    def click_cart_button(self):
        self.get_cart_button().click()
        print("Cart button clicked")

    def select_product(self):
        self.get_current_url()
        self.click_add_to_cart_button()
        self.click_cart_button()
        self.get_current_url()