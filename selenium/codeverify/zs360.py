# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-21
# Author:  pangjian
from zs360_config import URL, USERNAME, PASSWORD, UPDATE_URL, CHANNELNO
from gobal_config import IS_UPDATE_TEXT, AU3PATH, APPNAME, ERROR_WRONG_UPDATE_URL
import time,sys,os,json
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from lib import log
from packagePubMarket import PackagePubMarket

class ZS360(PackagePubMarket):

    def __init__(self, url):
        try:
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
            self.logger = log.Log('360.txt')
            self.packagePath = self.getFilePathInDir(self.getPackageName())
            self.logger.outMsg(self.packagePath)
        except WebDriverException as e:
            print '启动chrome失败，重试中...'
            self.__init__(url)

    def isCorretUpdateUrl(self):
        appName = self.driver.find_element_by_class_name('appname')
        title = appName.text
        self.logger.outMsg(title)

        if title.find(APPNAME) >= 0:
            return True
        else:
            return False

    def getPackageName(self):
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def updateText(self):
        self.logger.outMsg('需要更新文案')
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_id('desc_desc')
        textarea.clear()
        textarea.send_keys(text.decode())

    def commit(self):
        self.logger.outMsg('commit')
        button = self.driver.find_element_by_id('submitform')
        self.logger.outMsg(button.get_attribute('value'))
        # button.click()
        time.sleep(20)

    def uploadPackage(self):
        self.logger.outMsg('waiting...')
        time.sleep(25)

        self.driver.find_element_by_xpath("//div[@id='normaluploadpanel']/object[1]").click()
        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@id='normaluploadpanel']/object[1]").click()
        time.sleep(3)
        cmd = AU3PATH + ' ' + '"' + self.packagePath + '"'
        self.logger.outMsg(cmd)
        os.system(cmd)
        time.sleep(5)
        uploadbar = self.driver.find_element_by_xpath("//div[@class='progressBarStatus']")

        print uploadbar.text
        print type(uploadbar.text)
        while uploadbar.text == u'上传中...':
            self.logger.outMsg('上传中，请等待...')
            time.sleep(10)

        self.logger.outMsg('上传完成，已成功')


    def login(self):
        f_cookie = open('cookie_360.txt')
        cookie = f_cookie.read()
        cookie = json.loads(cookie)

        for c in cookie:
            self.driver.add_cookie(c)

        self.driver.get(URL)

    def publishPackage(self):
        try:
            self.driver.get(URL)
            self.logger.outMsg('geturl end')
            time.sleep(5)
            self.login()
            time.sleep(3)
            self.driver.get(UPDATE_URL)
            time.sleep(3)
            if self.isCorretUpdateUrl() is False:
                self.logger.outMsg(ERROR_WRONG_UPDATE_URL)
                sys.exit()
            self.verifyVersionCode()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()
            time.sleep(3)
            self.commit()
            time.sleep(20)
        except WebDriverException as e:
            self.logger.outMsg('打开URL, selenium 错误: ' + str(e))
            sys.exit()

    def __del__(self):
        self.logger.outMsg('close chrome webdriver')
        self.driver.close()


if __name__ == '__main__':
    zs360 = ZS360(URL)
    zs360.publishPackage()
    zs360.uninit()
