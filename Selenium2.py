from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
time.sleep(2)

Element1=driver.find_element(By.ID,"textbox1")
Element1.clear()
time.sleep(2)
Element1.send_keys("Surya")
Element1.clear()
time.sleep(2)
Element1.send_keys("Selenium Python")
Element1.clear()