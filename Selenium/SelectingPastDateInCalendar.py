import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.find_element(By.ID,"datepicker").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

current_month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
current_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text

while not(current_month.__eq__("July") and current_year.__eq__("2024")):
    driver.find_element(By.XPATH,"//span[text()='Prev']").click()
    current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

driver.find_element(By.XPATH,"//a[@class='ui-state-default'][text()=6]").click()

time.sleep(5)
driver.quit()