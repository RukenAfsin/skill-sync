from selenium import webdriver
from pages.home_page import HomePage
from userinfo import UserInfo  
import time


class HomeTest:
    def __init__(self,browser):
        self.browser=browser



    def test_barclick(self):
        home_page=HomePage(self.browser)
        home_page.bar_click()
        self.browser.maximize_window()  
        time.sleep(10) 
        self.browser.quit() 

if __name__ == "__main__":
    browser = webdriver.Chrome()  
    test = HomeTest(browser)  
    test.test_barclick()

