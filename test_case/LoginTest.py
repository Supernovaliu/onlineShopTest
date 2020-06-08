import time

from selenium import webdriver

driver = webdriver.Chrome(r'D:\tools\SeleniumStudy\chromedriver.exe')
driver.get("localhost/admin")
driver.maximize_window()