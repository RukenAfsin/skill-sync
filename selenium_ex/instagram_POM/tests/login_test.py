from selenium import webdriver
from login_page import LoginPage
from userinfo import UserInfo  
import time

browser = webdriver.Chrome()
browser.get("https://www.instagram.com/")

login_page = LoginPage(browser)
login_page.login(UserInfo.username, UserInfo.password)  

browser.maximize_window()
time.sleep(10)

browser.quit()
