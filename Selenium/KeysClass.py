import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/login")

time.sleep(3)

driver.find_element(By.ID,"input-email").send_keys("surya1234@gmail.com")
time.sleep(3)

driver.find_element(By.ID,"input-password").send_keys("Surya690@")
time.sleep(3)

#driver.find_element(By.ID,"input-password").send_keys(Keys.ENTER)

actions = ActionChains(driver)
actions.send_keys(Keys.ENTER).perform()

time.sleep(3)
driver.quit()