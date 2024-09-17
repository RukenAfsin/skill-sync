from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base_page import Base

class LoginPage(Base):
    def __init__(self, browser):
        super().__init__(browser)
        self.username_textbox = (By.NAME, "username")
        self.password_textbox = (By.NAME, "password")
        self.login_button = (By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        

    def login(self, username, password):
        self.enter_text(*self.username_textbox, username) 
        self.enter_text(*self.password_textbox, password)
        self.click(*self.login_button)
        self.wait_for_element(By.XPATH, '//div[text()="Ana Sayfa"]', timeout=10)

