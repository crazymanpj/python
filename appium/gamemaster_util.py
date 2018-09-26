# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-09-26
# Author:  pangjian

def nav_shequ(d):
    d.find_element_by_xpath("//android.widget.RadioButton[@text='社区']").click()

def nav_my(d):
    d.find_element_by_xpath("//android.widget.RadioButton[@text='我的']").click()

def nav_sub_shequ(d):
    d.find_element_by_xpath("//android.widget.TextView[@text='我的社区']").click()
