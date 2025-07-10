import time
from datetime import datetime

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

expected_date = "2070-09-26"

formatted_date = datetime.strptime(expected_date,"%Y-%m-%d")
expected_day = formatted_date.day
expected_month = formatted_date.month
expected_year = formatted_date.year

current_month_text = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
month_number = {"January":1, "February":2, "March":3, "April":4, "May":5, "June":6, "July":7, "August":8, "September":9,"October":10, "November":11, "December":12}
current_month_number = month_number[current_month_text]

current_year_text = driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text
current_year_number = int(current_year_text)

while current_year_number < expected_year or current_month_number < expected_month:
    driver.find_element(By.XPATH,"//span[text()='Next']").click()
    current_month_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    month_number = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                    "September": 9, "October": 10, "November": 11, "December": 12}
    current_month_number = month_number[current_month_text]

    current_year_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    current_year_number = int(current_year_text)

while current_year_number > expected_year or current_month_number > expected_month:
    driver.find_element(By.XPATH, "//span[text()='Prev']").click()
    current_month_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
    month_number = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6, "July": 7, "August": 8,
                    "September": 9, "October": 10, "November": 11, "December": 12}
    current_month_number = month_number[current_month_text]

    current_year_text = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
    current_year_number = int(current_year_text)

driver.find_element(By.XPATH,"//td[@data-handler='selectDay']/a[text()='"+str(expected_day)+"']").click()
time.sleep(5)
driver.quit()