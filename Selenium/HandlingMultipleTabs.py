import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

present_window_id=driver.current_window_handle
print(present_window_id)
time.sleep(3)

driver.find_element(By.ID,"selenium143").click()

windows = driver.window_handles

print(windows)

for w in windows:
    driver.switch_to.window(w)
    if driver.title.__eq__("Selenium143"):
        driver.find_element(By.LINK_TEXT,"What is Selenium?").click()
        time.sleep(6)
        driver.close()
        break

driver.switch_to.window(present_window_id)
driver.find_element(By.ID,"ta1").send_keys("Hi Mr. Surya")
time.sleep(5)
driver.quit()