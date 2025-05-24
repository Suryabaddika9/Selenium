import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

double_click = driver.find_element(By.ID,"testdoubleclick")

actions = ActionChains(driver)
actions.double_click(double_click).perform()

time.sleep(4)
driver.quit()