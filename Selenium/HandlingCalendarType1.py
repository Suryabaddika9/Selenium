import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from Selenium.HandlingHyperlinks import xpath_text

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")
driver.find_element(By.ID,"datepicker").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))


def select_date_in_calendar(month,year,day):
    current_month = driver.find_element(By.CLASS_NAME,"ui-datepicker-month").text
    current_year = driver.find_element(By.CLASS_NAME,"ui-datepicker-year").text

    while not (current_month.__eq__(month) and current_year.__eq__(year)):
        driver.find_element(By.XPATH,"//span[text()='Next']")
        current_month = driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        current_year = driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

    xpath_text ="//td[@data-handler='selectDay']/a[text()='"+day+"']"
    driver.find_element(By.XPATH,xpath_text).click()

select_date_in_calendar("03","2026","21")

time.sleep(4)
driver.quit()
