# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-01-09
# Author:  pangjian
# version: 1.0
import os,shutil
import myconfig
import time

# configfilepath = "c:\Users\kingsoft\Desktop\makepacket.ini"
configfilepath = "D:\makepacketTools\makepacket.ini"

def getconfigpath():
    localsvnpath = myconfig.getconfigvalue(configfilepath, 'common', 'localsvnpath')
    svnfile1 = myconfig.getconfigvalue(configfilepath, 'duba', '168_hmpg')
    svnfile2 = myconfig.getconfigvalue(configfilepath, 'duba', '94_hmpg')
    return localsvnpath, os.path.dirname(svnfile1),os.path.dirname(svnfile2)

# def getcommand():
#     localsvnpath, svnfile1,svnfile2 = getconfigpath()
#     cmd1 =

def svnupdate(svnpath):
    cmd_clean = "svn.exe cleanup " + svnpath
    cmd_update = "svn.exe update " + svnpath
    os.system(cmd_clean)
    os.system(cmd_update)


if __name__ == '__main__':
    svnlist = getconfigpath()
    for i in svnlist:
        svnupdate(i)
        time.sleep(0.1)
