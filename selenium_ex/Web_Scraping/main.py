from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# WebDriver'ı başlat
browser = webdriver.Chrome()
baseUrl = "https://books.toscrape.com/"

# Web sitesini aç
browser.get(baseUrl)
time.sleep(2)


element_xpath ="//a[contains(text(), 'Travel') or contains(text(),'Nonfiction')]"


category_elements=browser.find_elements(By.XPATH,element_xpath)

category_urls= [element.get_attribute("href") for element in category_elements]

browser.get(category_urls[0])
time.sleep(2)


book_elements = browser.find_elements(By.XPATH, "//div[@class='image_container']//a")

# Kitap URL'lerini al
book_urls = [element.get_attribute("href") for element in book_elements]
# print(len(book_urls))


browser.get(category_urls[1])

# for i in range(1,999):
#     browser.get(f"https://books.toscrape.com/catalogue/category/books/nonfiction_13/page-{i}.html")
#     time.sleep(3)


MAX_PAGINATION=3
url=category_urls[1]
book_urls =[]

for i in range(1, MAX_PAGINATION):
    update_url= url if i==1 else url.replace("index", f"page-{i}")
    driver.get(update_url)
    book_elements= driver.find_elements(By.XPATH, book_elements)