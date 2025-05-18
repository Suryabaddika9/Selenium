import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/nested_frames")
time.sleep(3)

driver.switch_to.frame("frame-top")
driver.switch_to.frame("frame-left")
left_text = driver.find_element(By.XPATH,"//body").text
print(left_text)

driver.switch_to.parent_frame()
driver.switch_to.frame("frame-middle")
middle_text=driver.find_element(By.ID,"content").text
print(middle_text)

driver.switch_to.parent_frame()
driver.switch_to.frame("frame-right")
right_text=driver.find_element(By.XPATH,"//body").text
print(right_text)


