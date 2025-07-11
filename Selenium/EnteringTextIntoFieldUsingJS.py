import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

text_field = driver.find_element(By.ID,"ta1")

driver.execute_script("arguments[0].value='Hi Surya'",text_field)

time.sleep(5)
driver.quit()