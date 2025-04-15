from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://omayo.blogspot.com/")

#x=driver.find_element(By.XPATH,"//h2[@class='title']").txt
#print(x)

driver.quit()

