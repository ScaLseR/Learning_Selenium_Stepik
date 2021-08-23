import pytest, time, math
from selenium import webdriver


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    

def resh():
    znach = str(math.log(int(time.time() - 51.7)))
    return znach
        
    
@pytest.mark.parametrize('number', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_parametry_tests(browser, number):
    link = f"https://stepik.org/lesson/{number}/step/1"
    browser.get(link)
    browser.implicitly_wait(5)
    rez = browser.find_element_by_css_selector("textarea")
    rez.send_keys(resh())
    send = browser.find_element_by_css_selector(".submit-submission")
    send.click()
    browser.implicitly_wait(5)
    otv = browser.find_element_by_css_selector(".smart-hints__hint")
    txt = otv.text
    print('text=', txt)
    browser.implicitly_wait(5)
    assert txt =="Correct!", "Не верно!"  
    
   
