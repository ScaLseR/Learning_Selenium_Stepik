from selenium import webdriver
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  
  
try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    browser.execute_script("window.scrollBy(0, 110);")
    
    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(y)
    
    option1 = browser.find_element_by_id("robotCheckbox")
    option1.click()
    option2 = browser.find_element_by_id("robotsRule")
    option2.click()    
    option3 = browser.find_element_by_css_selector(".btn")
    option3.click()
        
finally:
    time.sleep(10)  
    browser.quit()