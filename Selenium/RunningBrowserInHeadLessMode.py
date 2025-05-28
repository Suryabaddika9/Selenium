from selenium import webdriver


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--headless")

driver=webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")
