#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-10-17
# Author:  pangjian
# version: 1.0
import os
import helper
from decimal import *
from config import MIN_DISPLAY_COUNT_DAU, DG_PUSH_DUBA_TOD2, MIN_DISPLAY_COUNT_PUSH,LB_PID_DESCRIPTION,DB_CHANNEL_NEW
import mynum

class Dgbase():

	def __init__(self, work_dir=''):
		self.work_dir = work_dir

	def readformatext_sublist(self, work_dir, filename):
		filepath = os.path.join(work_dir, 'config', filename)
		try:
			f = open(filepath, 'r')
			return f.read()
		except:
			print 'open file error'
		finally:
			f.close()

	def formatext_dau_install(self, dgdau, dgi):
		hh = '\n'
		subtemplate = self.readformatext_sublist(self.work_dir, 'dg_sublist.txt')
		subtemplate_short = self.readformatext_sublist(self.work_dir, 'dg_sublist_short.txt')
		subtemplate_long = self.readformatext_sublist(self.work_dir, 'dg_sublist_long.txt')
		reportinstall_nt_sublist = ''
		reportinstall_zd_sublist = ''
		reportdau_zd_sublist = ''

		reportext_dau_zd = dgdau.readformatext(self.work_dir, 'dg_dau_zd.txt').format(dgdau=dgdau)
		reportext_dau_nt = dgdau.readformatext(self.work_dir, 'dg_dau_nt.txt').format(dgdau=dgdau)
		reportext_dgi_zd = dgi.readformatext(self.work_dir, 'dg_install_zd.txt').format(dgi=dgi)
		reportext_dgi_nt = dgi.readformatext(self.work_dir, 'dg_install_nt.txt').format(dgi=dgi)

		# 主动活跃
		for k, v in dgdau.dau_sub_zd_d.items():
			temp = subtemplate.format(k, v)
			reportdau_zd_sublist = reportdau_zd_sublist + temp

		# 主动安装
		for k, v in dgi.install_zd_sub.items():
			temp = subtemplate_short.format(k, v)
			reportinstall_zd_sublist = reportinstall_zd_sublist + temp

		reportext_dgi_zd = reportext_dgi_zd + hh + reportinstall_zd_sublist

		# 内推安装
		for k, v in dgi.install_nt_sub.items():
			temp = subtemplate_short.format(k, v)
			reportinstall_nt_sublist = reportinstall_nt_sublist + temp

		reportext_dgi_nt = reportext_dgi_nt + hh + reportinstall_nt_sublist

		reporttext = reportext_dau_zd + reportdau_zd_sublist + hh + reportext_dau_nt + hh + reportext_dgi_zd + reportext_dgi_nt
		return reporttext

	def formatext_dgpush(self, dgp):
		hh = '\n'
		dgbase = Dgbase()
		subtemplate = dgbase.readformatext_sublist(self.work_dir, 'dg_sublist.txt')
		subtemplate_short = dgbase.readformatext_sublist(self.work_dir, 'dg_sublist_short.txt')
		subtemplate_long = dgbase.readformatext_sublist(self.work_dir, 'dg_sublist_long.txt')
		reportpush_sublist = ''
		reporttext_push = dgp.readformatext(self.work_dir).format(dgp=dgp)

		# 推广
		for k, v in dgp.dgpushduba_sub.items():
			temp = subtemplate_long.format(DG_PUSH_DUBA_TOD2[k], v)
			reportpush_sublist = reportpush_sublist + hh + temp

		reporttext = reporttext_push + reportpush_sublist
		return reporttext

	def formatext_lbliucun(self, lbliucun):
		hh = '\n'
		dgbase = Dgbase()
		subtemplate = dgbase.readformatext_sublist(self.work_dir, os.path.join('lb', 'lb_liucun_sub.txt'))
		reportsublist = ''
		reporttext_lbliucun = lbliucun.readformatext(self.work_dir).format(lbliucun=lbliucun)
		for i in lbliucun.channeltop:
			pid = i.replace('_inst', '', 1)
			newuninst_rate = mynum.getrate_str(lbliucun.newuninst_dict[pid], lbliucun.newinst_dict[i], fh=False)
			try:
				description = LB_PID_DESCRIPTION[i.replace('_inst', '', 1)]
			except KeyError as e:
				description = i.replace('_inst', '', 1)
			temp = subtemplate.format(description, mynum.format_number_ab(lbliucun.newinst_dict[i], dc='0.0'), newuninst_rate, lbliucun.liucun1d_rate_dict[i], lbliucun.liucun1d_rate_weekd_dict[i])
			reportsublist = reportsublist + hh + temp

		reporttext = reporttext_lbliucun + reportsublist
		return reporttext

	def formatext_dbliucun(self, dbliucun):
		hh = '\n'
		dgbase = Dgbase()
		subtemplate = dgbase.readformatext_sublist(self.work_dir, os.path.join('db', 'db_liucun_sub.txt'))
		reportsublist = ''
		reporttext_dbliucun = dbliucun.readformatext(self.work_dir).format(dbliucun=dbliucun)

		for i in dbliucun.channeltop:
			newuninst_rate = mynum.getrate_str(dbliucun.dict_newuninst[i], dbliucun.dict_newinst[i], fh=False)
			description = dbliucun.getchannel_description(i)
			temp = subtemplate.format(description, mynum.format_number_ab(dbliucun.dict_newinst[i], dc='0.0'), newuninst_rate, dbliucun.dict_liucun1d_rate[i], dbliucun.dict_liucun1d_rate_weekd[i])
			reportsublist = reportsublist + hh + temp

		reporttext = reporttext_dbliucun + reportsublist
		return reporttext


