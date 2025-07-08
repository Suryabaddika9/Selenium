import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

for i in range(1,6):
    Xpath_text = "(//div[@id='LinkList1']//a)["+str(i)+"]"
    driver.find_element(By.XPATH,Xpath_text).click()
    time.sleep(3)
    driver.back()
time.sleep(4)
driver.quit()