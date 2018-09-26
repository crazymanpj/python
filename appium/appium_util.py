# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-18
# Author:  pangjian
from appium.webdriver.common.touch_action import TouchAction

def getSize(d):
    x = d.get_window_size()['width']
    y = d.get_window_size()['height']
    return (x, y)

def swipeUp(d):
    l = getSize(d)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.85)   #起始y坐标
    y2 = int(l[1] * 0.25)   #终点y坐标
    d.swipe(x1, y1, x1, y2)
#屏幕向下滑动
def swipeDown(d):
    print 'swipeDown'
    l = getSize(d)
    x1 = int(l[0] * 0.5)  #x坐标
    y1 = int(l[1] * 0.35)   #起始y坐标
    y2 = int(l[1] * 0.85)   #终点y坐标
    d.swipe(x1, y1, x1, y2)
#屏幕向左滑动
def swipLeft(d):
    l=getSize(d)
    x1=int(l[0]*0.85)
    y1=int(l[1]*0.15)
    x2=int(l[0]*0.05)
    d.swipe(x1,y1,x2,y1)
#屏幕向右滑动
def swipRight(d):
    l=getSize(d)
    x1=int(l[0]*0.05)
    y1=int(l[1]*0.15)
    x2=int(l[0]*0.99)
    d.swipe(x1,y1,x2,y1)

def my_longpress(d, element):
    action1 = TouchAction(d)
    action1.long_press(element)
    action1.perform()
