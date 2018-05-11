# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-04-20
# Author:  pangjian
from oppo_config import URL, UPDATEURL, PACKAGEPAtH, AU3PATH, PACKAGEMD5,IS_UPDATE_TEXT, TEXTFIlEPATH, BANNEDWORD, ONEWORD
from selenium import webdriver
from PIL import Image
import sys,time
from lib.verifybreak import VerifyBreak
from selenium.common.exceptions import NoSuchElementException
import os
from lib import commonlib



def isLogInSuccess(driver):
    print 'isLogInSuccess...'
    try:
        cjyy = driver.find_element_by_xpath("//input[@class='form-control search']")
        ret = True
    except NoSuchElementException as e:
        ret = False

    print ret
    return ret

def resetverifycode(driver):
    print 'resetverifycode'
    driver.find_element_by_xpath("//a[@class='captcha-handler']").click()
    time.sleep(2)
    driver.save_screenshot(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
    im = Image.open(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
    box = (390,460,490,500)
    region = im.crop(box)
    codeimgpath = r'd:\kuaipan\python\autopublishpackage\script\image2.png'
    region.save(codeimgpath)
    vb = VerifyBreak(codeimgpath)
    verifycode = vb.getverifycode()
    print 'verifycode: ' + verifycode
    return verifycode

def login(driver, username, password, verifycode):
    k_username = driver.find_element_by_name('userName')
    k_username.send_keys(username)
    k_password = driver.find_element_by_name('password')
    k_password.send_keys(password)
    time.sleep(1)
    k_verifycode = driver.find_element_by_name('verifyCode')
    k_verifycode.send_keys(verifycode)

def resetdialog(driver):
    print 'resetdialog'
    k_username = driver.find_element_by_name('userName')
    k_username.clear()
    k_password = driver.find_element_by_name('password')
    k_password.clear()
    time.sleep(0.5)
    k_verifycode = driver.find_element_by_name('verifyCode')
    k_verifycode.clear()

def callloginloop(driver, username, password, verifycode, looptimes):
    for i in range(0, looptimes):
        print 'login fail, retry...'
        resetdialog(driver)
        time.sleep(1)
        verifycode = resetverifycode(driver)
        print verifycode
        time.sleep(2)
        login(driver, username, password, verifycode)
        time.sleep(2)
        if isLogInSuccess(driver) == True:
            return True,i
        else:
            continue
    return False

def iscorrectupdateurl(driver):
    print 'iscorrectupdateurl'
    print driver.current_url
    title_span = driver.find_element_by_xpath("//td[@class='text-top']/span[1]")
    title = title_span.text
    print title
    if title == u'':
        ret = True
    else:
        ret = False

    print ret
    return ret

def isneedupdatesamever(driver):
    print 'isneedupdatesamever...'
    try:
        ljsq = driver.find_element_by_xpath("//a[@class='error-tip-operation']")
        if ljsq.text == '立即申请':
            ret = True
        else:
            ret = False
    except NoSuchElementException as e:
        ret = False

    print ret
    return ret

def readtextfromfile():
    try:
        file = open(TEXTFIlEPATH, 'r')
        text = file.read()
    except:
        print 'read file error'
    finally:
        file.close()
    print text
    return text

def filterText(text):
    for i in BANNEDWORD:
        if text.find(i) != -1:
            print '不允许更新该文案：' + i
            sys.exit(0)

def commit(driver):
    print 'commit'
    # driver.find_element_by_id('auditbutton').click()
    pass

def updatesamever(driver):
    print 'updatesamever...'

def updatenormal(driver):
    print 'updatenormal'
    if IS_UPDATE_TEXT == True:
        print '需要更新文案'
        text = readtextfromfile()
        filterText(text)
        textarea = driver.find_element_by_name('update_desc')
        textarea.clear()
        textarea.send_keys(text.decode())
        commit(driver)
    else:
        commit(driver)


if __name__ == '__main__':
    # text = readtextfromfile()
    # filterText(text)
    # sys.exit(0)
    driver = webdriver.Chrome()
    try:
        driver.get(URL)
    except:
        print 'selenium error'
        sys.exit()

    # k_username = driver.find_element_by_name('userName')
    # k_username.send_keys('guominmin@conew.com')
    # k_password = driver.find_element_by_name('password')
    # k_password.send_keys('CMCM2016!')
    # time.sleep(20)
    # driver.get(UPDATEURL)
    # time.sleep(2)
    # print iscorrectupdateurl(driver)
    # sys.exit(0)
    codeImg = driver.find_element_by_xpath("//img[@class='captcha-img']")
    print codeImg.get_attribute('src')
    sys.exit()

    driver.save_screenshot(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
    im = Image.open(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
    box = (390,390,490,430)
    region = im.crop(box)
    codeimgpath = r'd:\kuaipan\python\autopublishpackage\script\image2.png'
    region.save(codeimgpath)
    vb = VerifyBreak(codeimgpath)
    verifycode = vb.getverifycode()
    login(driver, '', '', verifycode)
    time.sleep(3)

    if isLogInSuccess(driver):
        print '登录成功'
    else:
        print '登录失败'
        ret, trynum = callloginloop(driver, '', '', verifycode, 20)
        if ret == True:
            print '登录成功'
            print '登录次数：' + str(trynum)
        else:
            print '登录失败'
            sys.exit(0)

    driver.get(UPDATEURL)
    time.sleep(5)
    ret = iscorrectupdateurl(driver)
    if ret==False:
        print '不是，退出'
        sys.exit(0)

    driver.find_element_by_xpath("//div[@class='apk-uploader upload-button clickable']").click()
    time.sleep(2)

    try:
        if commonlib.md5_file(PACKAGEPAtH) != PACKAGEMD5:
            print 'md5不一致，发布退出'
    except Exception as e:
        print '文件路径不在，退出'
        driver.quit()
        sys.exit()

    cmd = AU3PATH + ' ' + PACKAGEPAtH
    os.system(cmd)
    time.sleep(10)
    uploadbutton = driver.find_element_by_xpath("//div[@class='apk-uploader upload-button clickable']/span[1]")
    print uploadbutton.text
    while uploadbutton.text != '上传':
        print '上传中，等待...'
        time.sleep(10)

    print '上传完成，已成功'
    time.sleep(5)
    oneword = driver.find_element_by_xpath("//input[@id='oneword']")
    oneword.clear()
    oneword.send_keys(ONEWORD)

    sm = driver.find_element_by_xpath("//textarea[@name='test_desc']")
    sm.clear()
    sm.send_keys(u'无')
    if isneedupdatesamever(driver) == True:
        print '需要同版本更新...'
        updatesamever(driver)
    else:
        print '不需要同版本更新...'
        updatenormal(driver)

    driver.close()
