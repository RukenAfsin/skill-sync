from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import Base
import time

class LoginPage(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        self.button = (By.XPATH, "//div[contains(@class, 'x1i10hfl') and contains(text(), 'Şimdi değil')]")
        self.not_now=(By.XPATH, " //div[@class='_a9-z']//button[contains(text(), 'Şimdi Değil')]")
       


    def login(self, username, password):
        time.sleep(2)
        self.enter_text(*self.username_textbox, username) 
        time.sleep(2)
        self.enter_text(*self.password_textbox, password)
        self.click(*self.login_button)
        self.wait_for_element(*self.button, timeout=10)
        self.click(*self.button)
        self.wait_for_element(*self.not_now,timeout=5)
        self.click(*self.not_now)
        self.wait_for_element(By.XPATH, "//span[contains(@class, 'x1lliihq') and contains(text(), 'Ana Sayfa')]", timeout=10)

        print('görüldü')

