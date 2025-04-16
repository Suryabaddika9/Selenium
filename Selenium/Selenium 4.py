from selenium import webdriver

import time

from selenium.webdriver.common.by import By

driver=webdriver.Firefox()
driver.get("https://omayo.blogspot.com/")
time.sleep(2)
a=driver.find_element(By.ID,"ta1").get_attribute("rows")
print(a)

q=driver.find_element(By.ID,"ta1").is_displayed()
print(q)
driver.find_element(By.XPATH,"//div[@id='HTML5']//a[@id='link2']").click()
time.sleep(4)
driver.back()
time.sleep(4)
driver.forward()
time.sleep(5)


driver.quit()
