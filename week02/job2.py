from selenium import webdriver
import time

try:
    # create browser object
    browser = webdriver.Chrome()
    browser.get("https://shimo.im/login?from=home")
    # find and send user info
    browser.find_element_by_xpath('//input[@name="mobileOrEmail"]').send_keys("myemail")
    browser.find_element_by_xpath('//input[@name="password"]').send_keys("password")
    # find submit and click
    button = browser.find_element_by_class_name("submit")
    button.click()
except Exception as e:
    print(e)
finally:
    browser.close()