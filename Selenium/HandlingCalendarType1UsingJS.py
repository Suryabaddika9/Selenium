import time

import document
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")


driver.execute_script("document.getElementById('datepicker').value='25/11/2026'")

time.sleep(5)

driver.quit()