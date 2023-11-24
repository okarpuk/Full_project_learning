import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_select_product(self):
    driver = webdriver.Chrome()
    print("Test started")

    open_cart = WebDriverWait(driver, 30).until(EC.element_to_be_clickable((By.XPATH, "//div[@id='shopping_cart_container']")))
    open_cart.click()
    print("Cart opened")
    time.sleep(3)
