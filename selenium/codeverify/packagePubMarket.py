# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-31
# Author:  pangjian
from gobal_config import TEXTFIlEPATH, BANNEDWORD
from lib import log
from selenium import webdriver
import sys

class PackagePubMarket(object):

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url
        self.logger = log.Log('publog.txt')

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

    def __del__(self):
        self.logger.outMsg('close chrome webdriver')
        self.driver.close()
