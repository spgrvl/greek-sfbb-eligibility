from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time
import config

if os.name == "nt":
    chrome_path = r"C:\chromedriver_win32\chromedriver.exe"
elif os.name == "posix":
    chrome_path = "/usr/lib/chromium-browser/chromedriver"
else:
    print("Error: Chrome path is not set for this os: " + os.name)

def check_message():
    try:
        active_msg = driver.find_element_by_id("ctl00_cphMain_lblSuccessMsgActive")
        print(active_msg.text)
        coupon_url = active_msg.find_element_by_tag_name('a').get_attribute('href')
        print(coupon_url)
    except:
        try:
            inactive_msg = driver.find_element_by_id("ctl00_cphMain_lblSuccessMsgInActive")
            print(inactive_msg.text)
            signup_url = inactive_msg.find_element_by_tag_name('a').get_attribute('href')
            print(signup_url)
        except:
            unavailable_msg = driver.find_element_by_css_selector("div[class='alert alert-danger']")
            print(unavailable_msg.text)
    driver.quit()
    exit()

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path=chrome_path, options=chrome_options)

url = "https://submit.sfbb.gr/EligibilityCheck.aspx"
driver.get(url)
time.sleep(1)

driver.find_element_by_id("ctl00_cphMain_txtZipCode_I").send_keys(config.zip_code)
driver.find_element_by_id("ctl00_cphMain_btnCheckZipCode").click()
time.sleep(1)

try:
    driver.find_element_by_id("ctl00_cphMain_txtAddress_I").send_keys(config.address)
except:
    check_message()

driver.find_element_by_id("ctl00_cphMain_btnCheckAddress").click()
time.sleep(1)

try:
    driver.find_element_by_id("ctl00_cphMain_txtStreetNumber_I").send_keys(config.home_number)
except:
    check_message()

driver.find_element_by_id("ctl00_cphMain_btnCheckEligibility").click()
time.sleep(1)
check_message()