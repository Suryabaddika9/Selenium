import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.globalsqa.com/demo-site/sliders/#Range")

time.sleep(3)

min_label=driver.find_element(By.XPATH,"//span[@style='left: 42.7451%;']")

time.sleep(3)

actions = ActionChains(driver)
actions.drag_and_drop_by_offset(min_label,-20,0).perform()

time.sleep(4)
driver.quit()