class Dgdau(object):
	"""docstring for Dgdau"""
	def __init__(self, arg=''):
		super(Dgdau, self).__init__()
		self.arg = arg
		self.dau = ''
		self.week_d = ''
		self.rate_d = ''
		self.dau_zhudong_hwt = ''
		self.week_d_zd =''
		self.rate_d_zd =''
		self.week_d_nt =''
		self.rate_d_nt =''
		self.dau_neitui = ''
		self.date =''
		self.dau_sub_zd_d = {}

	def setvalue(self, dau, week_d, rate_d, dau_zhudong, dau_neitui, week_d_zd, rate_d_zd, week_d_nt, rate_d_nt, dau_channel_zd_d, dau_channel_tx_d):
		self.dau = mynum.format_number_ab(dau)
		self.week_d = mynum.format_number_ab(week_d, fh=True, dc='0.0')
		self.rate_d = rate_d
		self.dau_zhudong_hwt = mynum.format_number_ab(dau_zhudong)
		self.dau_neitui = mynum.format_number_ab(dau_neitui)
		self.date = helper.get_time_yesterday_f()
		self.week_d_zd = mynum.format_number_ab(week_d_zd, fh=True, dc='0.0')
		self.rate_d_zd = rate_d_zd
		self.week_d_nt = mynum.format_number_ab(week_d_nt, fh=True, dc='0.0')
		self.rate_d_nt = rate_d_nt
		self.dau_zd = mynum.format_number_ab(dau_channel_zd_d, fh=True, dc='0.0')
		self.dau_tx = mynum.format_number_ab(dau_channel_tx_d, fh=True, dc='0.0')

	def formatext(self, work_dir):
		text = self.readformatext(work_dir)
		print text
		for i in text:
			print i

	def readformatext(self, work_dir, filename):
		filepath = os.path.join(work_dir, 'config', filename)
		try:
			f = open(filepath, 'r')
			return f.read()
			# return f.readlines()
		except:
			print 'open file error'
		finally:
			f.close()




