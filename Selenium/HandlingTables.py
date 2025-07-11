from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

table_data = driver.find_element(By.XPATH,"//table[@id='table1']").text
print(table_data)

table_body = driver.find_element(By.XPATH,"//table[@id='table1']/tbody").text
print(table_body)

table_headings = driver.find_element(By.XPATH,"//table[@id='table1']//thead").text
print(table_headings)


table_data2 = driver.find_element(By.XPATH,"//table[@id='table1']/tbody/tr[3]/td[3]").text
print(table_data2)


table_headings2 = driver.find_elements(By.XPATH,"//table[@id='table1']//th")
for heading in table_headings2:
    print(heading.text)

