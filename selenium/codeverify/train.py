# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-05
# Author:  pangjian
from selenium import webdriver
from oppo_config import URL
import time
from PIL import Image
import os


def getimg():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(URL)
    for i in range(0, 500):
        driver.save_screenshot(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
        im = Image.open(r'd:\kuaipan\python\autopublishpackage\script\image1.png')
        # box = (390,390,490,430)
        box = (320,240,420,280)
        region = im.crop(box)
        codeimgpath = os.path.join(r'd:\kuaipan\python\autopublishpackage\script\img', str(i)+'.png')
        print(codeimgpath)
        region.save(codeimgpath)
        driver.find_element_by_xpath("//a[@class='captcha-handler']").click()
        time.sleep(0.1)




if __name__=='__main__':
    getimg()