class Dginstall(object):
	"""docstring for Dginstall"""
	def __init__(self, arg=''):
		super(Dginstall, self).__init__()
		self.arg = arg
		self.totalinstall = ''
		self.week_d = ''
		self.rate_d = ''
		self.install_zhudong = ''
		self.install_neitui = ''
		self.install_zd_week_d = ''
		self.install_zd_rate = ''
		self.install_nt_week_d = ''
		self.install_nt_rate = ''
		self.install_zd_sub = {}
		self.install_nt_sub={}

	def setvalue(self, totalinstall, week_d, rate_d, install_zhudong, install_zd_week_d, install_zd_rate, install_nt_list, install_zd_sub, install_nt_sub, install_kff, install_kff_rate, install_kff_week_d):
		self.totalinstall = mynum.format_number_ab(totalinstall, dc='0.0')
		self.week_d = mynum.format_number_ab(week_d, fh=True, dc='0.0')
		self.rate_d = rate_d
		self.install_zhudong = mynum.format_number_ab(install_zhudong, dc='0.0')
		self.install_neitui = mynum.format_number_ab(install_nt_list[0], dc='0.0')
		self.install_zd_week_d = mynum.format_number_ab(install_zd_week_d, fh=True, dc='0.0')
		self.install_zd_rate = install_zd_rate
		self.install_nt_week_d = mynum.format_number_ab(install_nt_list[1], fh=True, dc='0.0')
		self.install_nt_rate = install_nt_list[2]
		self.instal_kff = mynum.format_number_ab(install_kff, dc='0.0')
		self.install_kff_rate = install_kff_rate
		self.install_nt_sub = format_dict_dau(install_nt_sub)
		self.install_zd_sub = format_dict_dau(install_zd_sub)
		self.install_kff_week_d = mynum.format_number_ab(install_kff_week_d, fh=True, dc='0.0')

	def readformatext(self, work_dir, filename):
		filepath = os.path.join(work_dir, 'config', filename)
		try:
			f = open(filepath, 'r')
			return f.read()
		except:
			print 'open file error'
		finally:
			f.close()



class Dgpushduba(object):
	"""docstring for Dgpushduba"""
	def __init__(self, arg=''):
		super(Dgpushduba, self).__init__()
		self.arg = arg
		self.dgpushduba = ''
		self.week_d = ''
		self.rate = ''
		self.dgpushduba_sub = {}
		self.push_gw = ''
		self.push_bdp = ''

	def setvalue(self, dgpushduba, week_d, rate, dgpushduba_sub, estimatecount, estimate_weed_d, estimate_rate):
		self.date = helper.get_time_today_f()
		self.dgpushduba = mynum.format_number_ab(dgpushduba, dc='0.0')
		self.week_d = mynum.format_number_ab(week_d, fh=True, dc='0.0')
		self.rate = rate
		self.dgpushduba_sub = dgpushduba_sub
		self.estimatecount = mynum.format_number_ab(estimatecount, dc='0.0')
		self.estimate_weed_d = mynum.format_number_ab(estimate_weed_d, fh=True, dc='0.0')
		self.estimate_rate = estimate_rate

		self.dgpushduba_sub = format_dict_push(self.dgpushduba_sub)

	def readformatext(self, work_dir):
		filepath = os.path.join(work_dir, 'config', u'dg_push.txt')
		try:
			f = open(filepath, 'r')
			return f.read()
		except:
			print 'open file error'
		finally:
			f.close()

