import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://jqueryui.com/resizable/")

frame_one = driver.find_element(By.CLASS_NAME,"demo-frame")

driver.switch_to.frame(frame_one)

actions = ActionChains(driver)
dd = driver.find_element(By.CSS_SELECTOR,"div.ui-icon ui-icon-gripsmall-diagonal-se")
time.sleep(3)
actions.drag_and_drop_by_offset(dd,35,80).perform()
time.sleep(4)
driver.quit()

