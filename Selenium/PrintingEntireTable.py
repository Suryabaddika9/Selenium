from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

rows = driver.find_elements(By.XPATH,"//table[@id='table1']//tr")
rows_count = len(rows)

columns = driver.find_elements(By.XPATH,"//table[@id='table1']//th")
columns_count = len(columns)

for r in range(1,rows_count+1):
    for c in range(1,columns_count+1):
        if r==1:
            data = driver.find_element(By.XPATH,"//table[@id='table1']//th["+str(c)+"]")
            print(data.text,end=' ')
        else:
            data = driver.find_element(By.XPATH,"//table[@id='table1']//tr["+str(r-1)+"]/td["+str(c)+"]")
            print(data.text,end=' ')
    print()  #This will print each iteration in new line. So each row will print in a new line

