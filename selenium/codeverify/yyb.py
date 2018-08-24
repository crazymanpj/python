# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-11
# Author:  pangjian
from yyb_config import URL,USERNAME,PASSWORD, UPDATE_URL,CHANNELNO,UPDATE_SHARE_URL, CHANNELNO_SHARE, CHANNELNO_GW
from gobal_config import IS_UPDATE_TEXT
from const import TEXTFIlEPATH, AU3PATH, BANNEDWORD, APPNAME, ERROR_WRONG_UPDATE_URL
from selenium import webdriver
from selenium.common.exceptions import WebDriverException,NoSuchElementException, StaleElementReferenceException
import sys,time,os
from lib import mystr, log, androidhelper
import traceback
from packagePubMarket import PackagePubMarket

class YYB(PackagePubMarket):

    def init(self):
        self.logger = log.Log('log/yyb.txt')
        self.packagePath = self.getFilePathInDir(self.getPackageName())
        self.logger.outMsg(self.packagePath)
        self.packagePathShare = self.getFilePathInDir(self.getPackageNameShare())
        self.logger.outMsg(self.packagePathShare)

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
        self.logger.outMsg(title)
        if title.decode('utf-8') == APPNAME:
            ret = True
        else:
            ret = False
        return ret

    def isCorretUpdaateUrl_share(self):
        appName = self.driver.find_element_by_xpath("//div[@class='app-name-wrap']/h3[1]")
        title = appName.text.encode('utf-8')
        self.logger.outMsg(title)
        if title.decode('utf-8') == APPNAME:
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
        time.sleep(3)
        uploadbutton = self.driver.find_element_by_xpath("//div[@class='add-pic-ing']")
        while uploadbutton.is_displayed() != False:
            self.logger.outMsg('上传中，请等待...')
            time.sleep(2)

        self.logger.outMsg('上传完成，已成功')

    def uploadPackage_share(self):
        time.sleep(5)
        self.driver.switch_to_frame(self.driver.find_element_by_id('ifm-ability'))
        self.driver.find_element_by_link_text('我要修改').click()
        self.driver.switch_to.parent_frame()
        self.logger.outMsg('wait')
        time.sleep(10)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//div[@class='main-content'][1]/iframe[1]"))
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

    def uploadPackage_loop(self):
        self.uploadPackage_bychannel()
        # try:
        #     self.uploadPackage_bychannel()
        # except NoSuchElementException as e:
        #     self.logger.outMsg('uploadPackage_loop try refresh')
        #     time.sleep(5)
        #     self.uploadPackage_loop()

    def uploadPackage_bychannel(self):
        packagePath = ''
        self.logger.outMsg('UPDATE_SHARE_URL')
        self.driver.get(UPDATE_SHARE_URL)
        if self.isCorretUpdaateUrl_share() == False:
            self.logger.outError(self.name + '\n' + ERROR_WRONG_UPDATE_URL, True)
            sys.exit()
        #test
        time.sleep(5)
        self.driver.switch_to_frame(self.driver.find_element_by_id('ifm-ability'))
        self.driver.find_element_by_link_text('我要修改').click()
        self.driver.switch_to.parent_frame()
        self.logger.outMsg('wait')
        time.sleep(10)
        self.driver.switch_to_frame(self.driver.find_element_by_xpath("//div[@class='main-content'][1]/iframe[1]"))
        table1 = self.driver.find_element_by_class_name('myapp-mod-upload-contianer')
        table_rows = table1.find_elements_by_tag_name('tr')
        self.logger.outMsg('table_rows: ')
        self.logger.outMsg(len(table_rows))
        if len(table_rows) <= 0:
            self.logger.outError('获取tr个数失败，退出...', True)
            sys.exit()

        for i in range(1, len(table_rows) + 1):
            channel = self.driver.find_element_by_xpath("//tbody[@id='channelpkg-list']/tr[%s]/td[1]"%(str(i)))

            if channel.text.find('800003') >= 0:
                self.logger.outMsg('800003')
                self.logger.outMsg('channel: ' + channel.text)
                packagePath = self.getFilePathInDir(self.getPackageNameByChannelNo(CHANNELNO_GW))
                uploadButton = self.driver.find_element_by_xpath("//tbody[@id='channelpkg-list']/tr[%s]/td[5]/div[3]/span[1]/div[2]/input[1]"%(str(i)))
                time.sleep(2)
                uploadButton.send_keys(packagePath)
                self.logger.outMsg('upload success 800003')
                self.waitforfinish()
            elif channel.text.find('800036') >= 0:
                self.logger.outMsg('800036')
                self.logger.outMsg('channel: ' + channel.text)
                packagePath = self.getFilePathInDir(self.getPackageNameByChannelNo(CHANNELNO_SHARE))
                uploadButton = self.driver.find_element_by_xpath("//tbody[@id='channelpkg-list']/tr[%s]/td[5]/div[3]/span[1]/div[2]/input[1]"%(str(i)))
                time.sleep(2)
                uploadButton.send_keys(packagePath)
                self.logger.outMsg('upload success 800036')
                self.waitforfinish()

            time.sleep(0.5)


    def waitforfinish(self):
            time.sleep(2)
            try:
                uploadBar = self.driver.find_element_by_class_name('upload-progress-val')
                while uploadBar.is_displayed() == True:
                    self.logger.outMsg('上传中，请等待')
                    time.sleep(2)
            except StaleElementReferenceException as e:
                time.sleep(3)
                self.driver.find_element_by_class_name('aui_state_highlight').click()
                self.logger.outMsg('上传完成')

    def updateText(self):
        self.logger.outMsg('需要更新文案')
        text = self.readtextfromfile()
        self.filterText(text)
        textarea = self.driver.find_element_by_name('update_des')
        textarea.clear()
        textarea.send_keys(text.decode())

    def commit(self):
        self.logger.outMsg('commit')
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

    def getPackageNameByChannelNo(self, channelno):
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + channelno

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
                self.logger.outMsg(ERROR_WRONG_UPDATE_URL)

            self.verifyVersionCode()
            self.uploadPackage()
            time.sleep(3)
            if IS_UPDATE_TEXT == True:
                self.updateText()

            time.sleep(3)
            self.commit()

            self.WaitReview()
            # update share link
            self.uploadPackage_loop()
            # self.uploadPackage_share()

            time.sleep(20)
            self.logger.outMsg('发布结束')

        except WebDriverException as e:
            self.logger.outError(self.name + '\n' + 'selenium error: ' + str(e), True)
            time.sleep(20)
            sys.exit()

if __name__ == '__main__':
    yyb = YYB(URL)
    yyb.publishPackage()
    yyb.uninit()
