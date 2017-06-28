from __future__ import unicode_literals

# for timeout
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.ANDROID
# capabilities['platform'] = "WINDOWMS"
# capabilities['version'] = "10"

driver = webdriver.PhantomJS(desired_capabilities=capabilities)
driver.get('http://www.google.com')
# returns False is encounters an IO error otherwise True
print driver.get_screenshot_as_file('Screenshots/file.png')


# wait for 2secs just a preview time
time.sleep(2)
driver.close()
