# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-11
# Author:  pangjian
from yyb_config import URL,USERNAME,PASSWORD, UPDATE_URL,CHANNELNO,UPDATE_SHARE_URL, CHANNELNO_SHARE
from gobal_config import TEXTFIlEPATH, AU3PATH, BANNEDWORD, IS_UPDATE_TEXT
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,NoSuchElementException, StaleElementReferenceException
import sys,time,os
from lib import mystr, log, androidhelper
import traceback
from packagePubMarket import PackagePubMarket

class YYB(PackagePubMarket):

    def init(self):
        self.logger = log.Log('yyb.txt')
        self.packagePath = self.getFilePathInDir(self.getPackageName())
        self.logger.outMsg(self.packagePath)
        self.packagePathShare = self.getFilePathInDir(self.getPackageNameShare())
        self.logger.outMsg(self.packagePathShare)

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

    def isCorretUpdaateUrl_share(self):
        appName = self.driver.find_element_by_xpath("//div[@class='app-name-wrap']/h3[1]")
        title = appName.text.encode('utf-8')
        self.logger.outMsg(title)
        if title.decode('utf-8') == u'':
            ret = True
        else:
            ret = False
        return ret

    def closeNouseWindow(self):
        pass

    def uploadPackage(self):
        time.sleep(5)
        self.driver.find_element_by_xpath("//div[@class='add-pic-after add-file-after']").click()
        time.sleep(2)
        cmd = AU3PATH + ' ' + '"' + self.packagePath + '"'
        self.logger.outMsg(cmd)
        os.system(cmd)
        time.sleep(5)
        uploadbutton = self.driver.find_element_by_xpath("//div[@class='add-pic-ing']")
        while uploadbutton.is_displayed() != False:
            print '上传中，请等待...'
            time.sleep(10)

        print '上传完成，已成功'

    def uploadPackage_share(self):
        time.sleep(5)
        self.driver.switch_to_frame(self.driver.find_element_by_id('ifm-ability'))
        self.driver.find_element_by_link_text('我要修改').click()
        self.driver.switch_to.parent_frame()
        self.logger.outMsg('wait')
        time.sleep(10)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//div[@class='main-content']/iframe[1]"))
        uploadButton = self.driver.find_element_by_xpath("//div[@class='upload-channelpkg-wrapper']/span[1]/div[2]/input[1]")
        time.sleep(2)
        uploadButton.send_keys(self.packagePathShare)
        time.sleep(2)
        try:
            uploadBar = self.driver.find_element_by_class_name('upload-progress-val')
            while uploadBar.is_displayed() == True:
                self.logger.outMsg('上传中，请等待')
                time.sleep(5)
        except StaleElementReferenceException as e:
            time.sleep(3)
            self.driver.find_element_by_class_name('aui_state_highlight').click()
            self.logger.outMsg('上传完成')

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

    def getPackageName(self):
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def getPackageNameShare(self):
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO_SHARE

    def getApkVer(self):
        return androidhelper.getApkVersionCode(apkfilepath=self.packagePath)

    def WaitReview(self):
        title = u'审核中，暂时不能操作'
        time.sleep(5)
        self.driver.get(UPDATE_URL)
        time.sleep(3)
        while title == u'审核中，暂时不能操作':
            self.logger.outMsg('审核中，继续等待...')
            time.sleep(180)
            #超时处理
            try:
                self.driver.get(UPDATE_URL)
                time.sleep(5)
                title = self.driver.find_element_by_xpath("//div[@class='sub-content']/div[1]/div[1]/p[1]").text
            except NoSuchElementException as e:
                self.logger.outMsg('审核通过，继续发布分享渠道...')
                return True

    def publishPackage(self):
        self.logger.outMsg('start')

        try:
            self.driver.get(URL)
            self.driver.maximize_window()
            time.sleep(1)
            self.login(USERNAME, PASSWORD)
            time.sleep(5)
            self.driver.get(UPDATE_URL)
            time.sleep(5)
            if self.iscorretupdateurl() == False:
                print ''

            self.verifyVersionCode()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()

            self.WaitReview()
            #update share link
            self.driver.get(UPDATE_SHARE_URL)
            if self.isCorretUpdaateUrl_share() == False:
                self.logger.outMsg('')
                sys.exit()

            self.uploadPackage_share()
            time.sleep(20)
            self.logger.outMsg('发布结束')

        except WebDriverException as e:
            self.logger.outError('selenium error: ' + str(e))
            time.sleep(200)
            sys.exit()

if __name__ == '__main__':
    yyb = YYB(URL)
    yyb.publishPackage()
    yyb.uninit()
