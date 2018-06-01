# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-24
# Author:  pangjian
from sougou_config import URL, USERNAME, PASSWORD,UPDATE_URL, PACKAGEPATH, IS_UPDATE_TEXT
from gobal_config import TEXTFIlEPATH, AU3PATH, BANNEDWORD
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, StaleElementReferenceException
import sys,time,os
from lib import commonlib, log, mystr

logger = log.Log('sougou.txt')

class SOUGOU(object):

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url


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
        logger.outMsg(title)
        logger.outMsg(type(title))
        # logger.outMsg(mystr.getstrencodingtype(title))
        if title.strip(" ") == u'':
            ret = True
        else:
            ret = False
        return ret

    def readtextfromfile(self):
        try:
            file = open(TEXTFIlEPATH, 'r')
            text = file.read()
        except:
            print 'read file error'
        finally:
            file.close()
        print text
        return text

    def filterText(self, text):
        for i in BANNEDWORD:
            if text.find(i) != -1:
                print '不允许更新该文案：' + i
                sys.exit(0)

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
        cmd = AU3PATH + ' ' + PACKAGEPATH
        os.system(cmd)
        time.sleep(5)
        processbar = self.driver.find_element_by_xpath("//div[@class='progress']")

        try:
            while processbar.is_displayed() != False:
                logger.outMsg('上传中，请等待...')
                time.sleep(10)
        except StaleElementReferenceException as e:
            logger.outMsg('上传完成')

        logger.outMsg('上传完成，已成功')

    def commit(self):
        logger.outMsg('commit')
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
                logger.outMsg('')
                sys.exit()

            self.driver.find_element_by_link_text('编辑更新').click()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()
            time.sleep(10)

        except Exception as e:
            logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()

    def __del__(self):
        logger.outMsg("close chrome webdriver")
        self.driver.close()

if __name__ == '__main__':
    sougou = SOUGOU(URL)
    sougou.publishPackage()
