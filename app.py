from __future__ import unicode_literals

# for timeout
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Note: reason for using xpaths for finding elements is that facebook page
# element ids may vary from time to time so it's hard to locate an element/s

driver = webdriver.Firefox()
#  We visit facebook
driver.get("http://www.facebook.com")

# First we find an input element with a name of `firstname`
firstName = driver.find_element_by_xpath('//input[@name="firstname"]')
# input `First Name` in the field the locate the next field using the tab
# indexing the input `Last Name` to the next field navigated
firstName.send_keys('First Name')
firstName.send_keys(Keys.TAB, 'Last Name')
email = driver.find_element_by_xpath('//input[@name="reg_email__"]')
email.send_keys('tada@gmail.com')
# we trigger sleep here since a form field is appended upon setting a valid
# value for the email field
time.sleep(2)
email.send_keys(Keys.TAB, 'tada@gmail.com')
password = driver.find_element_by_xpath('//input[@name="reg_passwd__"]')
password.send_keys('tada_password_ni')
# Use Keys to navigate the dropdown values
password.send_keys(Keys.TAB, Keys.ARROW_DOWN, Keys.TAB, Keys.ARROW_DOWN)

# get all input elements with a name `sex`
genders = driver.find_elements_by_xpath('//input[@name="sex"]')
print len(genders)
# iterate all gender and then trigger click events
for gender in genders:
    print gender.get_attribute('value')
    gender.click()

# Import Select module to use some helpful methos  for interacting
# select element
from selenium.webdriver.support.ui import Select
select = Select(driver.find_element_by_id('month'))
# you can use `select_by_index`, `select_by_visible_text`,
# and `select_by_value`
select.select_by_visible_text('Nov')
# if you want to get all possible options on the select element
options = select.options

# if you have a multi-select element and you want to de-select all then you
# can call the deselect_all function to do so
# select.deselect_all()

# if you have and alert and want to access or deny
# alert = driver.switch_to_alert()
# alert.deny()
# alert.accept()
# alert.authenticate(username, password) if alert is an authentication alert Implicitly ‘clicks ok’

# Navigating history
driver.get('http://www.google.com')
# to go to the previous page
driver.back()
# to go forward
driver.forward()

# setting cookies
cookie = {'name': 'cookie', 'value': 'baked'}
driver.add_cookie(cookie)
# accessing the browser cookie
print driver.get_cookies()

# And now output all the available cookies for the current URL
driver.get_cookies()

# for mouse navigations and stuff
from selenium.webdriver.common.action_chains import ActionChains

menu = driver.find_element_by_id('gbwa')
hidden_submenu = driver.find_element_by_id("gb36")

# action chaining for mouse events
ActionChains(driver).move_to_element(menu).click(menu).move_to_element(
    hidden_submenu).click(hidden_submenu).perform()


# wait for 2secs just a preview time
time.sleep(2)
driver.close()
