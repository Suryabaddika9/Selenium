import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.implicitly_wait(10)

driver.find_element(By.CLASS_NAME,"dropbtn").click()
driver.find_element(By.LINK_TEXT,"Flipkart").click()
driver.back()

time.sleep(5)
driver.quit()
