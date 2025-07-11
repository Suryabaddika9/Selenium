import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.opencart.com/TlbeVW/index.php?route=sale/order&user_token=b40240f9a1f1b59e32590fead82c08d6")

time.sleep(30)