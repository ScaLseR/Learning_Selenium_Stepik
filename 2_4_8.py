from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math, time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
  

try: 
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    book_btn = browser.find_element_by_id("book")
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"),"$100"))
    book_btn.click()
    
    browser.execute_script("window.scrollBy(0, 150);")
    
    x_element = browser.find_element_by_id("input_value")
    x = x_element.text
    y = calc(x)
    
    textarea = browser.find_element_by_id("answer")
    textarea.send_keys(y)
    
    bttn2 = browser.find_element_by_id("solve")
    bttn2.click()
    
    
    
    
finally:
    time.sleep(10)  
    browser.quit()