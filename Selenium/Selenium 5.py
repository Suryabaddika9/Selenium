import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

#from selenium.webdriver.chrome import options

#chrome_options = options()
#
chrome_options=Options()
chrome_options.add_argument("--disable-notifications")
driver=webdriver.Chrome(options=chrome_options)
driver.get("https://www.homedepot.com/")

time.sleep(15)
