import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://the-internet.herokuapp.com/iframe")
time.sleep(3)

driver.switch_to_frame("mce_0_ifr")
driver.find_element(By.XPATH,'//body[@id="tinymce"]/p').clear()

time.sleep(3)
driver.quit()