import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

driver.find_element(By.ID,"third_date_picker").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

month_dropdown_field = driver.find_element(By.CLASS_NAME,"ui-datepicker-month")
select_month = Select(month_dropdown_field)
select_month.select_by_visible_text("Nov")

year_dropdown_field = driver.find_element(By.CLASS_NAME,"ui-datepicker-year")
select_year = Select(year_dropdown_field)
select_year.select_by_visible_text("2027")

driver.find_element(By.XPATH,"//td[@data-handler='selectDay']/a[text()=20]").click()

time.sleep(6)
driver.quit()
