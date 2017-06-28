from __future__ import unicode_literals

# First we import the necessary modules for selenium to work
from selenium import webdriver
# Keys module provides keys in the keyboard e.g RETURN, ALT, etc.
from selenium.webdriver.common.keys import Keys

# First we create our firefox webdriver
driver = webdriver.Firefox()  # this can be Chrome(), PhantomJS() web drivers

# Then navigate to the page/url provided
driver.get("http://www.google.com")
# just for testing, check if the page title has `Google` in it
assert 'Google' in driver.title
# find HTML element with and id of `lst-ib`
elem = driver.find_element_by_id('lst-ib')
# Clear out the field
elem.clear()
# Provide input to the element then press enter key to trigger form submit
string = 'this is a testing selenium'
elem.send_keys(string)
assert string == elem.get_attribute('value')
elem.send_keys(Keys.RETURN)
# close browser
driver.close()
