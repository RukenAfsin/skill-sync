from selenium import webdriver
from selenium.webdriver.common.by import By
import time



class Base:
    def __init__(self,browser):
         self.browser = webdriver.Chrome()

