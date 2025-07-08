from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

wait = WebDriverWait(driver,10)
h_button = wait.until(expected_conditions.presence_of_element_located((By.ID,"hbutton")))

h_button_text = h_button.get_attribute("value")
print(h_button_text)

