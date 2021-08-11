from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.keys import Keys
import time


def gotomeet(usersname, passwrd, meetcode):
    driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    #to get a website
    driver.get("https://meet.google.com/")
    driver.maximize_window()
    driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
    username=driver.find_element_by_xpath("//input[@id='identifierId']")
    username.send_keys(usersname)
    driver.find_element_by_xpath("//span[normalize-space()='Next']").click()
    time.sleep(4)
    #driver.implicitly_wait(10)
    password=driver.find_element_by_name("password")
    #password=driver.find_element_by_css_selector("input[type=password]")
    password.send_keys(passwrd)
    password.send_keys(Keys.ENTER)
    time.sleep(7)
    elem = driver.find_element_by_xpath("//input[@id='i3'] ")
    elem.send_keys(meetcode)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    driver.find_element_by_class_name("ZB88ed").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='IYwVEf HotEze nAZzG']//div[@class='oTVIqe BcUQQ']//*[local-name()='svg']").click()
    time.sleep(2)
    driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()

print("##### WELCOME TO MEET AUTOMISER #####")
usersname=input("Enter the username of your Gmail:")
passwrd=input("Enter the password of your Gmail:")
meetcode=input("Enter the meet code")
gotomeet(usersname, passwrd, meetcode)