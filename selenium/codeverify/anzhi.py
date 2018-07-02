# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-06-26
# Author:  pangjian
from anzhi_config import URL, USERNAME, PASSWORD,UPDATE_URL,CHANNELNO
from gobal_config import AU3PATH, IS_UPDATE_TEXT, APPNAME, ERROR_WRONG_UPDATE_URL
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import sys,time,os,json
from lib import commonlib, log
from packagePubMarket import PackagePubMarket

class ANZHI(PackagePubMarket):

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
            self.logger = log.Log('anzhi.txt')
            self.packagePath = self.getFilePathInDir(self.getPackageName())
            self.logger.outMsg(self.packagePath)
        except WebDriverException as e:
            print '启动chrome失败，重试中...'
            self.__init__(url)

    def getPackageName(self):
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def login(self):
        f1 = open('cookie_anzhi.txt')
        cookie = f1.read()
        cookie =json.loads(cookie)
        f1.close()

        for c in cookie:
            print c
            self.driver.add_cookie(c)
        # # 刷新页面
        self.driver.get(URL)
        self.driver.refresh()

    def uploadPackage(self):
        time.sleep(15)
        self.driver.find_element_by_id('SWFUpload_0').click()
        cmd = AU3PATH + ' ' + '"' + self.packagePath + '"'
        os.system(cmd)
        time.sleep(10)
        uploadBar = self.driver.find_element_by_xpath("//div[@id='apk-queue']/div[1]")

        try:
            while uploadBar.is_displayed() is True:
                self.logger.outMsg('上传中，请等待...')
                time.sleep(10)
        except StaleElementReferenceException as e:
            self.logger.outMsg('上传完成')

        self.logger.outMsg('上传完成，已成功')

    def updateText(self):
        self.logger.outMsg('需要更新文案')
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_id('appInfo_update_des')
        textarea.clear()
        textarea.send_keys(text.decode())

    def commit(self):
        self.logger.outMsg('commit')
        button = self.driver.find_element_by_class_name('button-max')
        self.logger.outMsg(button.get_attribute('value'))
        # button.click()
        time.sleep(20)


    def publishPackage(self):
        try:
            self.driver.get(URL)
            time.sleep(3)
            self.login()
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(3)
            self.driver.find_element_by_name('soft_name').send_keys(u'')
            time.sleep(1)
            self.driver.find_element_by_name('submitted').click()
            time.sleep(1)
            self.driver.find_element_by_link_text('升级').click()
            time.sleep(5)
            self.verifyVersionCode()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()
            #
            # time.sleep(3)
            # self.commit()
            time.sleep(20)


        except Exception as e:
            self.logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()


if __name__ == '__main__':
    anzhi = ANZHI(URL)
    anzhi.publishPackage()
    anzhi.uninit()
