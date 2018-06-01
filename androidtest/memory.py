# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-24
# Author:  pangjian
import os,re,time
from lib import log
packageName = ''

logger = log.Log('')

def getPssFromText(text):
    pattern = '( +)(TOTAL)( +)(\d+)'
    m = re.match(pattern, text)
    return m.group(4)

def getRssFromText(text):
    pass

def getMemory(packageName):
    cmd = 'adb shell dumpsys meminfo ' + packageName
    text = os.popen(cmd).readlines()
    for i in text:
        if i.find('TOTAL') >= 0:
            time.sleep(5)
            print '内存pss值为： ' + getPssFromText(i)
            logger.outMsg('内存pss值为： ' + getPssFromText(i))
            break





if __name__ == '__main__':
    while True:
        getMemory(packageName)
        time.sleep(0.3)
