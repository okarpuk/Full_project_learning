import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import Login_page

class My_OOP_test_1():
    def test_select_product(self):
        driver = webdriver.Chrome()
        base_url = 'https://www.saucedemo.com/'
        driver.delete_all_cookies()
        driver.get(base_url)
        driver.maximize_window()
        time.sleep(3)
        print("Test started")

        user_name = "standard_user"
        user_password = "secret_sauce"

        login = Login_page(driver)
        login.authorization(user_name, user_password)

        add_to_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//button[@id='add-to-cart-sauce-labs-backpack']")))
        add_to_cart.click()
        print("Product added to cart")
        time.sleep(3)

        open_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
        open_cart.click()
        print("Cart opened")
        time.sleep(3)

        check_cart_redirect = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//span[@class='title']")))
        check_text = check_cart_redirect.text
        print(f"SCREEN NAME: {check_text}")
        assert check_text == "Your Cart"
        print(f"TEST PASSED\nSCREEN NAME {check_text} CORRECT")


test_1 = My_OOP_test_1()
test_1.test_select_product()
