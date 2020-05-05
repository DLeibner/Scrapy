from parsel import Selector
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def search_google(searchText):
    driver.get('https://www.google.com/')
    driver.implicitly_wait(5)
    searchInput = driver.find_element_by_xpath('//input[@name="q"]')
    searchInput.send_keys(searchText)
    searchInput.send_keys(Keys.RETURN)
    driver.implicitly_wait(5)

driver = webdriver.Chrome('D:/other/simple/scrapy/chromedriver_win32/chromedriver.exe')
driver.maximize_window()

search_google('selidbe Zagreb')

links = driver.find_elements_by_xpath('//*[@class="ad_cclk"]/a[@href]')
urls = [link.get_attribute('href') for link in links]

for url in urls:
    driver.get(url)
    sel = Selector(text = driver.page_source)
    driver.implicitly_wait(10)

driver.quit()