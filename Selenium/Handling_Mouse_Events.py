import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

blog = driver.find_element(By.ID,"blogsmenu")

actions = ActionChains(driver)
actions.move_to_element(blog).perform()

time.sleep(3)
driver.quit()
