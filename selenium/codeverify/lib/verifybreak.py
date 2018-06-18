# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-04-21
# Author:  pangjian
from PIL import Image, ImageEnhance
import apiutil
# from singletonexecute import Singleton
import os,sys
sys.path.append('..')
from gobal_config import APP_ID, APP_KEY

class VerifyBreak(object):

    imgpath =''

    def __init__(self, imgpath=''):
        self.imgpath = imgpath

    def imageOpt(self):
        im = Image.open(self.imgpath)
        imgry = im.convert('L')
        sharpness = ImageEnhance.Contrast(imgry)
        sharp_img = sharpness.enhance(2.0)
        sharp_img.save(self.imgpath)

    def getverifycode(self):
        return pytesser.image_file_to_string(self.imgpath)

    def imgToString(self):
        print 'nn'
        # outfile = os.path.join(OUTPUTFILEPATH, 'out.txt')
        # cmd = 'tesseract.exe -psm 7' + ' ' + self.imgpath + ' stdout'
        cmd = 'tesseract.exe' + ' ' + self.imgpath + ' stdout -l code'
        # cmd = 'tesseract.exe' + ' ' + self.imgpath + ' stdout code'
        print cmd
        ret = os.popen(cmd).readlines()
        print ret
        for i in ret:
            if i.find('Error') >= 0 or i.find('Warning') >= 0:
                print i
                continue
            else:
                print 'return'
                print i
                return i
        return ''

    def img_to_string_txai(self):
        f = open(self.imgpath, 'rb')
        img_text = f.read()
        f.close()
        ai_obj = apiutil.AiPlat(APP_ID, APP_KEY)
        rsp = ai_obj.getOcrGeneralocr(img_text)
        if rsp['ret'] == 0:
            for i in rsp['data']['item_list']:
                return i['itemstring']
        else:
            print rsp
            print "获取失败"
            return ''

if __name__ == '__main__':
    codeimgpath = r'd:\kuaipan\python\autopublishpackage\script\image2.png'
    verifybreak = VerifyBreak(codeimgpath)
    print verifybreak.imgToString()
