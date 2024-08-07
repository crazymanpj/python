# encoding=utf-8
# Date:    2017-10-17
# Author:  pangjian
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
from selenium.webdriver.remote.webelement import WebElement
import win32api
import win32con
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class DaoHangSearch(unittest.TestCase):

    def setUp(self):
        # fp = webdriver.FirefoxProfile(r'C:\Users\kingsoft\AppData\Roaming\Mozilla\Firefox\Profiles\aq9nmxxd.default')
        # self.driver = webdriver.Chrome()
        self.testurl = 'http://t.duba.com'
        # self.initcookie()
        # self.testurl = 'http://bj.www.duba.com'
        # self.testurl = 'http://www.duba.com'
        self.driver = RemoteWebDriver(command_executor="http://10.12.128.129:4444/wd/hub",desired_capabilities=DesiredCapabilities.CHROME)
        # 目标：导航量，点击率
        # 案例重头：搜索（百度，搜狗），名站酷站点击，通栏，搜索下方热词刷新，广告位，鼠标滚动下拉，导航二楼

    def initcookie(self):
        print 'initcookie'
        self.driver.add_cookie({'name':'ad_cjzp', 'value':'close'})
        self.driver.add_cookie({'name': 'ad_hsbf', 'value': 'close'}) #火山爆发
        self.driver.add_cookie({'name': 'ad_kpgj', 'value': 'close'})
        self.driver.add_cookie({'name': 'ad_middleModal_close', 'value': 'close'})
        self.driver.add_cookie({'name': 'btmask', 'value': '1522166400000-30336722'})

    def closeads(self, driver):
        print 'closeads'
        dbmc = driver.find_element_by_class_name('J_BottomAdBan_bg')
        if dbmc.is_displayed == True:
            print "true"
            dbmc.click()

    def scrolltest(self):
        time.sleep(5)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1000)
        time.sleep(5)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1000)
        time.sleep(5)

    # 搜索框搜索内容
    def dtest01_search_daohang_default(self):
        driver = self.driver
        driver.get(self.testurl)
        print("curret test url: %s"%(self.testurl))
        # self.initcookie(driver)
        # for cookie in driver.get_cookies():
        # print(cookie['name'], cookie['value'])
        # print(sys.getdefaultencoding())
        driver.get(self.testurl)
        assert u"毒霸网址大全" in driver.title
        hotkey_down = driver.find_element_by_id("search_keyword")
        # hotkey_down.clear()
        text = u'test'
        print text
        hotkey_down.send_keys(text)
        hotkey_down.send_keys(Keys.RETURN)
        time.sleep(2)
        windows = driver.window_handles
        driver.switch_to_window(windows[1])
        print(driver.title)
        assert driver.title.find('test') >= 0
        print('test01_search_daohang_default end')

    # 搜索框内相关操作，点击搜索框，收起，点击右边数字红点 收起
    def test02_search_hotword(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie()
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
        print('test02_search_hotword end')

    # 热词左侧刷新
    def dtest03_refresh_hotkey(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie()
        driver.get(self.testurl)
        for i in range(0, 4):
            temptext = driver.find_element_by_xpath("//ul[@class='hot_link']").text
            driver.find_element_by_xpath("//a[@class='ico_change']").click()
            assert temptext != driver.find_element_by_xpath("//ul[@class='hot_link']").text
        print('dtest03_refresh_hotkey end')

    # 新加热词右侧下拉操作
    #需要驱动最新，否则报错
    def dtest04_hotword_dropdown(self):
        driver = self.driver
        # driver.set_window_size(1024, 800)
        driver.get(self.testurl)
        # self.initcookie(driver)
        driver.maximize_window()
        # driver.set_window_size(1200,800)

        print('test')
        element = driver.find_element_by_xpath("//a[@class='s_tico']").click()
        dropdown = driver.find_element_by_xpath("//ul[@class='s_hottab operate']")
        assert dropdown.is_displayed() == True
        time.sleep(1)
        element = driver.find_element_by_xpath("//a[@class='s_tico active']").click()
        assert dropdown.is_displayed() == False
        print('test04_hotword_dropdown end')

    # 切换搜索引擎
    def dtest05_swicth_search(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie(driver)
        driver.get(self.testurl)
        logo_text = driver.find_element_by_xpath("//a[@id='search_logo']").get_attribute("class")
        driver.find_element_by_xpath("//div[@class='J_selectSearch ico_select']").click()
        element = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.CLASS_NAME, "logo_sogou")))
        print(logo_text)
        if logo_text == 'logo_baidu':
            driver.find_element_by_xpath("//a[@class='logo_sogou']").click()
        elif logo_text == 'logo_sogou':
            driver.find_element_by_xpath("//a[@class='logo_baidu']").click()
        print('debug')
        time.sleep(2)
        hotkey_down = driver.find_element_by_id("search_keyword")
        hotkey_down.send_keys(u'test')
        hotkey_down.send_keys(Keys.RETURN)
        print('debug2')
        windows = driver.window_handles
        print(windows)
        print(driver.title)
        driver.switch_to_window(windows[1])
        print(driver.title)
        # assert driver.title.find("test") >= 0

    #2楼
    def dtest06_floor2_scrolltip(self):
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie()
        driver.get(self.testurl)
        driver.maximize_window()

        floor2_gj = driver.find_element_by_xpath("//a[@class='floor2_anchor operate']")
        print(floor2_gj.is_displayed())
        while(not floor2_gj.is_displayed()):
            driver.refresh()
            floor2_gj = driver.find_element_by_xpath("//a[@class='floor2_anchor operate']")
        time.sleep(2)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0 ,0 ,100)
        # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 100)
        # win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 100)
        time.sleep(1)
        floor2_wave = driver.find_element_by_xpath("//div[@id='J_FloorWave']")
        assert floor2_wave.is_displayed() == True
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 1000)
        floor2_wrap = driver.find_element_by_xpath("//div[@class='floor2-wrap']")
        time.sleep(1)
        assert floor2_wrap.is_displayed() == True

        driver.find_element_by_xpath("//ul[@id='J_el11_list']/li[2]").click()
        time.sleep(1)
        driver.find_element_by_xpath("//ul[@id='J_el11_list']/li[1]").click()
        time.sleep(1)
        win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0 ,0 ,-1000)
        time.sleep(1)

    #通栏
    def dtest07_subsite_switch_scroll(self):
        driver = self.driver
        driver.get(self.testurl)
        driver.maximize_window()
        # driver.switch_to_frame(driver.find_element_by_xpath("//a[contains(@iframesrc, 'ent.html')]"))

        driver.find_element_by_xpath("//div[@class='second_nav s_change']/ul/li[3]").click()
        self.scrolltest()
        driver.find_element_by_xpath("//div[@class='second_nav s_change']/ul/li[7]").click()
        self.scrolltest()

    #信息流
    def dtest08_xxl_switch_scroll(self):
        print 'test08_xxl_switch_scroll'
        driver = self.driver
        driver.get(self.testurl)
        self.initcookie()
        driver.get(self.testurl)
        driver.maximize_window()

        js = 'window.scrollTo(100, 4000)'
        driver.execute_script(js)
        time.sleep(3)
        driver.find_element_by_xpath("//div[@class='ss_tabbox operate']/div/a[4]").click()
        self.scrolltest()
        driver.find_element_by_xpath("//div[@class='ss_tabbox operate']/div/a[8]").click()
        self.scrolltest()
        print 'test08_xxl_switch_scroll end'


    #点击更多按钮正常
    #hover
    #改图标需要过换肤
    #测试多个案例后计算每次打开url后加载onload的时间，求平均值
    #记录元素坐标位置，判断是否界面错乱
    #通过图片识别来判断是否界面错乱
    def tearDown(self):
        time.sleep(1)
        # self.driver.quit()
        self.driver.close()

if __name__ == "__main__":
    print('py3')
    unittest.main()
