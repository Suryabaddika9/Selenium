import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

sel_143=driver.find_element(By.ID,"link1")

actions=ActionChains(driver)
actions.click(sel_143).perform()

time.sleep(4)
driver.quit()