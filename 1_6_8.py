from selenium import webdriver
import time 

link = "http://suninjuly.github.io/find_xpath_form"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    l_name = browser.find_element_by_name("last_name")
    l_mame.send_keys("Ivan")
    
    f_name = browser.find_element_by_name("first_name")
    f_name.send_keys("Petrov")
    
    i_city = browser.find_element_by_class_name("city")
    i_input3.send_keys("Smolensk")
    
    i_contry = browser.find_element_by_id("country")
    i_contr.send_keys("Russia")
    
    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(10)    
    browser.quit()