# !/usr/bin/env python
# encoding=utf-8
# Date:    2017-01-09
# Author:  pangjian
# version: 1.0
import threading
# from lib import myconfig
# import myconfig_py3
import myconfig
import os
import time
import subprocess
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import logging
logger = logging.getLogger('dbpackage')

class Singleton(object):

    INSTANCE = None

    lock = threading.RLock()
    threads = []
    handle = None

    def __new__(cls, configfile='', argvs=''):
        cls.configfile = configfile
        cls.argvs = argvs
        cls.lock.acquire()
        if cls.INSTANCE is None:
            cls.INSTANCE = super(Singleton, cls).__new__(cls)
        cls.lock.release()
        return cls.INSTANCE

    def getisworking(self):
        self.lock.acquire()
        isworking = myconfig.getconfigvalue(self.configfile, 'singletonthread', 'isworking')
        logger.debug(isworking)
        if isworking != '99':
            logger.debug(self.configfile)
            logger.debug('writing..')
            # myconfig.writeinivalue(self.configfile, 'singletonthread', 'isworking', '1')
            self.lock.release()
            return True
        else:
            print('working...')
            self.lock.release()
            return False

    def executebin(self):
        pass

    def makepackage_thread(self):
        if self.getisworking() is True:
            # os.system(self.getfilepath())
            try:
                self.setCurrentProduct()
                args = self.getfilepath() + ' ' + self.argvs
                logger.debug('start call script..')
                logger.debug(args)
                self.handle = subprocess.Popen(args)
                logger.debug('call script end...')
                time.sleep(0.1)
            except Exception as e:
                logger.debug('call script error...')
                logger.debug(str(e))
                traceback.print_exc()
                self.resetworking()

            return True
        else:
            logger.debug('is working is False')
            return False

        # for i in self.threads:
        #     i.start()

    def queryprocess(self):
        isworking = myconfig.getconfigvalue(self.configfile, 'singletonthread', 'isworking')
        if isworking == '0':
            return False
        else:
            return True

    def resetworking(self):
        logger.debug('resetworking')
        myconfig.writeinivalue(self.configfile, 'singletonthread', 'isworking', '0')

    def resetworking_bymanu(self):
        logger.debug('resetworking by manually')
        myconfig.writeinivalue(self.configfile, 'singletonthread', 'isworking', '-1')

    def stop_makepackage(self):
        subprocess.Popen("taskkill /F /T /PID %i"%self.handle.pid, shell=True)
        self.resetworking()

    def getfilepath(self):
        # print(os.getcwd())
        filename = myconfig.getconfigvalue(self.configfile, 'bininfo', 'filename')
        # print(filename)
        filepath = myconfig.getconfigvalue(self.configfile, 'bininfo', 'filepath')
        # print(filepath)
        return os.path.join(filepath, filename)

    def winwaitcallexe(self, waitingsecond, breaksecond):
        popen = subprocess.Popen(self.argvs)
        waitcount = 0
        while(popen.poll() == None):
            logger.debug('not finished')
            time.sleep(breaksecond)
            waitcount = waitcount + breaksecond
            if(waitcount >= waitingsecond):
                popen.kill()
        logger.debug('winwaitcallexe end...')
        return True

    def getArgvByName(self, argv):
        for i in self.argvs.split(' '):
            temp = '-' + argv + '='
            logger.debug(temp)
            if i.find(temp) == 0:
                return i.replace(temp, '')

    def setCurrentProduct(self):
        product = self.getArgvByName('product')
        myconfig.writeinivalue(self.configfile, 'share', 'product', product)

if __name__ == '__main__':
    # ret = subprocess.Popen('f:\Tools\makedata.exe -product=duba -isnewitem=1 -itemname=lenovo -tryno=1337 -packettype=exe -packetmodel=silence -tid1=99 tid2=33 tod1=77 tod2=66 -fixuplive=1 -islokmp=1 -specialfile=1 -localname=kinst_1270.exe')
    a = Singleton('stconfig.ini', '-product=kp -isnewitem=1 -itemname=lenovo -tryno=1337 -packettype=exe -packetmodel=silence -tid1=99 tid2=33 tod1=77 tod2=66 -fixuplive=1 -islokmp=1 -specialfile=1 -localname=kinst_1270.exe')
    b = Singleton('stconfig.ini', '-product=duba -isnewitem=1 -itemname=lenovo -tryno=1337 -packettype=exe -packetmodel=silence -tid1=99 tid2=33 tod1=77 tod2=66 -fixuplive=1 -islokmp=1 -specialfile=1 -localname=kinst_1270.exe')
    print(os.getcwd())
    # print a.makepackage_thread()
    # a.stop_makepackage()
    a.makepackage_thread()
    a.stop_makepackage()
    print 'product:'
    print a.getArgvByName('product')
    time.sleep(5)
    print('end')
    b.makepackage_thread()
    time.sleep(50)
    b.stop_makepackage()
    # print id(b)
    # print b.makepackage_thread()
    b.stop_makepackage()
    # assert id(a) == id(b)
    a.resetworking()
