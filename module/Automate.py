import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import date

def WaitTillElementFound(element):
    try:
        return WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, element))
        )
    except :
        driver.quit()

driver = webdriver.Chrome(driverPath)  # Optional argument, if not specified will search path.
driver.get('http://3.7.23.170/');

usernameField = WaitTillElementFound("/html[1]/body[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[1]/input[1]")
usernameField.send_keys(username)
passwordField = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[2]/input[1]")
passwordField.send_keys(password)
SubmitButton = driver.find_element_by_xpath("/html[1]/body[1]/div[4]/div[1]/div[1]/form[1]/div[2]/div[3]/input[1]")
SubmitButton.click() 

timeButton = WaitTillElementFound("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/ul[1]/li[6]/a[1]/b[1]")
timeButton.click()
enterTimeButton = WaitTillElementFound("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[4]/div[1]/ul[1]/li[2]/a[1]/p[1]")
enterTimeButton.click()

day = date.today().weekday()
index = "";
if(day == 6):
    dayIndex = 2;
else:
    dayIndex = day + 3
index = dayIndex
timeBoxHour = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/table[1]/tbody[3]/tr[1]/td["+str(index) +"]/input[1]")
timeBoxHour.click()
timeSplitted = timevalue.split(':')
timeBoxHour.send_keys(timeSplitted[0])
timeBoxHour.send_keys(Keys.TAB)
timeBoxHour.send_keys(timeSplitted[1])
submitButton = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[4]/div[5]/div[1]/div[1]/table[1]/tbody[4]/tr[3]/td[2]/div[1]/input[1]")
submitButton.click()
profileButton = driver.find_element_by_xpath("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[1]/span[1]")
profileButton.click()
logoutButton = WaitTillElementFound("/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/a[3]")
logoutButton.click()

time.sleep(2)
driver.quit()