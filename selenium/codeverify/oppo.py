# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-04-20
# Author:  pangjian
import sys,time
from oppo_config import URL, UPDATEURL, ONEWORD, USERNAME, PASSWORD, CHANNELNO
from gobal_config import TEXTFIlEPATH, AU3PATH, BANNEDWORD, IS_UPDATE_TEXT
from selenium import webdriver
from PIL import Image
from lib.verifybreak import VerifyBreak
from selenium.common.exceptions import NoSuchElementException
import os,requests
from packagePubMarket import PackagePubMarket
from lib import log

class OPPO(PackagePubMarket):

    def init(self):
        self.logger = log.Log('oppo.txt')
        self.packagePath = self.getFilePathInDir(self.getPackageName())
        self.logger.outMsg(self.packagePath)

    def getPackageName(self):
        return 'cmgamemaster_oppo_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def isLogInSuccess(self):
        self.logger.outMsg('isLogInSuccess...')
        try:
            cjyy = self.driver.find_element_by_xpath("//input[@class='form-control search']")
            ret = True
        except NoSuchElementException as e:
            ret = False

        return ret

    def resetverifycode(self):
        self.logger.outMsg('resetverifycode')
        self.driver.find_element_by_xpath("//a[@class='captcha-handler']").click()
        time.sleep(2)
        self.driver.save_screenshot(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
        im = Image.open(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
        # box = (390,460,490,500)
        box = (386,466,476,496)
        region = im.crop(box)
        codeimgpath = r'd:\kuaipan\python\autopublishpackage\script\image2.png'
        region.save(codeimgpath)
        # time.sleep(500)
        vb = VerifyBreak(codeimgpath)
        verifycode = vb.getverifycode()
        self.logger.outMsg('verifycode: ' + verifycode)
        return verifycode

    def login(self,verifycode):
        k_username = self.driver.find_element_by_name('userName')
        k_password = self.driver.find_element_by_name('password')
        k_username.send_keys(USERNAME)
        k_password.send_keys(PASSWORD)
        time.sleep(1)
        k_verifycode = self.driver.find_element_by_name('verifyCode')
        k_verifycode.send_keys(verifycode)

    def resetdialog(self):
        self.logger.outMsg('resetdialog')
        k_username = self.driver.find_element_by_name('userName')
        k_username.clear()
        k_password = self.driver.find_element_by_name('password')
        k_password.clear()
        time.sleep(0.5)
        k_verifycode = self.driver.find_element_by_name('verifyCode')
        k_verifycode.clear()

    def callloginloop(self, verifycode, looptimes):
        for i in range(0, looptimes):
            self.logger.outMsg('login fail, retry...')
            self.resetdialog()
            time.sleep(1)
            verifycode = self.resetverifycode()
            self.logger.outMsg(verifycode)
            time.sleep(2)
            self.login(verifycode)
            time.sleep(2)
            if self.isLogInSuccess() == True:
                return True,i
            else:
                continue
        return False,0

    def iscorrectupdateurl(self):
        title_span = self.driver.find_element_by_xpath("//td[@class='text-top']/span[1]")
        title = title_span.text
        self.logger.outMsg(title)
        if title == u'':
            ret = True
        else:
            ret = False

        self.logger.outMsg(ret)
        return ret

    def isneedupdatesamever(self):
        self.logger.outMsg('isneedupdatesamever...')
        try:
            ljsq = self.driver.find_element_by_xpath("//a[@class='error-tip-operation']")
            if ljsq.text == '立即申请':
                ret = True
            else:
                ret = False
        except NoSuchElementException as e:
            ret = False

        self.logger.outMsg(ret)
        return ret

    def commit(self):
        self.logger.outMsg('commit')
        self.driver.find_element_by_id('auditbutton').click()
        time.sleep(20)

    def updatesamever(self):
        self.logger.outMsg('updatesamever...')
        self.driver.find_element_by_link_text('立即申请').click()
        time.sleep(2)
        textarea = self.driver.find_element_by_name('update_reason')
        textarea.send_keys('修复bug')
        time.sleep(1)
        self.driver.find_elemnt_by_id('button').click()

        time.sleep(3)
        self.driver.find_element_by_xpath("//div[@class='apk-uploader upload-button clickable']").click()
        time.sleep(2)

        cmd = AU3PATH + ' ' + self.packagePath
        os.system(cmd)
        time.sleep(10)
        uploadbutton = self.driver.find_element_by_xpath("//div[@class='apk-uploader upload-button clickable']/span[1]")
        self.logger.outMsg(uploadbutton.text)
        while uploadbutton.text != '上传':
            self.logger.outMsg('上传中，等待...')
            time.sleep(10)

        self.logger.outMsg('上传完成，已成功')
        time.sleep(5)
        updatenormal()

    def updatenormal(self):
        self.logger.outMsg('updatenormal')
        if IS_UPDATE_TEXT == True:
            self.logger.outMsg('需要更新文案')
            text = self.readtextfromfile()
            self.filterText(text)
            textarea = self.driver.find_element_by_name('update_desc')
            textarea.clear()
            textarea.send_keys(text.decode())
            self.commit()
        else:
            self.commit()

    def downloadImg(self):
        f_handle = None
        codeImg = self.driver.find_element_by_xpath("//img[@class='captcha-img']")
        url = codeImg.get_attribute('src')
        self.logger.outMsg(url)
        try:
            r = requests.get(url, verify = False)
            f_handle = open('codeImg.png', 'wb')
            f_handle.write(r.content)
            self.logger.outMsg('donwload codeimg ok')
        except Exception as e:
            self.logger.outError('download codeimg fail' + str(e))
        finally:
            f_handle.close()

    def publishPackage(self):
        self.logger.outMsg('start')
        self.driver.get(URL)

        self.driver.save_screenshot(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
        im = Image.open(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
        # box = (390,390,490,430)
        box = (387,396,477,426)
        region = im.crop(box)
        codeimgpath = r'd:\kuaipan\python\autopublishpackage\script\image2.png'
        region.save(codeimgpath)
        vb = VerifyBreak(codeimgpath)
        verifycode = vb.getverifycode()
        self.login(verifycode)
        time.sleep(3)

        if self.isLogInSuccess():
            self.logger.outMsg('登录成功')
        else:
            self.logger.outMsg('登录失败')
            ret, trynum = self.callloginloop(verifycode, 20)
            if ret == True:
                self.logger.outMsg('登录成功')
                self.logger.outMsg('登录次数：' + str(trynum))
            else:
                self.logger.outMsg('登录失败')
                sys.exit(0)

        self.driver.get(UPDATEURL)
        time.sleep(5)
        ret = self.iscorrectupdateurl()
        if ret==False:
            self.logger.outMsg('')
            sys.exit(0)

        self.driver.find_element_by_xpath("//div[@class='apk-uploader upload-button clickable']").click()
        time.sleep(2)

        self.verifyVersionCode()

        cmd = AU3PATH + ' ' + self.packagePath
        os.system(cmd)
        time.sleep(10)
        uploadbutton = self.driver.find_element_by_xpath("//div[@class='apk-uploader upload-button clickable']/span[1]")
        self.logger.outMsg(uploadbutton.text)
        while uploadbutton.text != '上传':
            self.logger.outMsg('上传中，等待...')
            time.sleep(10)

        self.logger.outMsg('上传完成，已成功')
        time.sleep(5)
        oneword = self.driver.find_element_by_xpath("//input[@id='oneword']")
        oneword.clear()
        oneword.send_keys(ONEWORD)

        sm = self.driver.find_element_by_xpath("//textarea[@name='test_desc']")
        sm.clear()
        sm.send_keys(u'无')

        self.driver.find_element_by_id('radios-5').click()

        if self.isneedupdatesamever() == True:
            self.logger.outMsg('需要同版本更新...')
            self.updatesamever()
        else:
            self.logger.outMsg('不需要同版本更新...')
            self.updatenormal()


if __name__ == '__main__':
    oppo = OPPO(URL)
    oppo.publishPackage()
    #结束操作
    oppo.uninit()
