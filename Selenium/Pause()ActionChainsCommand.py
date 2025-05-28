import time

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common import keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=account/register")

driver.find_element(By.ID,"input-firstname").send_keys("Baddika")

actions = ActionChains(driver)

actions.send_keys(Keys.TAB).pause(3).send_keys("Surya").send_keys(Keys.TAB).pause(3).send_keys("surya@gmail.com").send_keys(Keys.TAB).pause(3).send_keys("123456").perform()

time.sleep(3)
driver.quit()