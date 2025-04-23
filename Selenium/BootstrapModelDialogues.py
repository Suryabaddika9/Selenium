import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://practice-automation.com/modals/")

driver.find_element(By.ID,"simpleModal").click()

time.sleep(4)

Heading_Text=driver.find_element(By.XPATH,"//div[@id='pum_popup_title_1318']").text
print(Heading_Text)

Info_Text=driver.find_element(By.XPATH,"//p[contains(text(),'Hi, I’m a simple modal.')]").text
print(Info_Text)