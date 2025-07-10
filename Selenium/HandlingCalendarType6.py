import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

driver.find_element(By.CLASS_NAME,"ui-datepicker-trigger").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.ID,"ui-datepicker-div")))

driver.find_element(By.CSS_SELECTOR,"td.ui-datepicker-today a").click()
time.sleep(6)
driver.quit()
