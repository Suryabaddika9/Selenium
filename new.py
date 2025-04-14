from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
#driver.find_element(By.ID,"ta1").send_keys("Hi Surya what are you doing Now...???")
#driver.find_element(By.NAME,"q").send_keys("B.Surya")
#driver.find_element(By.CLASS_NAME,"combobox").click()
driver.find_element(By.LINK_TEXT,"testwisely").click()
#driver.find_element(By.CSS_SELECTOR,"#prompt").click()
#driver.find_element(By.XPATH,"//input[@value='Login']").click()


time.sleep(5)
driver.quit()