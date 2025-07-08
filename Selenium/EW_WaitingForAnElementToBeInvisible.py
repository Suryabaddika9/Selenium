from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")

driver.find_element(By.XPATH,"//button[text()='Start']").click()

wait = WebDriverWait(driver,18)
progress_section = wait.until(expected_conditions.invisibility_of_element_located((By.ID,"loading")))

heading_text = driver.find_element(By.XPATH,"//div[@id='finish']/h4").text

print(heading_text)
driver.quit()

