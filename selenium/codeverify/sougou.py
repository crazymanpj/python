# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-24
# Author:  pangjian
from sougou_config import URL, USERNAME, PASSWORD,UPDATE_URL,CHANNELNO
from gobal_config import IS_UPDATE_TEXT
from const import TEXTFIlEPATH, AU3PATH, BANNEDWORD
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import sys,time,os
from lib import commonlib, log, mystr
from packagePubMarket import PackagePubMarket

class SOUGOU(PackagePubMarket):

    def init(self):
        self.logger = log.Log('log/sougou.txt')
        self.packagePath = self.getFilePathInDir(self.getPackageName())
        self.logger.outMsg('packagepath: ' + self.packagePath)

    def login(self, username, password):
        self.driver.maximize_window()
        login = self.driver.find_element_by_class_name('signin')
        login.click()
        time.sleep(1)
        k_username = self.driver.find_element_by_name('username')
        k_password = self.driver.find_element_by_name('password')
        login_button = self.driver.find_element_by_class_name('subbtn')


        k_username.send_keys(username)
        k_password.send_keys(password)
        time.sleep(0.5)
        login_button.click()

    def iscorretupdateurl(self):
        appName = self.driver.find_element_by_xpath("//div[@class='app-detail']/div[1]/h3[1]")
        title = appName.text
        self.logger.outMsg(title)
        self.logger.outMsg(type(title))
        # self.logger.outMsg(mystr.getstrencodingtype(title))
        if title.strip(" ") == u'':
            ret = True
        else:
            ret = False
        return ret

    def getPackageName(self):
        self.logger.outMsg('packagename: ' + 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO)
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def updateText(self):
        print '需要更新文案'
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_name('update_info')
        textarea.clear()
        textarea.send_keys(text.decode())

    def uploadPackage(self):
        time.sleep(5)
        self.driver.find_element_by_class_name('webuploader-container').click()
        time.sleep(2)
        cmd = AU3PATH + ' ' + self.packagePath
        os.system(cmd)
        time.sleep(5)
        processbar = self.driver.find_element_by_xpath("//div[@class='progress']")

        try:
            while processbar.is_displayed() != False:
                self.logger.outMsg('上传中，请等待...')
                time.sleep(10)
        except StaleElementReferenceException as e:
            self.logger.outMsg('上传完成')

        self.logger.outMsg('上传完成，已成功')

    def commit(self):
        self.logger.outMsg('commit')
        self.driver.find_element_by_id('submit').click()
        time.sleep(20)

    def publishPackage(self):
        try:
            self.driver.get(URL)
            time.sleep(1)
            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(5)
            if self.iscorretupdateurl() == False:
                self.logger.outMsg('')
                sys.exit()

            self.driver.find_element_by_link_text('编辑更新').click()
            self.verifyVersionCode()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()
            time.sleep(10)

        except Exception as e:
            self.logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()


if __name__ == '__main__':
    sougou = SOUGOU(URL)
    sougou.publishPackage()
    sougou.uninit()
