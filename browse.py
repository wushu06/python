from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
def goToMyWebsite(): 
        driver = webdriver.Firefox()
        driver.get("https://nourdigital.com/contact")
        el = driver.find_element_by_xpath("//input[contains(@id,'input_1_1')]")       
        el.send_keys('value', 'nour@gmail.com')
        driver.find_element_by_name("input_2").send_keys("value", "robot testing")       
        driver.find_element_by_id('gform_submit_button_1').click()
                
if __name__ == '__main__':
    goToMyWebsite()
  
'''
results = []
for link in links:
        href = link.get_attribute('href')
        print (href)
        results.append(href)
        '''
