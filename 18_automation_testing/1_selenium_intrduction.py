'''
One of the best tools for browser automation is Selenium.

to install: pip install selenium.

Selenium requires driver inorder to run the automation instance. We can install executable files. When we run it, it runs
some binary code.

https://www.seleniumeasy.com/
'''

# webdriver allows us to drive the automation through web driver

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# service = Service(executable_path="C:\\Automation\\chromedriver_win32\\chromedriver.exe")
# # to create an instance of the browser
# chrome_browser = webdriver.Chrome(service=service)  # this is the chrome class given by webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome("C:\\Automation\\chromedriver_win32\\chromedriver.exe")
driver.get("https://www.seleniumeasy.com/")
driver.maximize_window()
print(driver.title)
driver.find_element(By.LINK_TEXT,"TestNG").get_attribute('class')
print(driver.find_element(By.LINK_TEXT,"TestNG").click())
driver.find_element(By.LINK_TEXT,"TestNG Report").click()
