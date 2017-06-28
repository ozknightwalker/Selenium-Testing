from __future__ import unicode_literals

# for timeout
import time

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

capabilities = DesiredCapabilities.PHANTOMJS
# capabilities['platform'] = "WINDOWMS"
# capabilities['version'] = "10"

driver = webdriver.Firefox(capabilities=capabilities)
driver.get('http://www.google.com')

time.sleep(1)
driver.execute_script('alert("Alert here!");')

# returns False is encounters an IO error otherwise True
print driver.get_screenshot_as_file('Screenshots/file.png')


# wait for 2secs just a preview time
time.sleep(2)
driver.close()
