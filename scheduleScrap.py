from scrapOglasClass import ScrapOglas
import time

scrap = ScrapOglas(
    'D:/other/simple/scrapy/chromedriver_win32/chromedriver.exe',
    ['selidbe Zagreb', 'kombi prijevoz', 'kombi prijevoz Zagreb', 'jeftin kombi prijevoz'])

while 1:
    scrap.run()
    time.sleep(120)
