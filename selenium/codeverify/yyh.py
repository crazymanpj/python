# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-25
# Author:  pangjian
from yyh_config import URL, USERNAME, PASSWORD, UPDATE_URL, PACKAGEPATH, IS_UPDATE_TEXT
from gobal_config import TEXTFIlEPATH, AU3PATH, BANNEDWORD
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys,time,os
from lib import commonlib, log
from packagePubMarket import PackagePubMarket

logger = log.Log(u'')

class YYH(PackagePubMarket):

    def login(self, username, password):
        k_username = self.driver.find_element_by_name('login')
        k_password = self.driver.find_element_by_name('password')
        login_button = self.driver.find_element_by_xpath("//input[@type='image']")

        k_username.send_keys(username)
        k_password.send_keys(password)
        time.sleep(0.5)
        login_button.click()

    def iscorretupdateurl(self):
        print 'ttt'
        time.sleep(5)
        appName = self.driver.find_element_by_id('name')
        title = appName.get_attribute('value')
        logger.outMsg(title)
        logger.outMsg(type(title))
        logger.outMsg(title.strip(" "))
        if title.find(u'') >= 0:
            ret = True
        else:
            ret = False
        return ret

    def uploadPackage(self):
        print 'kkk'
        uploadbutton = self.driver.find_element_by_xpath("//div[@id='uploadapk']/div[1]/div[1]/input[1]")
        time.sleep(2)
        uploadbutton.send_keys(PACKAGEPATH)
        time.sleep(10)
        buttonText = self.driver.find_element_by_class_name('button-text')
        divUpload = self.driver.find_element_by_id('uploadapk')
        while buttonText.text != '上传APk' and buttonText.text != '':
            logger.outMsg(buttonText.text)
            logger.outMsg('上传中，等待...')
            time.sleep(10)

        logger.outMsg('上传完成，已成功')

    def updateText(self):
        logger.outMsg('需要更新文案')
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_id('updatemsg')
        textarea.clear()
        textarea.send_keys(text.decode())

    def commit(self):
        logger.outMsg('commit')
        # self.driver.find_elemnt_by_id('submit').click()
        time.sleep(20)

    def publishPackage(self):
        logger.outMsg('start')
        try:
            self.driver.get(URL)
            time.sleep(1)
            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(1)
            self.driver.find_element_by_id('noticecheck').click()
            self.driver.find_element_by_id('switch').click()

            if self.iscorretupdateurl() == False:
                logger.outMsg('')
                sys.exit()
            self.driver.find_element_by_id('switch').click()
            time.sleep(1)
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()
            time.sleep(10)
            time.sleep(200)
        except Exception as e:
            logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()

if __name__ == '__main__':
    yyh = YYH(URL)
    yyh.publishPackage()
