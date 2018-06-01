# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-21
# Author:  pangjian
from zs360_config import URL, USERNAME, PASSWORD, UPDATE_URL
import time,sys
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from lib import log

logger = log.Log('', isdebug=True)

class ZS360(object):

    def __init__(self, url):
        chromeOpitons = webdriver.ChromeOptions()
        prefs = {
        "profile.managed_default_content_settings_images":1,
        "profile.default_content_setting_values.plugins":1,
        "profile.content_settings.plugin_whitelist.adobe-flash-player":1,
        "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1,
        "credentials_enable_service":False,
        "profile.password_manager_enabled" : False
        }
        chromeOpitons.add_experimental_option('prefs', prefs)
        self.driver = webdriver.Chrome(chrome_options=chromeOpitons)
        self.url = url

    def uploadPackage(self):
        time.sleep(5)
        time.sleep(20)
        self.driver.find_element_by_xpath("//div[@id='normaluploadpanel']/object[1]").click()
        logger.outMsg('click')
        time.sleep(10)

    def login(self, username, password):
        k_username = self.driver.find_element_by_name('userName')
        k_password = self.driver.find_element_by_name('password')
        login_button = self.driver.find_element_by_class_name('quc-button-submit')

        k_username.send_keys(username)
        k_password.send_keys(password)
        time.sleep(5)
        login_button.click()

    def publishPackage(self):
        try:
            self.driver.get(URL)
            logger.outMsg('geturl end')
            time.sleep(5)
            self.login(USERNAME, PASSWORD)
            time.sleep(3)
            self.driver.get(UPDATE_URL)
            time.sleep(60)
        except WebDriverException as e:
            logger.outMsg('打开URL, selenium 错误: ' + str(e))
            sys.exit()

    def __del__(self):
        logger.outMsg('close chrome webdriver')
        self.driver.close()


if __name__ == '__main__':
    zs360 = ZS360(URL)
    zs360.publishPackage()
