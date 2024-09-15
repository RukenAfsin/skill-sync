from selenium import webdriver
from tests.login_test import LoginTest

def main():
    browser = webdriver.Chrome()  # Tarayıcıyı başlat
    
    try:
        test = LoginTest(browser)  # Tarayıcı nesnesini geç
        test.test_login()  # Testi çalıştır
        
    except Exception as e:
        print(f"Bir hata oluştu: {e}")
        
    finally:
        browser.quit()  # Tarayıcıyı kapat

if __name__ == "__main__":
    main()
