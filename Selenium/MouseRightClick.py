import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/")

search = driver.find_element(By.XPATH,"//input[@name='search']")

actions = ActionChains(driver)
actions.context_click(search).perform()

time.sleep(3)
driver.quit()