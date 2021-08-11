from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import getpass


def gotomeet(usersname, passwrd, meetcode, browser_name):
    ####        BROWSER DRIVER SELECTION        ####
    if(browser_name=="firefox"):
        from webdriver_manager.firefox import GeckoDriverManager
        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif(browser_name=="chrome"):
        from webdriver_manager.chrome import ChromeDriverManager
        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif(browser_name=="chromium"):
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.utils import ChromeType
        driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())
    elif(browser_name=="ie"):
        from webdriver_manager.microsoft import IEDriverManager
        driver = webdriver.Ie(IEDriverManager().install())
    elif(browser_name=="edge"):
        from webdriver_manager.microsoft import EdgeChromiumDriverManager
        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif(browser_name=="opera"):
        from webdriver_manager.opera import OperaDriverManager
        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        print("ENTERED BROWSER NOT SUPPORTED!!!")
        return
    ####        END OF BROWSER DRIVER SELECTION        ####

    #to get a website
    driver.get("https://meet.google.com/")
    driver.maximize_window()
    time.sleep(4)
    driver.find_element_by_class_name("cta-wrapper").click()
    #driver.find_element_by_xpath("//a[normalize-space()='Sign in']").click()
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
    mute=WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CLASS_NAME, "ZB88ed")))
    mute.click()
    #driver.find_element_by_class_name("ZB88ed").click()
    time.sleep(2)
    driver.find_element_by_xpath("//div[@class='IYwVEf HotEze nAZzG']//div[@class='oTVIqe BcUQQ']//*[local-name()='svg']").click()
    time.sleep(2)
    driver.find_element_by_css_selector('div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
    if(browser_name=="chrome"):
        while(True):
            pass

print("##### WELCOME TO MEET AUTOMISER #####")

browser_name=input("Enter the name of the browser in which you want to open Gmeet:").lower()


usersname=input("Enter the username of your Gmail:")
passwrd=getpass.getpass(prompt="Enter the password of your Gmail:")
meetcode=input("Enter the meet code:")
gotomeet(usersname, passwrd, meetcode,browser_name)