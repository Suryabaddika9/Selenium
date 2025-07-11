import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

#driver.execute_script("document.getElementById('alert1').click()")

button = driver.find_element(By.ID,"alert1")

driver.execute_script("arguments[0].click()",button)

time.sleep(5)