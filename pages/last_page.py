from base.base_class import Base
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Last_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def create_screenshot(self):
        self.screenshot()