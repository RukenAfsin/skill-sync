from selenium import webdriver
import time
from userinfo import username,password
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import json



class Github:
    

    

    def __init__(self):
        self.browser=webdriver.Chrome()
        self.baseUrl="https://github.com/"
        self.username=username
        self.password=password


    def signIn(self):
        self.browser.get(self.baseUrl+"login")
        self.browser.find_element("name","login").send_keys(self.username)
        passwordInput=self.browser.find_element("name","password").send_keys(self.password)
        btn=self.browser.find_element("name", "commit").click()



    def findRepositories(self, keyword):
        self.browser.get(self.baseUrl)
        search_input = self.browser.find_element('xpath', '//*[@id="query-builder-test"]')
        time.sleep(3)
        search_input.send_keys(keyword)
        search_input.send_keys(Keys.ENTER)
        time.sleep(4)

    # def __del__(self):
    #     time.sleep(4)
    #     self.browser.close()




    def another(self):
        self.browser.get(self.baseUrl + "search?q=python&type=repositories")
        source = BeautifulSoup(self.browser.page_source, "html.parser")
        titles = source.find_all('div', {'class': 'Box-sc-g0xbh4-0 kXssRI'})

        with open('python.json', 'a', encoding='utf-8') as file:
            for title in titles:
                spans = title.find_all('span',{'class': 'Text-sc-17v1xeu-0 qaOIC search-match'})
                description=title.find_all('span',{'class': 'Text-sc-17v1xeu-0 kWPXhV search-match'})

                for span,desc in zip(spans,description):
                    print(span.text)
                    print(desc.text)

                    info={
                            'Repository Name': span.text,
                            'Repository Description':desc.text
                    }

                    json.dump(info,file, ensure_ascii=False, indent=4)
                    file.write('\n')

    def getFollowers(self):
        self.browser.get(f'{self.baseUrl}{self.username}?tab=followers')

        follower_elements = self.browser.find_elements('css selector', '.d-table.table-fixed.col-12.width-full.py-4.border-bottom.color-border-muted')

        for follower_element in follower_elements:
            name_element = follower_element.find_elements('css selector', '.f4.Link--primary')
            username_element = follower_element.find_elements('css selector', '.Link--secondary.pl-1')
            
            if name_element and username_element:
                name = name_element[0].text.strip()
                username = username_element[0].text.strip()
                print("Name:", name)
                print("Username:", username)
            elif not name_element:
                print("Name not found")

app=Github()
app.getFollowers()
# app.another()

# app.findRepositories("Python")
# app.signIn()

