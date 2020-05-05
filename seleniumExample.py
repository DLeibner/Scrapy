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

links = driver.find_elements_by_xpath('//*[@class="r"]/a[@href]')

for link in links:
    try:
        url = link.get_attribute('href')
        driver.get(url)
        sel = Selector(text = driver.page_source)
        driver.implicitly_wait(5)
        search_google('selidbe Zagreb')
    except:
        print("Exception in url")

driver.quit()