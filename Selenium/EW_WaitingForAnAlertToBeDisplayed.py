import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.ID,"alert1").click()

wait = WebDriverWait(driver,15)
wait.until(expected_conditions.alert_is_present())

alert = driver.switch_to.alert
alert_text = alert.text
print(alert_text)

time.sleep(3)

alert.accept()

time.sleep(3)

driver.quit()