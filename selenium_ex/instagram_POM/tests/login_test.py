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
        self.browser.maximize_window()  
        login_page.login(UserInfo.username, UserInfo.password)  
        
       
        time.sleep(10) 
        self.browser.quit() 

if __name__ == "__main__":
    browser = webdriver.Chrome()  
    test = LoginTest(browser)  
    test.test_login()
