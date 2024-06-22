from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



browser = webdriver.Chrome()
browser.maximize_window()

url = ""

browser.get(url)
browser.find_element(By.XPATH,".//button[@id='onetrust-reject-all-handler']").click()
time.sleep(2)

# actions = ActionChains(browser)
# actions.move_by_offset(10, 10).click().perform()
# time.sleep(2)
# first_li = browser.find_element(By.XPATH, "//*[@id='container']/div[3]/div/aside/div[1]/nav/ul[4]/li[1]/ul/li[1]/a")
# first_li.click()

div_element = browser.find_element(By.XPATH, "//div[@class='sahibindenSelect-holder']")
span_elements = div_element.find_elements(By.TAG_NAME, "span")

for span in span_elements:
    if span.text.strip().lower() == 'satılık':
        span.click()
        break

time.sleep(2) 

li_element = browser.find_element(By.XPATH, "//li[@data-value='16622']")
li_element.click()

time.sleep(5) 




div_element = browser.find_element(By.XPATH, "//div[@class='sahibindenSelect closed subCategoryArea']")
span_elements = div_element.find_elements(By.TAG_NAME, "span")

for span in span_elements:
    if span.text.strip().lower() == 'konut':
        span.click()
        break

li_element = WebDriverWait(browser, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//li[@data-value='16624']"))
)
li_element.click()
print('konuta tıklandı')
time.sleep(5) 






div_elements = browser.find_elements(By.XPATH, "//div[@class='sahibindenSelect-holder']")

if len(div_elements) > 2:
        div_elements[2].click()
        print("İndeks 2 olan 'sahibindenSelect-holder' elementi tıklandı.")
        li_element = browser.find_element(By.XPATH, "//li[@data-value='6']")
        li_element.click()
else:
        print("İndeks 2 olan 'sahibindenSelect-holder' elementi bulunamadı.")




div_elements = browser.find_elements(By.XPATH, "//div[@class='sahibindenSelect-holder']")

if len(div_elements) > 2:
        div_elements[2].click()
        print("İndeks 2 olan 'sahibindenSelect-holder' elementi tıklandı.")
        li_element = browser.find_element(By.XPATH, "//li[@data-value='6']")
        li_element.click()
else:
        print("İndeks 2 olan 'sahibindenSelect-holder' elementi bulunamadı.")

time.sleep(2)




div_elements = browser.find_elements(By.XPATH, "//div[@class='sahibindenSelect-holder']")

if len(div_elements) > 3:
        div_elements[3].click()
        print("İndeks 3 olan 'sahibindenSelect-holder' elementi tıklandı.")
        li_element = browser.find_element(By.XPATH, "//li[@data-value='59']")
        li_element.click()
else:
        print("İndeks 2 olan 'sahibindenSelect-holder' elementi bulunamadı.")

browser.quit()