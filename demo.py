from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Correct path to the ChromeDriver
load_dotenv()
driver_path = r'S:\pyth\chromedriver.exe'
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.implicitly_wait(10)
wait = WebDriverWait(driver, 60)

try:
    # Navigate to the login page
    driver.get('https://www.mymazevo.com/')

    # Locate the username and the login button
    username_field = wait.until(EC.presence_of_element_located((By.ID, 'email')))
    login_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'k-button')))
    username_field.send_keys('siv30@txstate.edu') 
    login_button.click()

    # TxSt Authentication
    txst_login_username = driver.find_element(By.ID, 'username')
    txst_login_username.send_keys(os.getenv("TXST_UN"))    
    txst_login_password = driver.find_element(By.ID, 'password')
    txst_login_password.send_keys(os.getenv("TXST_PWD"))
    txst_login_button = driver.find_element(By.NAME, '_eventId_proceed')
    txst_login_button.click()
    time.sleep(50)
finally:
    # Close the browser
    driver.quit()
