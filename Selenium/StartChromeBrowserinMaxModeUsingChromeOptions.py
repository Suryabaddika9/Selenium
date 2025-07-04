import time

from selenium import webdriver

from Selenium.RunningBrowserInHeadLessMode import chrome_options

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized")

driver=webdriver.Chrome(options=chrome_options)
driver.get("https://omayo.blogspot.com/")
time.sleep(4)



