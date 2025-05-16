import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

for i in range(1,6):
    xpath_text="(//div[@id='LinkList1']//a)["+str(i)+"]"
    links=driver.find_element(By.XPATH,xpath_text)
    links.click()
    driver.back()
time.sleep(5)