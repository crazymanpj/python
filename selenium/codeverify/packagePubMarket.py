# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-31
# Author:  pangjian
from gobal_config import TEXTFIlEPATH, BANNEDWORD, DIR, APKVER
from lib import log, androidhelper
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
import sys,os,re,time

class PackagePubMarket(object):

    def __init__(self, url):
        try:
            self.driver = webdriver.Chrome()
            self.url = url
            # self.logger = log.Log('publog.txt')
            self.packagePath = ''
            self.init()
        except WebDriverException as e:
            print '启动chrome失败，重试中...'
            self.__init__(url)

    def readtextfromfile(self):
        try:
            file = open(TEXTFIlEPATH, 'r')
            text = file.read()
        except Exception as e:
            self.logger.outError('read file error')
        finally:
            file.close()

        return text

    def filterText(self, text):
        for i in BANNEDWORD:
            if text.find(i) != -1:
                self.logger.outMsg('不允许更新该文案：' + i)
                sys.exit(0)


    def getFilePathInDir(self, name):
        for root, dirs, files in os.walk(DIR):
            for filename in files:
                pattern = re.compile(name)
                match = pattern.search(filename)
                if match:
                    return os.path.join(root, filename)

    def verifyVersionCode(self):
        try:
            packageVer = androidhelper.getApkVersionCode(apkfilepath=self.packagePath)
            if packageVer != APKVER:
                self.logger.outMsg('apk版本号不一致，发布退出')
                sys.exit()
        except Exception as e:
            self.logger.outError('文件路径不在，退出' + str(e))
            sys.exit()

    def uninit(self):
        self.logger.outMsg('close chrome webdriver')
        self.driver.quit()
