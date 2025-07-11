import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

def highlight_element(element):
    driver.execute_script("arguments[0].style.border='3px solid yellow'",element)


button = driver.find_element(By.XPATH,"//h2/span")

highlight_element(button)

time.sleep(5)
driver.quit()