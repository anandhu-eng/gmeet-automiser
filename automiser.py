from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager

driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())


#to get a website
driver.get("https://www.google.co.in")
driver.maximize_window()