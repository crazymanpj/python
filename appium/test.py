#coding=utf-8
from appium import webdriver
import time
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0.1'
desired_caps['deviceName'] = '26eda776'
desired_caps['appPackage'] = ''
desired_caps['appActivity'] = ''

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)


def test_login():
    time.sleep(15)
    print 'start'
    driver.find_element_by_id("").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("").click()
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("").click()
    driver.implicitly_wait(30)
    driver.find_element_by_id("").click()
    #隐性等待
    driver.implicitly_wait(30)
    driver.find_element_by_xpath("//android.widget.Button[@text='登录']").click()
    print 'end'
    time.sleep(500)
    driver.quit()

def test_helishadi():
    time.sleep(10)
    print 'start'
    driver.find_element_by_id("").click()
    driver.implicitly_wait(30)
    time.sleep(10)

    


if __name__ == '__main__':
    test_helishadi()
