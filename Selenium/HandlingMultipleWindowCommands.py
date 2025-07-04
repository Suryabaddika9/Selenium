import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

page_one_title = driver.title
print(page_one_title)
driver.find_element(By.ID,"link1").click()
time.sleep(4)

driver.switch_to.new_window("window")

driver.get("https://www.facebook.com/")
page_two_title=driver.title
print(page_two_title)
time.sleep(4)
driver.quit()