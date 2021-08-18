from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

def calc(x,y):
  return str(int(x)+int(y))
  
try: 
    link = "http://suninjuly.github.io/selects2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("num1")
    x = x_element.text
    
    y_element = browser.find_element_by_id("num2")
    y = y_element.text
        
    z = calc(x,y)
    
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    
    option3 = browser.find_element_by_css_selector(".btn")
    option3.click()
        
finally:
    time.sleep(10)  
    browser.quit()