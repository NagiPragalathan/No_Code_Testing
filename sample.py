from selenium import webdriver
from selenium.webdriver.support.select import Select
import time

driver = webdriver.Chrome("C:/Users/nagip/Desktop/New_folder/chromedriver.exe")

driver.set_window_position()
driver.get('http://www.toolsqa.com/automation-practice-form/')
s1 = Select(driver.find_element_by_id('continents'))

s1.select_by_visible_text('Europe')

for opt in s1.options:
    print(opt.text)
    s1.select_by_visible_text(opt.text)
    time.sleep(10)