import time
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.user_info_page import User_info_page

def test_buy_product():
    driver = webdriver.Chrome()
    print("Test started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product()

    cp = Cart_page(driver)
    cp.confirm_product()

    uip = User_info_page(driver)
    uip.confirm_user_info()

    time.sleep(5)
