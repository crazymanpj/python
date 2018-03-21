#!/usr/bin/env python
#encoding=utf-8
import unittest
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver as RemoteWebDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.action_chains import ActionChains
import win32api
import win32con

class DaoHangSearch(unittest.TestCase):

    def setUp(self):
        # fp = webdriver.FirefoxProfile(r'C:\Users\kingsoft\AppData\Roaming\Mozilla\Firefox\Profiles\aq9nmxxd.default')
        self.driver = webdriver.Chrome()
        self.testurl = 'http://t.duba.com/'
        # self.initcookie()

        # self.testurl = 'http://bj.www.duba.com'
        # self.testurl = 'http://www.duba.com'
        # self.driver = RemoteWebDriver(command_executor="http://10.20.225.75:5555/wd/hub",desired_capabilities=DesiredCapabilities.FIREFOX)
        #目标：导航量，点击率
    #案例重头：搜索（百度，搜狗），名站酷站点击，通栏，搜索下方热词刷新，广告位，鼠标滚动下拉，导航二楼

    def initcookie(self, driver):
        driver.add_cookie({'name':'ad_cjzp', 'value':'close'})
        driver.add_cookie({'name': 'ad_hsbf', 'value': 'close'}) #火山爆发
        driver.add_cookie({'name': 'ad_kpgj', 'value': 'close'})
        driver.add_cookie({'name': 'ad_middleModal_close', 'value': 'close'})

    def test01_search_daohang_default(self):
        print 'zz'
        driver = self.driver
        driver.get(self.testurl)
        print "curret test url: %s"%(self.testurl)
        # self.initcookie(driver)

        # for cookie in driver.get_cookies():
            # print "%s   :   %s"%(cookie['name'], cookie['value'])
        print '清理cookie结束...'
        driver.get(self.testurl)
        assert u"毒霸网址大全" in driver.title
        hotkey_down = driver.find_element_by_id("search_keyword")
        # hotkey_down.clear()
        hotkey_down.send_keys(u"test")
        hotkey_down.send_keys(Keys.RETURN)
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        print driver.title
        assert driver.title.find('test') >= 0
        print 'test01_search_daohang_default end'

    def test02_search_hotword(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie(driver)
        driver.get(self.testurl)
        driver.find_element_by_id("search_keyword").click()
        dropdown_elem = driver.find_element_by_xpath("//div[@id='search_ext']")
        assert dropdown_elem.is_displayed() == True
        time.sleep(2)
        driver.find_element_by_xpath("//div[@class='ipt_wrap']/span[1]").click()
        # dropdown_elem = driver.find_element_by_xpath("//div[@id='search_ext']")
        assert dropdown_elem.is_displayed() == False
        time.sleep(1)
        driver.find_element_by_xpath("//div[@class='ipt_wrap']/span[1]").click()
        assert dropdown_elem.is_displayed() == True
        print 'test02_search_hotword end'

    def test03_refresh_hotkey(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie(driver)
        driver.get(self.testurl)
        for i in range(0,4):
            print i
            temptext =  driver.find_element_by_xpath("//ul[@class='hot_link']").text
            driver.find_element_by_xpath("//a[@class='ico_change']").click()
            assert temptext != driver.find_element_by_xpath("//ul[@class='hot_link']").text

    def dtest04_swicth_search(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie(driver)
        driver.get(self.testurl)
        logo_text = driver.find_element_by_xpath("//a[@id='search_logo']").get_attribute("class")
        driver.find_element_by_xpath("//div[@class='J_selectSearch ico_select']").click()
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "logo_sogou")))
        print logo_text
        if logo_text == 'logo_baidu':
            driver.find_element_by_xpath("//a[@class='logo_sogou']").click()
        elif logo_text == 'logo_sogou':
            driver.find_element_by_xpath("//a[@class='logo_baidu']").click()
        print 'debug'
        time.sleep(2)
        hotkey_down = driver.find_element_by_id("search_keyword")
        hotkey_down.send_keys(u'test')
        hotkey_down.send_keys(Keys.RETURN)
        print 'debug2'
        windows = driver.window_handles
        print windows
        print driver.title
        driver.switch_to_window(windows[1])
        print driver.title
        # assert driver.title.find("test") >= 0

    def dtest05_floor2_scrolltip(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie(driver)
        driver.get(self.testurl)

        # js = "var q=document.documentElement.scrollTop=10000"
        # driver.execute_script(js)
        # time.sleep(2)
        floor2_gj = driver.find_element_by_xpath("//a[@class='floor2_anchor']")
        print floor2_gj.is_displayed()
        while(not floor2_gj.is_displayed()):
            driver.refresh()
            floor2_gj = driver.find_element_by_xpath("//a[@class='floor2_anchor']")
        # ActionChains(driver).move_to_element(cool_textlink).

        # js = "var q=document.documentElement.scrollTop=-100"
        # driver.execute_script(js)
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0 ,0 ,100)
        # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 100)
        # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 100)
        time.sleep(1)
        floor2_wave = driver.find_element_by_xpath("//div[@id='J_FloorWave']")
        assert floor2_wave.is_displayed() == True
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1000)


    #2楼切换按钮
    #点击更多按钮正常
    #hover
    #改图标需要过换肤



    def tearDown(self):
        time.sleep(1)
        self.driver.quit()

if __name__ == "__main__":
    print 'dd'
    unittest.main()
