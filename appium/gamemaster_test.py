# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
import unittest
from appium import webdriver
import appium_util
import time


class MomentTest(unittest.TestCase):

    def setUp(self):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '26eda776'
        desired_caps['appPackage'] = ''
        desired_caps['appActivity'] = ''

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id("").click()
        self.driver.implicitly_wait(30)

    def test01_view_information_flow(self):
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='社区']").click()
        time.sleep(5)
        self.driver.implicitly_wait(30)
        print 'start swipLeft'
        time.sleep(3)
        appium_util.swipLeft(self.driver)
        kj = None
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id("")
        except:
            pass
        print kj
        assert kj is not None
        kj = None
        print 'start swipRight'
        appium_util.swipRight(self.driver)
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id("")
        except Exception as e:
            pass
        assert kj is not None
        kj = None
        print 'start swipRight'
        appium_util.swipRight(self.driver)
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id("")
        except Exception as e:
            pass

        assert kj is not None

    def test02_publish(self):
        

    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
