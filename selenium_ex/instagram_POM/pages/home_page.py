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
        self.profile_button=(By.XPATH, '//span[contains(@class="x1lliihq") and text()="Profil"]')
        self.followers=(By.XPATH, '//a[contains(., "takipçi")]')
        self.visible_follower=(By.XPATH,'//span[@class="_ap3a _aaco _aacw _aacx _aad7 _aade" and contains(text(), "brn.afsn")]')
       
    def bar_click(self):
        self.click(*self.profile_button)
        self.just_wait()


    def get_followers(self):
        self.click(*self.followers)
        self.just_wait()
        self.scroll_until_visible(*self.visible_follower)
        followers = self.collect_followers()
        self.save_to_csv(followers, filename='followers.csv', header='Follower')

