from selenium.webdriver.firefox.options import Options
from pyvirtualdisplay import Display
from configparser import ConfigParser
from stem.control import Controller
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
from stem import Signal
#import random
import string
import json
#import time
from random import randint
from time import sleep
import sys
import os
from selenium.webdriver.common.keys import Keys



def New_Identity(tor_pw):
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password=tor_pw)
        controller.signal(Signal.NEWNYM)
    sleep(5)

def Initialize_Selenium(Download_Folder):
    # Instantiate Firefox Profile
    profile = webdriver.FirefoxProfile()

    # Security Preferences
    profile.set_preference('places.history.enabled', False)
    profile.set_preference('privacy.clearOnShutdown.offlineApps', True)
    profile.set_preference('privacy.clearOnShutdown.passwords', True)
    profile.set_preference('privacy.clearOnShutdown.siteSettings', True)
    profile.set_preference('privacy.sanitize.sanitizeOnShutdown', True)
    profile.set_preference('signon.rememberSignons', False)
    profile.set_preference('network.cookie.lifetimePolicy', 2)
    profile.set_preference('network.dns.disablePrefetch', True)
    profile.set_preference('network.http.sendRefererHeader', 0)
    profile.set_preference('javascript.enabled', False)
    profile.set_preference('permissions.default.image', 2)
    #profile.set_preference('acceptInsecureCerts', True)
    #profile.set_preference('assumeUntrustedIssuer', True)

    # Set proxy to Tor client
    profile.set_preference('network.proxy.type', 1 )
    profile.set_preference('network.proxy.socks_version', 5 )
    profile.set_preference('network.proxy.socks', '127.0.0.1' )
    profile.set_preference('network.proxy.socks_port', 9050 )
    profile.set_preference('network.proxy.socks_remote_dns', True )

    # Download Preferences
    profile.set_preference('browser.download.dir',Download_Folder)
    profile.set_preference('browser.download.folderList',2)
    profile.set_preference('broswer.download.manager.showWhenStarting', False)
    profile.set_preference('browser.helperApps.neverAsk.openFile','text/csv')
    profile.set_preference('browser.helperApps.neverAsk.saveToDisk','text/csv')
    profile.update_preferences()

    # Make headless
    options = Options()
    #options.set_headless(headless=True)

    # Initialize Webdriver
    driver = webdriver.Firefox(firefox_options=options, firefox_profile=profile)

    return(driver)


def Main():
    

    # Initialize random interval variables for new identity requests
   

   # Initalize directory for automatic file download
    Download_Folder = os.getcwd() + '/Downloads/'
    if not os.path.exists(Download_Folder):
        os.mkdir(Download_Folder) #109.70.100.27 109.70.100.27 199.249.230.72 81.17.27.130 104.244.72.251

    # Test and Find IP
   
   
    while True:   
        driver = Initialize_Selenium(Download_Folder)       
        driver.get("http://icanhazip.com/")
        l = driver.find_element_by_xpath("//pre").text
        print (l)
        goToMyWebsite()
       
        tor_pw = 'password'
        sleep(20)
        driver.close()
        New_Identity(tor_pw)
    
def goToMyWebsite(): 
        driver = webdriver.Firefox()
        driver.get("https://google.com")
        elem = driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("nourdigital")
        elem.send_keys(Keys.RETURN)
        sleep(1)
        links= driver.find_elements_by_xpath("//*[@class='r']//a/h3/div")
        for link in links:
                if link.text == 'nourDigital':
                       # print(link.text)
                        link.click()
                        #sleep(3)
                        driver.find_element_by_id('btn_menu').click()
                        sleep(1)
                        url = 'https://nourdigital.com/contact'
                        driver.find_element_by_xpath('//a[@href="'+url+'"]').click()
                        el = driver.find_element_by_xpath("//input[contains(@id,'input_1_1')]")       
                        el.send_keys('value', 'nour@gmail.com')
                        driver.find_element_by_name("input_2").send_keys("value", "robot testing")       
                        driver.find_element_by_id('gform_submit_button_1').click()
                
   

if __name__ == '__main__':
    Main()