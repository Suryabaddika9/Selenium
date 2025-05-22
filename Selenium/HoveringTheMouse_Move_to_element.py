import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

sel_143 = driver.find_element(By.XPATH,"//a/span[text()='Selenium143']")
blog = driver.find_element(By.ID,"blogsmenu")

actions = ActionChains(driver)
actions.move_to_element(blog).perform()
actions.move_to_element(sel_143).perform()

time.sleep(4)
driver.quit()