# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-06-25
# Author:  pangjian
import time,os
from wostore_config import URL, USERNAME, PASSWORD, CHANNELNO, CORDLEFT, CORDRIGHT
from gobal_config import IS_UPDATE_TEXT
from const import AU3PATH, APPNAME
from selenium import webdriver
from PIL import Image
from lib.verifybreak import VerifyBreak
from selenium.common.exceptions import NoSuchElementException
from packagePubMarket import PackagePubMarket
from lib import log

class WoStore(PackagePubMarket):

    def getPackageName(self):
        return 'cmgamemaster_common_v' + r'\d+' + '_legu_signed_zipalign_sign_cn' + CHANNELNO

    def __init__(self, url):
        try:
            chromeOpitons = webdriver.ChromeOptions()
            prefs = {
            "profile.managed_default_content_settings_images":1,
            "profile.default_content_setting_values.plugins":1,
            "profile.content_settings.plugin_whitelist.adobe-flash-player":1,
            "profile.content_settings.exceptions.plugins.*,*.per_resource.adobe-flash-player":1,
            "credentials_enable_service":False,
            "profile.password_manager_enabled" : False
            }
            chromeOpitons.add_experimental_option('prefs', prefs)
            self.driver = webdriver.Chrome(chrome_options=chromeOpitons)
            self.url = url
            self.logger = log.Log('log/wostore.txt')
            self.packagePath = self.getFilePathInDir(self.getPackageName())
            self.logger.outMsg(self.packagePath)
        except WebDriverException as e:
            print '启动chrome失败，重试中...'
            self.__init__(url)

    # def init(self):
    #     self.logger = log.Log('wostore.txt')
    #     self.packagePath = self.getFilePathInDir(self.getPackageName())
    #     self.logger.outMsg(self.packagePath)

    def isLogInSuccess(self):
        try:
            cjyy = self.driver.find_element_by_link_text("我的社区")
            ret = True
        except NoSuchElementException as e:
            ret = False
        self.logger.outMsg('isLogInSuccess ret is: ' +  str(ret))
        return ret

    def uploadPackage(self):
        time.sleep(5)
        try:
        self.driver.find_element_by_id('nextsave').click()
        except NoSuchElementException as e:
            self.logger.outMsg('不需要第一步')
            pass
        time.sleep(3)
        self.driver.find_element_by_id('i_select_files').click()
        time.sleep(2)
        cmd = AU3PATH + ' ' + '"' + self.packagePath + '"'
        self.logger.outMsg(cmd)
        os.system(cmd)
        time.sleep(5)
        uploadBar = self.driver.find_element_by_id('i_stream_files_queue')
        while uploadBar.is_displayed() != False:
            self.logger.outMsg('上传中，请等待...')
            time.sleep(10)

        self.logger.outMsg('上传完成，已成功')

    # def updateText(self):
    #     self.logger.outMsg('需要更新文案')
    #     text = self.readtextfromfile()
    #     self.filterText(text)

    def commit(self):
        self.logger.outMsg('commit')
        self.driver.find_element_by_id('commit').click()
        time.sleep(20)

    def isCorretUpdateUrl(self):
        name = self.driver.find_elemnt_by_id('cntname')
        title = name.get_attribute('value')
        self.logger.outMsg(title)
        if title == APPNAME:
            ret = True
        else:
            ret = False
        return ret


    def resetverifycode(self):
        self.logger.outMsg('resetverifycode')
        self.driver.find_element_by_class_name('login_code_icon').click()
        time.sleep(2)
        self.driver.save_screenshot(r'screenshots/captcha1.png')
        im = Image.open(r'screenshots/captcha1.png')
        box = (CORDLEFT - 10, CORDRIGHT - 10, CORDLEFT + 81 + 10, CORDRIGHT + 32 + 10)
        region = im.crop(box)
        codeimgpath = r'screenshots/captcha2.png'
        region.save(codeimgpath)

        vb = VerifyBreak(codeimgpath)
        verifycode = vb.img_to_string_txai()
        return verifycode

    def login(self, verifycode):
        k_username = self.driver.find_element_by_id('username')
        k_password = self.driver.find_element_by_id('password')
        k_verifycode = self.driver.find_element_by_id('authcode')

        k_username.send_keys(USERNAME)
        k_password.send_keys(PASSWORD)
        time.sleep(1)
        k_verifycode.send_keys(verifycode)
        time.sleep(1)
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

        self.driver.find_element_by_id('login_sub').click()

    def resetdialog(self):
        self.logger.outMsg('resetdialog')
        k_username = self.driver.find_element_by_id('username')
        k_password = self.driver.find_element_by_id('password')
        k_verifycode = self.driver.find_element_by_id('authcode')
        k_username.clear()
        k_password.clear()
        time.sleep(0.5)
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
            if self.isLogInSuccess() is True:
                return True,i
            else:
                continue
        return False,0

    def fortest(self):
        time.sleep(5)
        self.uninit()
        sys.exit()

    def publishPackage(self):
        self.logger.outMsg('start')
        self.driver.get(URL)
        self.driver.set_window_size(1366,768)
        time.sleep(1)
        self.driver.find_element_by_link_text('登录').click()
        time.sleep(5)

        self.driver.save_screenshot(r'screenshots/f_captcha1.png')
        im = Image.open(r'screenshots/f_captcha1.png')
        box = (CORDLEFT - 5, CORDRIGHT - 5, CORDLEFT + 81 + 5, CORDRIGHT + 32 + 5)
        region = im.crop(box)
        codeimgpath = r'screenshots/f_captcha2.png'
        region.save(codeimgpath)
        vb = VerifyBreak(codeimgpath)
        verifycode = vb.img_to_string_txai()
        self.login(verifycode)
        time.sleep(5)

        if self.isLogInSuccess():
            self.logger.outMsg('登录成功')
        else:
            self.logger.outMsg('登录失败')
            ret, trynum = self.callloginloop(verifycode, 20)
            if ret is True:
                self.logger.outMsg('登录成功' + ' , ' + '登录次数：' + str(trynum))
            else:
                self.logger.outMsg('登录失败')
                sys.exit(-1)

        time.sleep(5)

        self.driver.find_element_by_link_text('我的社区').click()
        time.sleep(3)
        self.driver.find_element_by_id('key').send_keys(u'')
        self.driver.find_element_by_xpath("//div[@class='search_kuang']/a[1]").click()
        time.sleep(3)
        self.driver.find_element_by_link_text('更新').click()
        time.sleep(5)
        self.uploadPackage()
        time.sleep(3)
        self.commit()
        time.sleep(20)
        self.logger.outMsg('登录失败')


if __name__ =='__main__':
    wostore = WoStore(URL)
    wostore.publishPackage()
    wostore.uninit()
