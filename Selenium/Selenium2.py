
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://tutorialsninja.com/demo/")

#Retrieving Text between HTML tags
element_text=driver.find_element(By.XPATH,"//h5[normalize-space()='Information']").text
print(element_text)

#retrieving the title of the current web page

title=driver.title
print(title)
time.sleep(2)

driver.quit()
