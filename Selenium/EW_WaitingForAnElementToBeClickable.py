import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.XPATH,"//button[text()='Check this']").click()

wait = WebDriverWait(driver,15)
check_box_field = wait.until(expected_conditions.element_to_be_clickable((By.ID,"dte")))
check_box_field.click()

time.sleep(5)
driver.quit()
