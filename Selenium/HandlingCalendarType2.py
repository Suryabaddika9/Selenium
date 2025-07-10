import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.path2usa.com/travel-companion/")

time.sleep(6)

driver.find_element(By.ID,"form-field-travel_comp_date").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,"div.flatpickr-calendar")))

current_month = driver.find_element(By.CLASS_NAME,"cur-month").text.strip()
print(current_month)

while not(current_month.__eq__("October")):
    driver.find_element(By.CLASS_NAME,"flatpickr-next-month").click()
    current_month = driver.find_element(By.CLASS_NAME, "cur-month").text.strip()

time.sleep(3)

driver.find_element(By.XPATH,"//div[@class='dayContainer']/span[text()=25]").click()

time.sleep(5)

driver.quit()