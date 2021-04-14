import time
import os
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup

#os.remove(r'\Users\mclark\Downloads\contact_export_1135561764861_032421_113128.csv')

# load your driver
driver = webdriver.Chrome(r'\Users\mclark\Desktop\python\scraping\chromedriver')

# get the web page
driver.get('https://login.constantcontact.com/login/login.sdo?goto=https%3A%2F%2Fgo.constantcontact.com%2Fprocessing_login.jsp&partner_name=ROVING');

#login credentials
username = driver.find_element_by_id("luser")
username.clear()
username.send_keys("acpa@acpafl.org")

password = driver.find_element_by_id("lpass")
password.clear()
password.send_keys("Jerin012080-")
#!Attention! Displaying this code publicly will reveal user & password. Use your own discretion with this script.

# click the login button
driver.find_element_by_id('login-button').click()

time.sleep(7)

#click contacts
driver.find_element_by_id('site-nav-item-contacts').click()

time.sleep(10)

#click Got It!
gotIt = driver.find_elements_by_class_name('btn-text')
#print(gotIt)
#print(len(gotIt))
gotIt[20].click()

#click General contact
#genContact = driver.find_elements_by_class_name('table-data-text-wrap')
#print(genContact)
#print(len(genContact))
#genContact[3].click()

#click 3rd checkbox
checkbox3 = driver.find_elements_by_class_name('simulated-input')
checkbox3[2].click()

time.sleep(3)

#click Actions
actions = driver.find_elements_by_class_name('btn-text')
actions[19].click()

time.sleep(3)

#click Export
truncate = driver.find_elements_by_class_name('truncate')
truncate[3].click()

#click custom fields
fields = driver.find_elements_by_class_name('simulated-input')
fields[21].click()

#click subExport
subExport = driver.find_elements_by_class_name('btn-text')
subExport[22].click()

time.sleep(3)

#Download CSV
download = driver.find_elements_by_class_name('btn-text')
download[19].click()

time.sleep(5)


#driver.quit()
