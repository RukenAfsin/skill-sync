from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import Base
from userinfo import UserInfo
import time


class HomePage(Base):

    def __init(self,browser):
        super().__init__(browser)
        self.profile_button=(By.CLASS_NAME, "xl5mz7h")



    def go_profile(self):
        self.browser.find_element(self.profile_button).click()
