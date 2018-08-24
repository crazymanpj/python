# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-06-01
# Author:  pangjian
from lenovo_config import URL, USERNAME, PASSWORD, UPDATE_URL, CHANNELNO
from gobal_config import IS_UPDATE_TEXT
from const import TEXTFIlEPATH, AU3PATH, BANNEDWORD
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys,time,os
from lib import log
from packagePubMarket import PackagePubMarket

class Lenovo(PackagePubMarket):

    def init(self):
        self.logger = log.Log('log/lenovo.txt')
        self.packagePath = self.getFilePathInDir(self.getPackageName())
        self.logger.outMsg('packagepath: ' + self.packagePath)

    def login(self, username, password):
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(1)
        k_username = self.driver.find_element_by_name('username')
        k_password = self.driver.find_element_by_name('password')
        login_button = self.driver.find_element_by_class_name('jsSubBtn')

        k_username.send_keys(username)
        k_password.send_keys(password)
        time.sleep(0.5)
        login_button.click()

    def uploadPackage(self):
        uploadButton = self.driver.find_element_by_class_name('file_view')
        time.sleep(2)
        uploadButton.click()
        time.sleep(2)
        cmd = AU3PATH + ' ' + self.packagePath
        os.system(cmd)
        time.sleep(10)
        barText = self.driver.find_element_by_xpath("//div[@class='file_bar']/span[3]/span[1]")
        # gou = self.driver.find_element_by_class_name('')
        self.logger.outMsg(barText.text)
        while barText.text != '':
            self.logger.outMsg('上传中，请等待...')
            time.sleep(10)

        self.logger.outMsg('上传完成，已成功')

    def getPackageName(self):
        self.logger.outMsg('packagename: ' + 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO)
        return 'cmgamemaster_oem_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def commit(self):
        self.logger.outMsg('commit')
        self.driver.find_element_by_xpath("//div[@class='submit']/button[1]").click()
        time.sleep(20)

    def updateText(self):
        self.logger.outMsg('需要更新文案')
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_name('newCharacter')
        textarea.clear()
        textarea.send_keys(text.decode())

    def publishPackage(self):
        self.logger.outMsg('start')
        try:
            self.driver.get(URL)
            time.sleep(1)

            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(5)
            self.verifyVersionCode()
            self.uploadPackage()
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()
            time.sleep(10)
            time.sleep(30)
        except Exception as e:
            self.logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()


if __name__ == '__main__':
    lenovo = Lenovo(URL)
    lenovo.publishPackage()
    lenovo.uninit()
