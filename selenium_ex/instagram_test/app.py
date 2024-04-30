from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from userinfo import username, password
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, NoSuchWindowException

class Instagram:

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.base_url = "https://www.instagram.com/"
        self.username = username
        self.password = password

    def sign_in(self):
        self.browser.get(self.base_url)
        time.sleep(5)
        self.browser.find_element(By.NAME, "username").send_keys(self.username)
        self.browser.find_element(By.NAME, "password").send_keys(self.password)
        self.browser.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
        self.browser.maximize_window()
        time.sleep(10)
        self.browser.find_element(By.XPATH, '//div[@role="button" and text() ="Şimdi değil"]').click()
        time.sleep(7)
        path=self.browser.find_element(By.CLASS_NAME, '_a9-z')
        button=path.find_elements(By.TAG_NAME, 'button')
        if len(button) > 1:
            second_button = button[1]
            second_button.click()
            time.sleep(7)

    def getFollowers(self):
        self.sign_in()
        profile_link = self.browser.find_element(By.XPATH, '//span[text()="Profil"]')
        profile_link.click()
        time.sleep(10)

    def followers(self):
        self.getFollowers()
        first=self.browser.find_element(By.CLASS_NAME, "x78zum5")
        second=first.find_elements(By.TAG_NAME, 'li')
        if len(second) > 1:
            followers = second[1]
            followers.click()
            time.sleep(2)

    def follower_name(self, max):
        self.followers()
        time.sleep(3)
        first = self.browser.find_elements(By.CLASS_NAME, 'x1dm5mii')
        count = len(first)
        action = webdriver.ActionChains(self.browser)
        print(f"user count: {count}")

        while count < max:
            try:
                for element in first:  
                    self.browser.execute_script("arguments[0].scrollIntoView(true);", element)
                    time.sleep(1)
                    element.click()
                    action.key_down(Keys.SPACE).key_up(Keys.SPACE).perform()
                    time.sleep(5)
            except (StaleElementReferenceException, NoSuchWindowException):
                continue 

            newCount = len(self.browser.find_elements(By.CLASS_NAME, 'x1dm5mii'))
            if count != newCount:
                count = newCount
                print(f"user count: {count}")
                time.sleep(5)
            else:
                break

        i = 0
        for element in first:
            second = element.find_elements(By.TAG_NAME, 'span')       
            if len(second) > 1:
                f = second[0]
                i += 1
                print(i)
                print(f.text)


app = Instagram()
app.follower_name(50)

