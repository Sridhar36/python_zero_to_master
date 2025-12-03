from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Chrome()

driver.get("https://www.google.com/")

username = driver.find_element('email')
password = driver.find_element('pass')

username.send_keys("user1")
password.send_keys("pass1")

