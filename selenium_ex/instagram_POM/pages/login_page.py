from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import Base
from userinfo import UserInfo
import time


class LoginPage(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        
    def enter_username(self, username):
        self.browser.find_element(*self.username_textbox).send_keys(username)

    def enter_password(self, password):
        self.browser.find_element(*self.password_textbox).send_keys(password)

    def click_button(self):
        self.browser.find_element(*self.login_button).click()

    def login(self, username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_button()
        WebDriverWait(self.browser, 10).until(EC.url_contains("instagram.com"))


