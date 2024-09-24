from selenium import webdriver
from tests.login_test import LoginTest
from tests.home_test import HomeTest
import time

def main():
    browser = webdriver.Chrome()  # Tarayıcıyı başlat
    time.sleep(2)  # Tarayıcının tamamen açılmasını bekle
    
    try:
        test = LoginTest(browser)  # Tarayıcı nesnesini geç
        test.test_login()  # Testi çalıştır
        test_home = HomeTest(browser)
        test_home.test_barclick()
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        
    finally:
        browser.quit()  # Tarayıcıyı kapat


if __name__ == "__main__":
    main()
