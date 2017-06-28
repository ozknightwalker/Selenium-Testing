from __future__ import unicode_literals

# for timeout
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

# Wait is use as an alternative for time.sleep and in a way more efficient

driver = webdriver.Firefox()
#  We visit facebook
driver.get("http://www.google.com")
try:
    box = driver.find_element_by_name('q')
    box.send_keys('Selenium')
    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
        (By.NAME, 'btnG')))
    button.click()
except TimeoutException:
    print("Box or Button not found in google.com")

# or just set the implicit wait implicitly_wait(seconds) 
driver.implicitly_wait(10)  # seconds
# wait for 2secs just a preview time
time.sleep(2)
driver.close()
