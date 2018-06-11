# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-06-01
# Author:  pangjian
from huawei_config import URL, USERNAME, PASSWORD, UPDATE_URL, PACKAGEPATH, IS_UPDATE_TEXT
from gobal_config import TEXTFIlEPATH, AU3PATH, BANNEDWORD
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys,time,os
from lib import log
from packagePubMarket import PackagePubMarket

logger = log.Log('huawei.txt')

class HUAWEI(PackagePubMarket):

    def login(self, username, password):
        self.driver.find_element_by_link_text('登录').click()
        k_username = self.driver.find_element_by_id('login_userName')
        k_password = self.driver.find_element_by_id('login_password')
        login_button = self.driver.find_element_by_id('btnLogin')

        k_username.send_keys(username)
        k_password.send_keys(password)
        time.sleep(0.5)
        login_button.click()

    def isCorretUpdateUrl(self):
        time.sleep(5)
        appName = self.driver.find_element_by_xpath("//div[@class='section-head']/span[1]")
        title = appName.text
        logger.outMsg(title)

        if title.find(u'') >= 0:
            ret = True
        else:
            ret = False

        logger.outMsg(ret)
        return ret

    def uploadPackage(self):
        time.sleep(3)
        uploadButton = self.driver.find_element_by_xpath("//div[@class='subtitle']/a[1]")
        uploadButton.click()
        time.sleep(1)
        self.driver.find_elements_by_xpath("//div[@class='uploadbar']/img[1]").click()
        time.sleep(2)
        cmd = AU3PATH + ' ' + PACKAGEPATH
        os.system(cmd)



    def publishPackage(self):
        logger.outMsg('start')
        try:
            self.driver.get(URL)
            time.sleep(3)
            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(1)
            if self.isCorretUpdateUrl() == False:
                logger.outMsg('')
                sys.exit()
            self.uploadPackage()
            time.sleep(300)
        except Exception as e:
            logger.outError("使用selenium启动chrome出错：" + str(e))
            sys.exit()

if __name__ == '__main__':
    huawei = HUAWEI(URL)
    huawei.publishPackage()
