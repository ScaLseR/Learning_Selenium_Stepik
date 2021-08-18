from selenium import webdriver
import time, os

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)    
             
    f_name = browser.find_element_by_name("firstname")
    f_name.send_keys("Иванов")
    
    l_name = browser.find_element_by_name("lastname")
    l_name.send_keys("Иван")
    
    e_mail = browser.find_element_by_name("email")
    e_mail.send_keys("ivanov@ivan.ivan")
    
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_name = "test.txt"
    file_path = os.path.join(current_dir, file_name)          
    add_file = browser.find_element_by_css_selector("[type='file']")
    add_file.send_keys(file_path)
          
    bttn = browser.find_element_by_css_selector(".btn")
    bttn.click()
        
finally:
    time.sleep(10)  
    browser.quit()