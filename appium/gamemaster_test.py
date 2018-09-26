# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
import unittest
from appium import webdriver
import appium_util,gamemaster_util
import time
from appium.webdriver.common.touch_action import TouchAction


class MomentTest(unittest.TestCase):

    def setUp(self):
        # desired_caps = {}
        # desired_caps['platformName'] = 'Android'
        # desired_caps['platformVersion'] = '7.1.1'
        # desired_caps['deviceName'] = '87ddde94'
        # desired_caps['appPackage'] = ''
        # desired_caps['appActivity'] = '.ui.main.GameMainActivity'

        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '6.0.1'
        desired_caps['deviceName'] = '26eda776'
        desired_caps['appPackage'] = ''
        desired_caps['appActivity'] = '.ui.main.GameMainActivity'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".main:id/guide_submit_iv").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".main:id/guide_submit_iv").click()
        self.driver.implicitly_wait(30)
        print 'setup end'

    def dtest01_view_information_flow(self):
        time.sleep(5)
        print 'start test01_view_information_flow'
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='社区']").click()
        time.sleep(5)
        self.driver.implicitly_wait(30)
        print 'start swipLeft'
        time.sleep(3)
        appium_util.swipLeft(self.driver)
        time.sleep(3)
        appium_util.swipeDown(self.driver)
        kj = None
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id(".moment:id/comment_ly")
        except:
            pass
        print kj
        assert kj is not None
        kj = None
        print 'start swipRight'
        appium_util.swipRight(self.driver)
        time.sleep(3)
        try:
            kj = self.driver.find_element_by_id(".moment:id/tv_name")
        except Exception as e:
            pass
        assert kj is not None
        kj = None
        print 'start swipRight'
        appium_util.swipRight(self.driver)
        self.driver.implicitly_wait(30)
        time.sleep(5)
        try:
            kj = self.driver.find_element_by_id(".moment:id/iv_empty")
        except Exception as e:
            pass

        assert kj is not None

    def test02_publish(self):
        self.login()
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='社区']").click()
        appium_util.swipRight(self.driver)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".moment:id/iv_publish").click()
        self.driver.implicitly_wait(30)
        editext = self.driver.find_element_by_id(".moment:id/et_moment_content")
        print editext
        editext.send_keys('test')
        self.driver.find_element_by_id(".moment:id/btn_publish").click()
        time.sleep(3)
        publishtext = self.driver.find_elements_by_id(".moment:id/tv_user_publish_text")[0]
        assert publishtext.text == "test"
        time.sleep(5)
        gamemaster_util.nav_my(self.driver)
        self.driver.implicitly_wait(30)
        gamemaster_util.nav_sub_shequ(self.driver)
        moment = self.driver.find_elements_by_id(".moment:id/feed_root_layout")[0]
        appium_util.my_longpress(self.driver, moment)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".moment:id/iv_content_delete_self").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".moment:id/btn_confirm_pos").click()
        # moment = self.driver.find_elements_by_id(".moment:id/feed_root_layout")[0]
        #判断元素不在或第一个元素text不是test



    def login(self):
        time.sleep(5)
        print 'start test01_view_information_flow'
        self.driver.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()
        time.sleep(5)
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".account:id/tv_begin_game").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_id(".account:id/qq_button").click()
        self.driver.implicitly_wait(30)
        self.driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
        self.driver.implicitly_wait(30)

    def dtest03_videoplay(self):
        print 'start'
        gamemaster_util.nav_shequ(self.driver)
        print 'end'
        self.driver.implicitly_wait(30)
        time.sleep(3)
        appium_util.swipLeft(self.driver)
        print 'start2'
        self.driver.implicitly_wait(30)
        videolist = self.driver.find_elements_by_id(".moment:id/iv_outline")
        if videolist[0].is_displayed() == True:
            self.driver.find_elements_by_id(".moment:id/media_video_btn")[0].click()
            time.sleep(10)
            self.driver.back()
        else:
            return False


    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
