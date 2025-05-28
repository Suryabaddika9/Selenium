import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

button_Save = driver.find_element(By.XPATH,"//input[@type='submit']")

button_Save.screenshot("Button.png")