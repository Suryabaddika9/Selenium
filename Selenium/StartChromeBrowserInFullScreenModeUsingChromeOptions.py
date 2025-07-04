import time

from selenium import webdriver

chrome_options=webdriver.ChromeOptions()
chrome_options.add_argument("--kiosk")


driver=webdriver.Chrome(options=chrome_options)

driver.get("https://omayo.blogspot.com/")

time.sleep(4)