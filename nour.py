from selenium import webdriver
from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.firefox.options import Options
import subprocess
import os
import requests
from stem import Signal
from stem.control import Controller

profileTor = '/etc/tor/' #  torrc
binary = os.path.expanduser("~/.local/share/torbrowser/tbb/x86_64/tor-browser_en-US/Browser/firefox")

firefox_binary = FirefoxBinary(binary)
firefox_profile = FirefoxProfile(profileTor)


#set some privacy settings
firefox_profile.set_preference( "places.history.enabled", False )
firefox_profile.set_preference( "privacy.clearOnShutdown.offlineApps", True )
firefox_profile.set_preference( "privacy.clearOnShutdown.passwords", True )
firefox_profile.set_preference( "privacy.clearOnShutdown.siteSettings", True )   
firefox_profile.set_preference( "privacy.sanitize.sanitizeOnShutdown", True )
firefox_profile.set_preference( "signon.rememberSignons", False )
firefox_profile.set_preference( "network.cookie.lifetimePolicy", 2 )
firefox_profile.set_preference( "network.dns.disablePrefetch", True )
firefox_profile.set_preference( "network.http.sendRefererHeader", 0 )

#set socks proxy
firefox_profile.set_preference( "network.proxy.type", 1 )
firefox_profile.set_preference( "network.proxy.socks_version", 5 )
firefox_profile.set_preference( "network.proxy.socks", '127.0.0.1' )
firefox_profile.set_preference( "network.proxy.socks_port", 9150 )
firefox_profile.set_preference( "network.proxy.socks_remote_dns", True )

#if you're really hardcore about your security
#js can be used to reveal your true i.p.
#firefox_profile.set_preference( "javascript.enabled", False )

#get a huge speed increase by not downloading images
firefox_profile.set_preference( "permissions.default.image", 2 )

options = Options()
options.set_headless(headless=False)
def renew_connection():
    with Controller.from_port(port = 9051) as controller:
        controller.authenticate(password="password")
        controller.signal(Signal.NEWNYM)
renew_connection()
driver = webdriver.Firefox(firefox_profile=firefox_profile,firefox_options=options)

print(driver)

driver.get("http://icanhazip.com/")
driver.save_screenshot("screenshot.png")
#192.42.116.18 