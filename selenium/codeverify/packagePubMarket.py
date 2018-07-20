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
            option = webdriver.ChromeOptions()
            option.add_argument('disable-infobars')
            self.driver = webdriver.Chrome(chrome_options=option)
            self.url = url
            # self.logger = log.Log('publog.txt')
            self.packagePath = ''
            self.init()
        except WebDriverException as e:
            print '启动chrome失败，重试中...'
            self.__init__(url)

    @property
    def name(self):
        return str(type(self))

    def readtextfromfile(self):
        try:
            file = open(TEXTFIlEPATH, 'r')
            text = file.read()
        except Exception as e:
            self.logger.outError(self.name + '\n' + 'read file error',True)
            sys.exit()
        finally:
            file.close()

        return text

    def filterText(self, text):
        for i in BANNEDWORD:
            if text.find(i) != -1:
                self.logger.outError(self.name + '\n' + '不允许更新该文案：' + i, True)
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
                self.logger.outError(self.name + '\n' + 'apk版本号不一致，发布退出', True)
                sys.exit()
        except Exception as e:
            self.logger.outError(self.name + '\n' + '文件路径不在，退出\n' + str(e), True)
            sys.exit()

    def uninit(self):
        self.logger.outMsg('close chrome webdriver')
        self.driver.quit()