class LBliucun(object):

	def __init__(self, arg=''):
		self.arg = arg
		self.date = ''
		self.week = ''
		self.totalinstall = ''
		self.newuninst = ''
		self.newuninst_rate = ''

	def setvalue(self, totalinstall, newuninst, newuninst_rate, week_d_rate,liucun1d_rate, liucun1d_rate_weekd, liucun7d_rate, liucun7d_rate_weekd):
		self.date = helper.get_time_yesterday()
		self.date_f = helper.get_time_yesterday_f()
		self.week = helper.get_weekday(self.date)
		self.totalinstall = mynum.format_number_ab(totalinstall, dc='0.0')
		self.newuninst = mynum.format_number_ab(newuninst, dc='0.0')
		self.newuninst_rate = newuninst_rate
		self.week_d_rate = week_d_rate
		self.liucun1d_rate = liucun1d_rate
		self.liucun1d_rate_weekd = liucun1d_rate_weekd
		self.liucun7d_rate = liucun7d_rate
		self.liucun7d_rate_weekd = liucun7d_rate_weekd
		self.liucun1d_date = helper.get_time_f_bydiff(self.date, 1)
		self.liucun7d_date = helper.get_time_f_bydiff(self.date, 7)
		#分渠道留存
		# self.channeltop5 = []
		# self.newinst_dict = {}
		# self.newuninst_dict = {}
		# self.liucun1d_rate_dict ={}
		# self.liucun1d_rate_weekd_dict = {}

	def readformatext(self, work_dir):
		filepath = os.path.join(work_dir, 'config', 'lb', u'lb_liucun.txt')
		try:
			f = open(filepath, 'r')
			return f.read()
		except:
			print 'open file error'
		finally:
			f.close()


class DBliucun(object):

	def __init__(self, arg=''):
		self.arg = arg

	def setvalue(self, liucunbasic, totalinstall_dif, db_totalinst_d_rate):
		self.date = helper.get_time_yesterday()
		self.date_f = helper.get_time_yesterday_f()
		self.week = helper.get_weekday(self.date)
		self.totalinstall = mynum.format_number_ab(liucunbasic.totalinstall, dc='0.0')
		self.newuninst = mynum.format_number_ab(liucunbasic.newuninst, dc='0.0')
		self.newuninst_rate = liucunbasic.newuninst_rate
		self.week_d_rate = liucunbasic.newuninst_week_d_rate
		self.liucun1d_rate = liucunbasic.liucun1d_rate
		self.liucun1d_rate_weekd = liucunbasic.liucun1d_rate_weekd
		self.liucun7d_rate = liucunbasic.liucun7d_rate
		self.liucun7d_rate_weekd = liucunbasic.liucun7d_rate_weekd
		self.liucun1d_date = helper.get_time_f_bydiff(self.date, 1)
		self.liucun7d_date = helper.get_time_f_bydiff(self.date, 7)
		self.totalinstall_d = mynum.format_number_ab(totalinstall_dif, dc='0.0', fh=True)
		self.totalinstall_d_rate = db_totalinst_d_rate

	def readformatext(self, work_dir):
		filepath = os.path.join(work_dir, 'config', 'db', 'db_liucun.txt')
		try:
			f = open(filepath, 'r')
			return f.read()
		except:
			print 'open file error'
		finally:
			f.close()

	def getchannel_description(self, channeltuple):
		tid1tid2 = str(channeltuple[0]) + '-' + str(channeltuple[1])
		try:
			description = DB_CHANNEL_NEW[tid1tid2]
		except KeyError as e:
			description = tid1tid2

		return description

def format_dict_dau(dict):
	for k, v in dict.items():
		if abs(v) < MIN_DISPLAY_COUNT_DAU:
			del dict[k]
		else:
			dict[k] = mynum.format_number_ab(v, fh=True, dc='0.0')
	return dict

def format_dict_push(dict):
	for k, v in dict.items():
		if abs(v) < MIN_DISPLAY_COUNT_PUSH:
			del dict[k]
		else:
			dict[k] = mynum.format_number_ab(v, fh=True, dc='0.0')
	return dict

if __name__ =='__main__':
	# dgp = Dgpushduba()
	# dgp.setvalue('11', '111', '111', '1111')
	# temp = ['fd', 'see']
	# print readformatext('d:\kuaipan\python\dg_report')
	# test = float(10313607) / float(10000)
	# temp = '0'
	# b = Decimal(test).quantize(Decimal(temp))
	# print b
	lbliucun = LBliucun()
	print lbliucun.readformatext(r'd:\kuaipan\python\dg_report')
