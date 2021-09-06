####                IMPORT SECTION              ####
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
import getpass
from plyer import notification
from datetime import datetime

####                END OF THE SECTION           ####


def gotomeet(usersname, passwrd, meetcode, browser_name):
    ####        BROWSER DRIVER SELECTION        ####
    if browser_name == "firefox":
        from webdriver_manager.firefox import GeckoDriverManager

        driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
    elif browser_name == "chrome":
        from webdriver_manager.chrome import ChromeDriverManager

        driver = webdriver.Chrome(ChromeDriverManager().install())
    elif browser_name == "chromium":
        from webdriver_manager.chrome import ChromeDriverManager
        from webdriver_manager.utils import ChromeType

        driver = webdriver.Chrome(
            ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install()
        )
    elif browser_name == "ie":
        from webdriver_manager.microsoft import IEDriverManager

        driver = webdriver.Ie(IEDriverManager().install())
    elif browser_name == "edge":
        from webdriver_manager.microsoft import EdgeChromiumDriverManager

        driver = webdriver.Edge(EdgeChromiumDriverManager().install())
    elif browser_name == "opera":
        from webdriver_manager.opera import OperaDriverManager

        driver = webdriver.Opera(executable_path=OperaDriverManager().install())
    else:
        print("ENTERED BROWSER NOT SUPPORTED!!!")
        return
    ####        END OF BROWSER DRIVER SELECTION        ####

    # to get a website
    driver.get("https://meet.google.com/")
    driver.maximize_window()
    time.sleep(4)
    driver.find_element_by_class_name("cta-wrapper").click()
    username = driver.find_element_by_xpath("//input[@id='identifierId']")
    username.send_keys(usersname)
    driver.find_element_by_xpath("//span[normalize-space()='Next']").click()
    time.sleep(4)
    password = driver.find_element_by_name("password")
    password.send_keys(passwrd)
    password.send_keys(Keys.ENTER)
    time.sleep(7)
    elem = driver.find_element_by_xpath("//input[@id='i3'] ")
    elem.send_keys(meetcode)
    elem.send_keys(Keys.RETURN)
    time.sleep(5)
    mute = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "ZB88ed"))
    )
    mute.click()
    time.sleep(2)
    driver.find_element_by_xpath(
        "//div[@class='IYwVEf HotEze nAZzG']//div[@class='oTVIqe BcUQQ']//*[local-name()='svg']"
    ).click()
    time.sleep(2)
    driver.find_element_by_css_selector("div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt").click()
    time.sleep(5)
    while True:
        try:
            driver.find_element_by_class_name("uGOf1d")
            break
        except:
            pass

    participants_beg = int(
        driver.find_element_by_class_name("uGOf1d").get_attribute("textContent")
    )
    participants_end = 0
    while True:
        time.sleep(10)
        try:
            participants_end = int(
                driver.find_element_by_class_name("uGOf1d").get_attribute("textContent")
            )
            print(participants_end)
        except:
            notification.notify(
                title="Gmeet automiser",
                message="Error! Might be due to gmeet ending without consent of program!",
                timeout=10,
            )
            return
        if participants_beg - participants_end > 7:
            driver.find_element_by_xpath("//button[@aria-label='Leave call']").click()
            title = "GMeet Automiser"
            message = "Meet ended!! closing the window in 10 seconds"
            notification.notify(title=title, message=message, timeout=10)
            time.sleep(10)
            driver.close()
            return

        else:
            participants_beg = participants_end
    # print(participants)
    if browser_name == "chrome":
        while True:
            pass


print("##### WELCOME TO MEET AUTOMISER #####")
period_code = []
start_time = []

browser_name = input(
    "Enter the name of the browser in which you want to open Gmeet:"
).lower()
usersname = input("Enter the username of your Gmail:")
passwrd = getpass.getpass(prompt="Enter the password of your Gmail:")

####        SECTION FOR ENTERING THE PERIOD DETAILS         ####
number_of_periods = int(input("Enter the number of period you have today:"))
for i in range(number_of_periods):
    period = input(
        ("Enter the meetcode for {period_number} period:").format(period_number=i + 1)
    )
    inp_time = input("Enter the time of the meet in hour:")
    inp_time_min = input("Enter the time of meet in minutes:")
    period_code.append(period)
    start_time.append(inp_time)
    start_time.append(inp_time_min)
####                    SECTION END                         ####

####        SECTION FOR LOGGING INTO PERIODS                ####
while len(period_code) != 0:
    time_now = datetime.now().strftime("%H:%M")
    lcltime = "{h}:{m}".format(h=start_time[0], m=start_time[1])

    if time_now == lcltime:
        gotomeet(usersname, passwrd, period_code[0], browser_name)
        period_code.remove(period_code[0])
        start_time.remove(start_time[0])
        start_time.remove(start_time[0])
    else:
        time.sleep(20)
####                END OF THE SECTION                      ####

####                PROGRAM END MESSAGE                     ####
title = "GMeet automiser"
message = "All the sheduled classes are over!! Take rest now"
notification.notify(title=title, message=message, timeout=10)
####                END OF THE SECTION                      ####
