from selenium import webdriver
import time, math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)    
   
    bttn1 = browser.find_element_by_css_selector(".trollface")
    bttn1.click()
    
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(y)
    
    bttn2 = browser.find_element_by_css_selector(".btn")
    bttn2.click()
    
finally:
    time.sleep(10)  
    browser.quit()