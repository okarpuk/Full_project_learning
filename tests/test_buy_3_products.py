import time
from selenium import webdriver
from pages.cart_page import Cart_page
from pages.last_page import Last_page
from pages.login_page import Login_page
from pages.main_page import Main_page
from pages.payment_page import Payment_page
from pages.user_info_page import User_info_page

def test_buy_product_1():
    driver = webdriver.Chrome()
    print("\nTest 1 started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_1()

    cp = Cart_page(driver)
    cp.confirm_product()

    # uip = User_info_page(driver)
    # uip.confirm_user_info()
    #
    # pp = Payment_page(driver)
    # pp.click_finish_button()
    #
    # lp = Last_page(driver)
    # lp.create_screenshot()

    print("Test 1 finished")
    time.sleep(3)
    driver.quit()

def test_buy_product_2():
    driver = webdriver.Chrome()
    print("\nTest 2 started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_2()

    cp = Cart_page(driver)
    cp.confirm_product()

    print("Test 2 finished")
    time.sleep(3)
    driver.quit()

def test_buy_product_3():
    driver = webdriver.Chrome()
    print("\nTest 3 started")

    login = Login_page(driver)
    login.authorization()

    mp = Main_page(driver)
    mp.select_product_3()

    cp = Cart_page(driver)
    cp.confirm_product()

    print("Test 3 finished")
    time.sleep(3)
    driver.quit()