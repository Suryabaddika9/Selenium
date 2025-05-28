import time

from attr.validators import deep_iterable
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")

button = driver.find_element(By.XPATH,"//span[text()='right click me']")

time.sleep(4)

actions = ActionChains(driver)
actions.context_click(button).perform()

quit_option = driver.find_element(By.XPATH,"//li/span[text()='Quit']")

time.sleep(3)

actions.click(quit_option).perform()

time.sleep(4)
driver.quit()