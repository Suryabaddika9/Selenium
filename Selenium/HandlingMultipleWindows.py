import time


from selenium import webdriver
from selenium.webdriver.common.by import By

#from Selenium.StartChromeBrowserinMaxModeUsingChromeOptions import chrome_options

#chrome_options=webdriver.ChromeOptions()
#chrome_options.add_argument("--start-maximized")

driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")


parent_window_id = driver.current_window_handle


driver.find_element(By.LINK_TEXT,"Open a popup window").click()

windows=driver.window_handles

for w in windows:
    driver.switch_to.window(w)
    print(w)
    if driver.title.__eq__("New Window"):
        para_one_text=driver.find_element(By.LINK_TEXT,"New Window").text
        print(para_one_text)
        driver.close()
        break

driver.switch_to.window(parent_window_id)
driver.find_element(By.ID,"ta1").send_keys("Surya Baddika")
time.sleep(5)
driver.close()