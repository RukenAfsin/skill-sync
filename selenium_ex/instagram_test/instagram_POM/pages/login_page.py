from selenium.webdriver.common.by import By



class LoginPage:


    def __init__(self,driver):
        self.driver=driver
        self.username_textbox=(By.NAME, "username")
        self.password_textbox=(By.NAME, "password")
        self.login_button=(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')



