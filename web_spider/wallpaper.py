#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-05-24
# Author:  pangjian
# version: 1.0

import requests
import urllib
from bs4 import BeautifulSoup
import re
import os

class WallPaper():

    def gethtmltext(self, url):
        ret = requests.get(url)
        print(ret.encoding)
        return ret.text.encode()


    def gethtmltext2(self):
        url = r"http://www.123mobilewallpapers.com/phone/1080x1920"
        ret = urllib.request.urlopen(url)
        print(ret.encoding)
        bsobj = bs4.BeautifulSoup(ret)

    def getwallpaper(self, htmltext):
        pattern = re.compile('src=\S+jpg')
        group1 = pattern.findall(htmltext.decode())
        for i in group1:
            url = i.strip('src="')
            print(url)
            self.savepicturetopath(url, "picture")


    def getnextpageurl(self):
        url = r"http://www.123mobilewallpapers.com/phone/1080x1920/page/"
        i = 1
        while i <=20:
            yield url + str(i)
            i = i + 1

    def getallwallpaper(self):
        for url in self.getnextpageurl():
            self.getwallpaper(self.gethtmltext(url))

    #过滤大小和分辨率
    #多线程下载
    #重试机制
    #防止重复下载
    #文件校验，
    #IO，异步IO

    def savepicturetopath(self, url, path):
        ret = None
        try:
            print("requests get start")
            headers = {"user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
            ret = requests.get(url, headers=headers, timeout=120)
        except Exception as e:
            print("error")
            print(str(e))
            print(url)
        print("requests end")
        if ret != None:
            with open(os.path.join(os.getcwd(), path, os.path.basename(url)),"wb") as f:
                f.write(ret.content)

w = WallPaper()
w.getallwallpaper()