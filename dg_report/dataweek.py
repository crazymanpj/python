#!/usr/bin/env python
# encoding=utf-8
# Date:    2017-10-27
# Author:  pangjian
# version: 1.1

class DateWeek(object):
    """docstring for DateWeek"""
    def __init__(self, arg=''):
        super(DateWeek, self).__init__()
        self.arg = arg
        self.count = 0
        self.count_weekago = 0

class LbLiucunSub(object):

    def __init__(self, arg=''):
        self.arg = arg

    def setvalue(self, channel, newinst, newuninst_rate, liucun1d_rate, liucun1d_rate_weekd):
        self.channel = channel
        self.newinst = newinst
        self.newuninst_rate = newuninst_rate
        self.liucun1d_rate = liucun1d_rate
        self.liucun1d_rate_weekd = liucun1d_rate_weekd

class LiuCunBasic(object):

    def __init__(self, arg=''):
        self.totalinstall = 0
        self.newuninst = ''
        self.newuninst_rate = ''
        self.newuninst_week_d_rate = ''
        self.liucun1d_rate = ''
        self.liucun7d_rate = ''
        self.liucun1d_rate_weekd = ''
        self.liucun7d_rate_weekd = ''

    def setvalue(self, totalinsall, newuninst, newuninst_rate, newuninst_week_d_rate, liucun1d_rate, liucun7d_rate, liucun1d_rate_weekd, liucun7d_rate_weekd):
        self.totalinstall = totalinsall
        self.newuninst = newuninst
        self.newuninst_rate = newuninst_rate
        self.newuninst_week_d_rate = newuninst_week_d_rate
        self.liucun1d_rate = liucun1d_rate
        self.liucun7d_rate = liucun7d_rate
        self.liucun1d_rate_weekd = liucun1d_rate_weekd
        self.liucun7d_rate_weekd = liucun7d_rate_weekd
