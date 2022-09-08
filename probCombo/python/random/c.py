# -------------------------------------
# Program Starts from here
# ------------------------------------- 
import os

#pip install selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
from datetime import date
import subprocess
import pyperclip #pip install pyperclip

# path of the directory
checkPath = "check"
validPath = "valid"

# creating the date object of today's date
todays_date = date.today()

EXTENSION_PATH = "C:\\Users\\niyankhadka\\AppData\\Local\\BraveSoftware\\Brave-Browser\\User Data\\Default\\Extensions\\nkbihfbeogaeaoehlefnkodbefgpgknn\\10.18.3_0.crx"
BINARY_LOCATION = "C:\\Program Files\\BraveSoftware\\Brave-Browser\\Application\\brave.exe"
CHROME_DRIVER = "G:\\metamask-bruteforce\\probCombo\\python\\random\\resources\\chromedriver.exe"
mm_extension_id = "nkbihfbeogaeaoehlefnkodbefgpgknn" #enter your metamask extension id here

option = webdriver.ChromeOptions()
option.add_extension(EXTENSION_PATH)
option.binary_location = BINARY_LOCATION
chromedriver = CHROME_DRIVER
s = Service(chromedriver)
driver = webdriver.Chrome(service=s, options=option)

#switch tabs
driver.switch_to.window(driver.window_handles[0])
#go to seed phrase page
driver.get('chrome-extension://'+mm_extension_id+'/home.html#initialize/create-password/import-with-seed-phrase')
time.sleep(2)
count = 1
t0 = time.time()
os.system('cls')
file_check = True
#declaring empty lists
totalLists = []
if len(os.listdir(checkPath)) == 0:
    print("No files found in the directory - Check.")
else:
    while file_check:
        if len(os.listdir(checkPath)) == 0:
            print("No files found in the directory - Check.")
            time.sleep(10)
            file_check = True
        else:
            for x in os.listdir(checkPath):
                if x.endswith(".txt"):
                    print("Opening file:", x)
                    totalLists.clear()
                    with open(r"{}\{}".format(checkPath, x), "r") as checklist:
                        for line in checklist:
                            totalLists.append(line.strip())
                    # lenght of lists
                    length = len(totalLists)
                    print("Working on file:", x)
                    looper = True
                    while looper:
                        for indiList in range(length):
                            pyperclip.copy(totalLists[indiList])

                            #PASTE CLIPBOARD TO TEXTFIELD
                            driver.find_element(by = By.XPATH, value = '//*[@id="import-srp__srp-word-0"]').send_keys(Keys.CONTROL + 'v') #paste string

                            #if invalid seed phrase:
                            try:
                                driver.find_element(by = By.CSS_SELECTOR, value = '#app-content > div > div.main-container-wrapper > div > div > div > form > div.import-srp__container > div.actionable-message.actionable-message--danger.import-srp__srp-error.actionable-message--with-icon') #check to see if invalid message pops up
                                print('Attempts', count, end = '\r', flush = False)
                                print('count/sec:', "{:.2f}".format(count/(time.time()- t0)), '---- count:',count, end='\r', flush=True)
                                count += 1

                            #if valid seed phrase:
                            except:
                                with open(r"{}\valid-{}.txt".format(validPath, todays_date), "a") as vf:
                                    vf.write(totalLists[indiList])
                                    vf.write('\n')

                        checklist.close()
                        print("Closed File:", x)
                        os.remove(r"{}\{}".format(checkPath, x))
                        looper = False

driver.quit()
exit()