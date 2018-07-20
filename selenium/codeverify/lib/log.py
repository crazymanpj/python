#!/usr/bin/env python
# encoding=utf-8
# Date:    2017-07-19
# Author:  pangjian
# version: 1.1
import logging,os,shutil,sys,datetime,ConfigParser
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#需要发邮件就导入
import mymail, mail_config

class Log():

    def __init__(self, filename, isdebug=False):
        self.filename = filename
        self.isdebug = isdebug
        self.logger = self.initlog()
        self.initlogfile()


    def initlog(self):
        result_filename=self.filename
        logger = logging.getLogger()
        f_logger = logging.FileHandler(result_filename)
        format = logging.Formatter('[%(levelname)s]:%(message)s')
        f_logger.setFormatter(format)
        logger.addHandler(f_logger)
        logger.setLevel(logging.INFO)
        return logger

    def outMsg(self, text):
        if self.isdebug == False:
            # self.logger.info(text)
            self.log(text)
        else:
            print(text)

    def outError(self, text, is_send_mail= False):
        if self.isdebug == False:
            # self.logger.error(text)
            self.log(text)
            self.log(traceback.format_exc())

            if is_send_mail:
                content = ''
                if traceback:
                    content = text + '\n' + traceback.format_exc() + '\n'
                else:
                    content = text + '\n'
                ret = mymail.send_mail(mail_config.MAILTO_LIST, mail_config.MAIL_ERROR_TITLE, content)
                if ret[0] is False:
                    self.log(mail_config.SEND_MAIL_ERROR + ret[1])
        else:
            print(text)

    def log(self, text):
        time =  datetime.datetime.now()
        text = str(time) + ":    " + str(text) + "\n"
        logfile = open(self.filename, "a+")
        logfile.write(text)
        logfile.close()

    def initlogfile(self):
        logfile = open(self.filename, "a+")
        logfile.write("\r\n")
        logfile.write("==============================" + os.path.splitext(self.filename)[0] + "   start ===============================" + "\r\n")
        # logfile.write("==============================makedata   start ===============================" + "\r\n")
        logfile.close()
