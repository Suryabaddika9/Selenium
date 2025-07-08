import time
from asyncio import timeout

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

driver.find_element(By.CLASS_NAME,"dropbtn").click()

wait = WebDriverWait(driver, timeout=30, poll_frequency=5,ignored_exceptions=[NoSuchElementException])
flipkart_option = wait.until(expected_conditions.visibility_of_element_located((By.LINK_TEXT,"Flipkart")))

flipkart_option.click()

time.sleep(4)
driver.quit()

