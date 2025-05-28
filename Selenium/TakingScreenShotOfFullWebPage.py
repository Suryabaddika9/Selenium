from ctypes import windll

from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")


driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

width = 1920

height = driver.execute_script("return Math.max(document.body.scrollHeight,document.documentElement.scrollHeight,document.body.offsetHeight,document.documentElement.offsetHeight,document.documentElement.clientHeight);")

driver.set_window_size(width, height)
page_body = driver.find_element(By.TAG_NAME,"body")

page_body.screenshot("Full_Body_Screen_Shot.png")
driver.quit()
