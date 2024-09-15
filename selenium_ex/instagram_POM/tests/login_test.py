from selenium import webdriver
from pages.login_page import LoginPage
from userinfo import UserInfo  
import time

class LoginTest:
    def __init__(self, browser):
        self.browser = browser  
    
    def test_login(self):
        self.browser.get("https://www.instagram.com/")  
        
        login_page = LoginPage(self.browser)  
        login_page.login(UserInfo.username, UserInfo.password)  
        
        self.browser.maximize_window()  
        time.sleep(10) 
        self.browser.quit() 

if __name__ == "__main__":
    browser = webdriver.Chrome()  # Tarayıcıyı başlat
    test = LoginTest(browser)  # Tarayıcı nesnesini geç
    test.test_login()
