from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

Section = driver.find_element(By.ID,"LinkList1")

Section.screenshot("Compendium.png")

