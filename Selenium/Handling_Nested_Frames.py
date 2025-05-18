import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://letcode.in/frame")
time.sleep(3)
driver.switch_to_frame("firstFr")
driver.find_element(By.NAME,"fname").send_keys("surya")
driver.find_element(By.NAME,"lname").send_keys("Baddika")
time.sleep(3)

inner_frame=driver.find_element(By.XPATH,"//iframe[@src='innerframe']")
driver.switch_to_frame(inner_frame)
driver.find_element(By.NAME,"email").send_keys("surya@gmail.com")
time.sleep(3)

driver.quit()


