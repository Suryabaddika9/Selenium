
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://tutorialsninja.com/demo/index.php?route=common/home")

driver.find_element(By.XPATH,"//span[text()='My Account']").click()
driver.find_element(By.LINK_TEXT,"Login").click()
driver.find_element(By.ID,"input-email").send_keys("surya1234@gmail.com")
driver.find_element(By.ID,"input-password").send_keys("123456789")
driver.find_element(By.XPATH,"//input[@value='Login']").click()
if driver.find_element(By.LINK_TEXT,"Edit your account information"):
    print("Account Logged in")
else:
    print("Not Logged in")

time.sleep(5)

driver.quit()



