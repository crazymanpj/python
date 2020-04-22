# !/usr/bin/env python
# encoding=utf-8
# Date:    2019-01-04
# Author:  pangjian
import time
import datetime
import os
import subprocess

testcasepath= r'/home/kingsoft/testcase'
testcase = 'commongame.air'
testresultpath = r'/home/kingsoft/testresult'
htmlpath = r'/var/lib/jenkins/workspace/gamemoney/htmlreport/output'

t = datetime.datetime.now()
time = t.strftime("%Y%m%d_%H%M%S")

testcaseabspath = os.path.join(testcasepath, testcase)
print(testcaseabspath)
outputpath = os.path.join(testresultpath, time)
os.mkdir(outputpath)
print(outputpath)
outputfile = os.path.join(testresultpath, time, time + '.html')
print(outputfile)

cmd_run = 'airtest run ' + testcaseabspath + ' --log ' + outputpath
print(cmd_run)
# p_run = subprocess.Popen(cmd_run)
# p_run.communicate()
os.system(cmd_run)
cmd_gen = 'airtest report ' + testcaseabspath + ' --log_root ' + outputpath + ' --outfile ' + outputfile + ' --lang zh ' + '--export ' + outputpath
print(cmd_gen)
os.system(cmd_gen)
cmd_html = 'cp -f -r ' + os.path.join(outputpath, 'commongame.log') + ' ' + htmlpath
print(cmd_html)
os.system(cmd_html)
