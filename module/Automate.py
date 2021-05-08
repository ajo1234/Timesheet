import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

driver = webdriver.Chrome(driverPath)

def WaitTillElementFound(element):
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element))
        )
    except :
        driver.quit()

def ScrollDown(isDown):
    body = driver.find_element_by_css_selector('body')
    body.send_keys(Keys.PAGE_DOWN) if isDown else body.send_keys(Keys.PAGE_DOWN)
    time.sleep(1)

def LoadWebsite():
    driver.get('http://3.7.23.170/');

def Login():
    usernameField = WaitTillElementFound("/html[1]/body[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
    usernameField.send_keys(username)
    passwordField = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]")
    passwordField.send_keys(password)
    SubmitButton = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[3]/input[1]")
    SubmitButton.click() 

def NavigateToLogTime():
    timeButton = WaitTillElementFound("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[6]/a[1]/b[1]")
    timeButton.click()
    enterTimeButton = WaitTillElementFound("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[4]/div[1]/ul[1]/li[2]/a[1]/p[1]")
    enterTimeButton.click()

def FindNumberOfProjects():
    header = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/table[1]/tbody[3]")
    numberOfProjects = header.find_elements_by_tag_name("tr")
    return str(len(numberOfProjects))

# Monday is td[3] and sunday is td[2]
def EnterTime():
    day = date.today().weekday()
    if(day == 6):
        dayIndex = 2;
    else:
        dayIndex = day + 3
    row = 1
    while(row <= len(timeList)):
        if(row % 4 == 0):
            ScrollDown(True)
        try:
            timeBoxHour = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/table[1]/tbody[3]/tr["+str(row)+"]/td["+str(dayIndex) +"]/input[1]")
            timeBoxHour.click()
            timeSplitted = timeList[row-1].split(':')
            timeBoxHour.send_keys(timeSplitted[0])
            timeBoxHour.send_keys(Keys.TAB)
            timeBoxHour.send_keys(timeSplitted[1])
        except Exception as e:
            print("Exception happend:" + str(e))
        row+=1

def LogOut():
    ScrollDown(True)
    submitButton = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/table[1]/tbody[4]/tr[3]/td[2]/div[1]/input[1]")
    submitButton.click()
    ScrollDown(False)
    profileButton = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")
    profileButton.click()
    logoutButton = WaitTillElementFound("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]")
    logoutButton.click()

def QuitDriver(): 
    time.sleep(5)
    driver.quit()

LoadWebsite()
Login()
NavigateToLogTime()
EnterTime()
LogOut()
QuitDriver()



