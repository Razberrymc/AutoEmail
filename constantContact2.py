import time
import glob
import os
import shutil
from selenium import webdriver
from random import randint
from bs4 import BeautifulSoup

#os.remove(r'\Users\mclark\Downloads\contact_export_1135561764861_032421_113128.csv')

# load your driver
driver = webdriver.Chrome(r'\Users\mclark\Desktop\python\scraping\chromedriver')

# get the web page
driver.get('https://login.constantcontact.com/login/login.sdo?goto=https%3A%2F%2Fgo.constantcontact.com%2Fprocessing_login.jsp&partner_name=ROVING');

cred = open("launchCodes2.txt", "r")
credList = cred.readlines()
user_enter = (credList[0]).rstrip('\n')
pass_enter = (credList[1]).rstrip('\n')

#login credentials
try:
    username = driver.find_element_by_id("luser")
    username.clear()
    username.send_keys(user_enter)
except:
    print("Tried to input username, but an error occurred")
    driver.quit()
    exit()

try:
    password = driver.find_element_by_id("lpass")
    password.clear()
    password.send_keys(pass_enter)
    #!Attention! Displaying this code publicly will reveal user & password. Use your own discretion with this script.
except:
    print("Tried to input password, but an error occurred")
    driver.quit()
    exit()

# click the login button
try:
    driver.find_element_by_id('login-button').click()
except:
    print("Tried to click the login button, but an error occurred")
    driver.quit()
    exit()

time.sleep(7)

#click contacts
try:
    driver.find_element_by_id('site-nav-item-contacts').click()
except:
    print("Tried to click contacts, but an error occurred")
    driver.quit()
    exit()

time.sleep(7)

#click Got It!
try:
    driver.find_element_by_xpath("//span[contains(text(),'Got')]").click()
except:
    pass

#gotIt = driver.find_elements_by_class_name('btn-text')
#print(gotIt)
#print(len(gotIt))
#gotIt[20].click()

#click General contact
#genContact = driver.find_elements_by_class_name('table-data-text-wrap')
#print(genContact)
#print(len(genContact))
#genContact[3].click()

#click General Contact
try:
    driver.find_element_by_xpath("//td[contains(text(),'General Cont')]").click()
except:
    print("Tried to click general contact, but an error occurred")
    driver.quit()
    exit()
#checkbox3 = driver.find_elements_by_class_name('simulated-input')
#checkbox3[2].click()

time.sleep(3)

#click overflow menu
try:
    driver.find_element_by_xpath("//button[@data-qe-id='button-contactsTable-headerOverflowMenu']").click()
except:
    print("Tried to click overflow menu, but an error occurred")
    driver.quit()
    exit()
#actions = driver.find_elements_by_class_name('btn-text')
#actions[19].click()

time.sleep(3)

#click Export
try:
    driver.find_element_by_xpath("//button[@data-qe-id='button-contactsTable-headerOverflowMenu_Menu--item_export_list']").click()
except:
    print("Tried to click export, but an error occurred")
    driver.quit()
    exit()
#truncate = driver.find_elements_by_class_name('truncate')
#truncate[3].click()

time.sleep(3)

#click custom fields
try:
    driver.find_element_by_xpath("//label[@data-qe-id='check-box-custom_fields-label']").click()
    #fields = driver.find_elements_by_class_name('simulated-input')
    #fields[21].click()
except:
    print("Tried to click custom fields, but an error occurred")
    driver.quit()
    exit()

#click date created
try:
    driver.find_element_by_xpath("//label[@data-qe-id='check-box-created_at-label']").click()
except:
    print("Tried to click date created, but an error occurred")
    driver.quit()
    exit()

#click date updated
try:
    driver.find_element_by_xpath("//label[@data-qe-id='check-box-updated_at-label']").click()
except:
    print("Tried to click date updated, but an error occurred")
    driver.quit()
    exit()

time.sleep(3)

#click subExport
try:
    driver.find_element_by_xpath("//button[@data-qe-id='export-contacts-export-button']").click()
    #driver.find_element_by_xpath("//span[contains(text(),'Expor')]").click()
    #subExport = driver.find_elements_by_class_name('btn-text')
    #subExport[22].click()
except:
    print("Tried to click export, but an error occurred")
    driver.quit()
    exit()

time.sleep(3)

#Download CSV
try:
    driver.find_element_by_xpath("//a[contains(text(),'Download')]").click()
    #download = driver.find_elements_by_class_name('btn-text')
    #download[19].click()
except:
    print("Tried to click Download CSV but an error occurred")
    driver.quit()
    exit()

time.sleep(5)


driver.quit()

list_of_files = glob.glob(r'C:\Users\mclark\Downloads\*') # * means all if need specific format then *.csv
latest_file = max(list_of_files, key=os.path.getctime)
print(latest_file)
print(latest_file[25:])
shutil.copy(latest_file, r'C:\Users\mclark\Desktop\emailProduction')
shutil.move(latest_file, r'C:\Users\mclark\Desktop\emailHistory' + latest_file[25:])

emailHist = (os.listdir(r'C:\Users\mclark\Desktop\emailHistory'))
emailProd = (os.listdir(r'C:\Users\mclark\Desktop\emailProduction'))

full_path = ["C:/Users/mclark/Desktop/emailHistory/{0}".format(x) for x in emailHist]
full_path2 = ["C:/Users/mclark/Desktop/emailProduction/{0}".format(x) for x in emailProd]

if len(emailHist) == 8:
    oldest_file = min(full_path, key=os.path.getctime)
    os.remove(oldest_file)

if len(emailProd) == 2:
    oldest_file2 = min(full_path2, key=os.path.getctime)
    os.remove(oldest_file2)

print(len(emailHist))
print(len(emailProd))
