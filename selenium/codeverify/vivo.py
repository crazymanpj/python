# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-06-26
# Author:  pangjian
from vivo_config import URL, USERNAME, PASSWORD,UPDATE_URL,CHANNELNO
from gobal_config import AU3PATH, IS_UPDATE_TEXT, APPNAME, ERROR_WRONG_UPDATE_URL
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import sys,time,os,json
from lib import commonlib, log
from packagePubMarket import PackagePubMarket

class VIVO(PackagePubMarket):

    def init(self):
        self.logger = log.Log('vivo.txt')
        self.packagePath = self.getFilePathInDir(self.getPackageName())
        self.logger.outMsg(self.packagePath)

    def getPackageName(self):
        return 'cmgamemaster_oem_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def isCorretUpdateUrl(self):
        appName = self.driver.find_element_by_class_name('details_top_name')
        title = appName.text
        self.logger.outMsg(title)

        if title.find(APPNAME) >= 0:
            ret = True
        else:
            ret = False

        self.logger.outMsg(ret)
        return ret

    def login(self):
        print 'login'
        f1 = open('cookie_vivo.txt')
        print f1
        cookie = f1.read()
        print cookie
        cookie =json.loads(cookie)
        print cookie
        print 'tt'

        for c in cookie:
            print c
            self.driver.add_cookie(c)
        # # 刷新页面
        print 'test'
        self.driver.get(URL)
        self.driver.refresh()

    def uploadPackage(self):
        self.driver.find_element_by_link_text('编辑与更新').click()
        time.sleep(3)
        uploadbutton = self.driver.find_element_by_id('uploadAppInput')
        uploadbutton.send_keys(self.packagePath)
        time.sleep(5)
        uploadBar = self.driver.find_element_by_id('progressWrap')

        while uploadBar.is_displayed() is True:
            self.logger.outMsg('上传中，请等待...')
            time.sleep(10)

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
            time.sleep(50)
            self.driver.get(UPDATE_URL)
            time.sleep(5)
            if self.isCorretUpdateUrl() is False:
                self.logger.outMsg(ERROR_WRONG_UPDATE_URL)
                sys.exit()
            self.verifyVersionCode()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            # self.commit()
            time.sleep(20)


        except Exception as e:
            self.logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()


if __name__ == '__main__':
    vivo = VIVO(URL)
    vivo.publishPackage()
    vivo.uninit()
