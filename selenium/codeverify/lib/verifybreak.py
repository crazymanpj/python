# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-04-21
# Author:  pangjian
from PIL import Image, ImageEnhance
import pytesser
from singletonexecute import Singleton
import os
OUTPUTFILEPATH = r'd:\kuaipan\python\autopublishpackage'

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
        outfile = os.path.join(OUTPUTFILEPATH, 'out.txt')
        # cmd = 'tesseract.exe -psm 7' + ' ' + self.imgpath + ' stdout'
        cmd = 'tesseract.exe' + ' ' + self.imgpath + ' stdout -l code'
        # cmd = 'tesseract.exe' + ' ' + self.imgpath + ' stdout code'
        print cmd
        ret = os.popen(cmd).readlines()
        print 'ret:' + str(ret[0])
        return ret[0]



if __name__ == '__main__':
    codeimgpath = r'd:\kuaipan\python\autopublishpackage\script\captcha.png'
    verifybreak = VerifyBreak(codeimgpath)
    print verifybreak.imgToString()
