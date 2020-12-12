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

def print_error():
    error_message = driver.find_element_by_css_selector("div[class='alert alert-danger']").text
    print(error_message)
    driver.quit()
    exit()

chrome_options = Options()
chrome_options.add_argument("--headless")
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
    print_error()

driver.find_element_by_id("ctl00_cphMain_btnCheckAddress").click()
time.sleep(1)

try:
    driver.find_element_by_id("ctl00_cphMain_txtStreetNumber_I").send_keys(config.home_number)
except:
    print_error()

driver.find_element_by_id("ctl00_cphMain_btnCheckEligibility").click()
time.sleep(1)
print_error()