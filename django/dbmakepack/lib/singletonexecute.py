# !/usr/bin/env python
# encoding=utf-8
# Date:    2017-01-09
# Author:  pangjian
# version: 1.0
import threading
from lib import myconfig
# import myconfig_py3
# import myconfig
import os
import time
import subprocess

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
                print('-' *50)
                print('makepackage_thread')
                print(self.getfilepath())
                args = self.getfilepath() + ' ' + self.argvs
                print('*' *50)
                print(args)
                self.handle = subprocess.Popen(args)
                time.sleep(0.1)
            except Exception as e:
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




if __name__ == '__main__':
    a.makepackage_thread()
    a.stop_makepackage()
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
