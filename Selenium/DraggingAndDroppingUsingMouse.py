import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")

oslo = driver.find_element(By.ID,"box1")
norway = driver.find_element(By.ID,"box101")

actions = ActionChains(driver)
actions.drag_and_drop(oslo,norway).perform()

time.sleep(4)
driver.quit()