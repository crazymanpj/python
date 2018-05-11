# !/usr/bin/env python
# encoding=utf-8
# Date:    2017-02-22
# Author:  pangjian
# windows相关
import os,shutil
import datetime
import time

def removeFileInFirstDir(targetDir): 
    for file in os.listdir(targetDir):
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(targetFile):     
            os.remove(targetFile)
        elif os.path.isdir(targetFile):
            shutil.rmtree(targetFile)

def getlast7day():
	currenttime = datetime.datetime.now()
	delta1 = datetime.timedelta(days=1)
	delta2 = datetime.timedelta(days=7)
	startday = currenttime - delta2
	endday = currenttime - delta1
	starttime = startday.strftime("%Y-%m-%d")
	endtime = endday.strftime("%Y-%m-%d")
	return starttime, endtime

def getftpdomain(ftppath):
	n_domain_start = ftppath.index("ftp://")
	n_domain_end = ftppath.index("/", 7)
	domain = ftppath[n_domain_start + 6 : n_domain_end]
	return domain

def waitfortime_second(starttime, waitingsenconds, breaksenconds):
	while 1:
		endtime = datetime.datetime.now()
		print endtime
		if (endtime - starttime).seconds >= 300:
			break
		else:
			time.sleep(breaksenconds)
			continue