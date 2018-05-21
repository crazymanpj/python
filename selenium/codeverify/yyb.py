# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-11
# Author:  pangjian
from yyb_config import URL,USERNAME,PASSWORD, UPDATE_URL, PACKAGEMD5, PACKAGEPATH, IS_UPDATE_TEXT
from gobal_config import TEXTFIlEPATH, AU3PATH, BANNEDWORD
from selenium import webdriver
from selenium.common.exceptions import RemoteDriverServerException
import sys,time,os
from lib import mystr,commonlib, log
import traceback

logger = log.Log('yyb.txt')

class YYB(object):

    def __init__(self, url):
        self.driver = webdriver.Chrome()
        self.url = url

    #<a class="link" hidefocus="true" id="switcher_plogin" href="javascript:void(0);" tabindex="8">帐号密码登录</a>
    # <input type="text" class="inputstyle" id="u" name="u" value="" tabindex="1">
    #<input type="password" class="inputstyle password" id="p" name="p" value="" maxlength="16" tabindex="2">
    #<input type="submit" tabindex="6" value="登 录" class="btn" id="login_button">
    def login(self, username, password):
        # self.driver.find_element_by_xpath("//div[@id='bottom_qlogin']/a[1]").click()
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//iframe[@id='login_frame']"))
        self.driver.find_element_by_id('switcher_plogin').click()
        k_username = self.driver.find_element_by_id('u')
        k_password = self.driver.find_element_by_id('p')
        login_button = self.driver.find_element_by_id('login_button')
        k_username.send_keys(username)
        k_password.send_keys(password)
        time.sleep(0.5)
        login_button.click()

    def iscorretupdateurl(self):
        appName = self.driver.find_element_by_xpath("//div[@class='app-name-wrap']/h3[1]")
        # print mystr.getstrencodingtype(appName.text.encode('utf-8'))
        title = appName.text.encode('utf-8')
        print title
        if title.decode('utf-8') == u'':
            ret = True
        else:
            ret = False
        return ret


    #<div class="form-col form-col1 txtarea-wrap"><textarea name="update_des" class="ui-txtarea" value="" validate="true" validate_type="empty|length|dirtySensitiveComment" validate_tip="请填写版本更新说明|内容字数为5个汉字以上、500个汉字以内|" maxlen="500" minlen="5" placeholder="5至500字内容"></textarea><div class="form-line" style="padding:0;text-align:right"><em class="tips"></em></div></div>

    def closeNouseWindow(self):
        pass

    def commit(self):
        pass

    def readtextfromfile(self):
        try:
            file = open(TEXTFIlEPATH, 'r')
            text = file.read()
        except:
            print 'read file error'
        finally:
            file.close()
        print text
        return text

    def uploadPackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='add-pic-after add-file-after']").click()
        time.sleep(2)
        cmd = AU3PATH + ' ' + PACKAGEPATH
        os.system(cmd)
        time.sleep(5)
        uploadbutton = self.driver.find_element_by_xpath("//div[@class='add-pic-ing']")
        while uploadbutton.is_displayed() != False:
            print '上传中，请等待...'
            time.sleep(10)

        print '上传完成，已成功'

    def filterText(self, text):
        for i in BANNEDWORD:
            if text.find(i) != -1:
                print '不允许更新该文案：' + i
                sys.exit(0)

    def updateText(self):
        print '需要更新文案'
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_name('update_des')
        textarea.clear()
        textarea.send_keys(text.decode())

    def commit(self):
        print 'commit'
        self.driver.find_element_by_id('j-submit-btn').click()
        time.sleep(3)
        self.driver.find_element_by_id('j-confirm-yes').click()
        time.sleep(20)

    def detailtrace(self):
        """获取程序当前运行的堆栈信息"""
        retStr = ""
        f = sys._getframe()
        f = f.f_back        # first frame is detailtrace, ignore it
        while hasattr(f, "f_code"):
            co = f.f_code
            retStr = "%s(%s:%s)->"%(os.path.basename(co.co_filename),
                    co.co_name,
                    f.f_lineno) + retStr
            f = f.f_back
        return retStr

    def publishPackage(self):
        # try:
        #     ret = 1 / 0
        # except Exception as e:
        #     logger.outError('除0失败: ' + str(e))
        #
        # sys.exit(0)

        try:
            self.driver.get(URL)
            time.sleep(1)
            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(5)
            if self.iscorretupdateurl() == False:
                print ''

            try:
                if commonlib.md5_file(PACKAGEPATH) != PACKAGEMD5:
                    print 'MD5不一致，退出'
                    sys.exit()
            except Exception as e:
                print '文件路径不在，退出'
                self.driver.quit()
                sys.exit()


            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()
        except RemoteDriverServerException as e:
            print str(e)
            print 'selenium error'
            sys.exit()


    def __del__(self):
        print 'close chrome webdriver'
        self.driver.close()



if __name__ == '__main__':
    yyb = YYB(URL)
    yyb.publishPackage()
