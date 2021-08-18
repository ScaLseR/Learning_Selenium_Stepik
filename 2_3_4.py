from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)    
   
    bttn = browser.find_element_by_css_selector(".btn")
    bttn.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(y)
    
    bttn = browser.find_element_by_css_selector(".btn")
    bttn.click()
    
finally:
    time.sleep(10)  
    browser.quit()