import time

from selenium import webdriver


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

driver.save_screenshot("Register_page.png")