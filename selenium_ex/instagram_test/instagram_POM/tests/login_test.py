from selenium import webdriver
import time

driver=webdriver.Chrome()

time.sleep(10)
driver.maximize_window()

driver.get("https://www.instagram.com/")

driver.find_element(By.NAME, "username").send_keys(self.username)
self.driver.find_element(By.NAME, "password").send_keys(self.password)
self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button').click()
self.driver.find_element(By.CLASS_NAME,'x6s0dn4')
