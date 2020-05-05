from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class ScrapOglas:
    def __init__(self, driver_path: str, search_texts: str):
        self.driver_path = driver_path
        self.search_texts = search_texts

    def __search_google(self, searchText: str):
        self.driver.get('https://www.google.com/')
        self.driver.implicitly_wait(5)
        searchInput = self.driver.find_element_by_xpath('//input[@name="q"]')
        searchInput.send_keys(searchText)
        searchInput.send_keys(Keys.RETURN)
        self.driver.implicitly_wait(5)

    def run(self):
        self.driver = webdriver.Chrome(self.driver_path)
        self.driver.maximize_window()

        for search_text in self.search_texts:
            self.__search_google(search_text)

            links = self.driver.find_elements_by_xpath('//*[@class="ad_cclk"]/a[@href]')
            urls = [link.get_attribute('href') for link in links]

            for url in urls:
                self.driver.get(url)
                self.driver.implicitly_wait(10)

        self.driver.quit()