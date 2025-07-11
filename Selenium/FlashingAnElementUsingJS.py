import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

def flash_element(element):
    for i in range(1,10):
        driver.execute_script("arguments[0].style.background='green'",element)
        time.sleep(0.1)
        driver.execute_script("arguments[0].style.background='yellow'", element)
        time.sleep(0.1)

button = driver.find_element(By.XPATH,"//h2/span")

flash_element(button)

time.sleep(5)
driver.quit()