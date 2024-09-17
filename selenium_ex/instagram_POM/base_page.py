from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv

class Base:
    def __init__(self, browser):
        self.browser = browser


    def wait_for_element(self, by, value, timeout=10):
        return WebDriverWait(self.browser, timeout).until(
            EC.presence_of_element_located((by, value))
        )
    
    def click(self, by, value):
        self.browser.find_element(by, value).click()
    
    def enter_text(self, by, value, text):
        self.browser.find_element(by, value).send_keys(text)


    def just_wait(self, timeout=10):
        time.sleep(timeout)


    def click_until_not_clickable(browser, xpath, timeout=10):
        while True:
            try:
                element = WebDriverWait(browser, timeout).until(
                    EC.element_to_be_clickable((By.XPATH, xpath))
                )
                element.click()
                time.sleep(1) 
            except:
                break


    def scroll_until_visible(browser, xpath, scroll_step=500, max_retries=10, wait_time=2):
        retries = 0
        
        while retries < max_retries:
            try:
                WebDriverWait(browser, wait_time).until(
                    EC.visibility_of_element_located((By.XPATH, xpath))
                )
                print("Öğe görünür hale geldi.")
                return
            except:
                browser.execute_script(f"window.scrollBy(0, {scroll_step});")
                print(f"{retries+1}. denemede öğe bulunamadı, sayfa kaydırılıyor...")
                retries += 1
                time.sleep(wait_time) 
        
        print("Öğe hala görünür değil veya bulunamadı.")


    def save_to_csv(items, filename='items.csv', header='Item'):
        with open(filename, 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([header])
            writer.writerows([[item] for item in items])