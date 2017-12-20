#! python3


aaaaaa
import unittest
from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'ios'
desired_caps['platformVersion'] = '11.0'
desired_caps['deviceName'] = 'iPhone Simulator'
desired_caps['app'] = '/Users/niejun/Documents/myproject/sample-code-master/sample-code/apps/TestApp/build/Release-iphonesimulator/TestApp-iphonesimulator.app'
desired_caps['noReset'] = 'false'

driver = webdriver.Remote('http://localhost:4723/wd/hub',desired_caps)

els1 = driver.find_element_by_accessibility_id('TextField1')
els1.send_keys(10)
els2 = driver.find_element_by_accessibility_id('TextField2')
els2.send_keys(100)
els3 = driver.find_element_by_xpath('//XCUIElementTypeButton[@name=\"ComputeSumButton\"]')
els3.click()
els4 = driver.find_element_by_accessibility_id('Answer')

if 100 == int(els4.text):
    print('text=100')
else:
    print('text=' + els4.text)





driver.quit()
