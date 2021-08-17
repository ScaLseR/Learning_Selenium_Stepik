from selenium import webdriver
import time 

link = "http://suninjuly.github.io/simple_form_find_task.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    l_name = browser.find_element_by_name("last_name")
    l_name.send_keys("Ivan")
    f_name = browser.find_element_by_name("first_name")
    f_name.send_keys("Petrov")
    i_city = browser.find_element_by_class_name("city")
    i_city.send_keys("Smolensk")
    i_country = browser.find_element_by_id("country")
    i_country.send_keys("Russia")
    button = browser.find_element_by_css_selector(".btn")
    button.click()

finally:    
    time.sleep(10)   
    browser.quit()
