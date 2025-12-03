from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

assert driver.title == "Google"

driver.quit()
