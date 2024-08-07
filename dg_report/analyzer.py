#encoding=utf-8
# Date:    2017-10-10
# Author:  pangjian
# version: 1.0

from sql import Sql
import helper
from formater import Dgdau, Dgpushduba, Dginstall, Dgbase, LBliucun, DBliucun
from config import DG_PUSH_DUBA_TOD2, LB_MAX_REPORT_COUNT, LB_FILTER_BY_INST, LB_PID_FIXED, DB_FILTER_BY_INSTOP,DB_CHANNEL_FIXED
from dataweek import DateWeek, LiuCunBasic
from log import Log
import os,sys
from sendmsg import sendwxmsg, getidandsender
from exceptions import KeyError
import mynum
from datanalyzer import Datanalyzer
from config import DB_MAX_REPORT_COUNT,DB_CHANNEL_NEW

class Analyzer(object):
	"""docstring for Analyzer"""
	def __init__(self, work_dir=''):
		super(Analyzer, self).__init__()
		self.work_dir = work_dir
		self.logger = Log(os.path.join(self.work_dir, 'log', 'dg_report.txt'))
		self.logger.outMsg(self.work_dir)

	def get_estimatedgpush(self, hourtime):
		s = Sql(helper.get_time_today())
		s_weekago = Sql(helper.get_time_weekago_today())
		count = s.get_dg_push_duba(hour=hourtime)
		count_b = s_weekago.get_dg_push_duba(hour=hourtime)
		count_all_b = s_weekago.get_dg_push_duba()
		week_d = count - count_b
		rate = round(float(week_d) / float(count_b), 2)
		estimatecount = float(count_all_b) * (1 + rate)
		estimate_weed_d = estimatecount - float(count_all_b)
		estimate_rate = mynum.getrate_str(float(estimate_weed_d), float(count_all_b))
		return estimatecount, estimate_weed_d, estimate_rate

	def get_estimatedgpush_sub(self, hourtime):
		ret = {}
		sub = {}
		sub_b = {}
		dgpushdb = Sql(helper.get_time_today())
		dgpushdb_b = Sql(helper.get_time_weekago_today())

		sub_hour = dgpushdb.get_dg_push_duba_bychannel(hour=hourtime)
		sub_hour_b = dgpushdb_b.get_dg_push_duba_bychannel(hour=hourtime)
		sub_b = dgpushdb_b.get_dg_push_duba_bychannel()
		for k, v in sub_hour.items():
			week_d = sub_hour[k] - sub_hour_b[k]
			rate = round(float(week_d) / float(sub_hour_b[k]), 2)
			estimatecount = float(sub_b[k]) * (1 + rate)
			estimate_week_d = estimatecount - float(sub_b[k])
			ret[k] = estimate_week_d
		return ret

	def get_estimatedgpush2(self, hourtime):
		s = Sql(helper.get_time_today())
		s_weekago = Sql(helper.get_time_weekago_today())
		count = s.get_dg_push_duba(hour=hourtime)
		count_b = s_weekago.get_dg_push_duba(hour=hourtime)
		count_all_b = s_weekago.get_dg_push_duba()
		week_d = count - count_b
		incre = float(count_all_b) - float(count_b)
		# rate = round(incre / float(count_b), 2)
		rate = mynum.float_decimal2(incre / float(count_b), fh=True)
		estimatecount = float(count) + float(count) * rate
		estimate_weed_d = estimatecount - float(count_all_b)
		estimate_rate = mynum.getrate_str(float(estimate_weed_d), float(count_all_b))
		return estimatecount, estimate_weed_d, estimate_rate

	def get_estimatedgpush_sub2(self, hourtime):
		ret = {}
		sub = {}
		sub_b = {}
		dgpushdb = Sql(helper.get_time_today())
		dgpushdb_b = Sql(helper.get_time_weekago_today())

		sub_hour = dgpushdb.get_dg_push_duba_bychannel(hour=hourtime)
		sub_hour_b = dgpushdb_b.get_dg_push_duba_bychannel(hour=hourtime)
		sub_b = dgpushdb_b.get_dg_push_duba_bychannel()
		for k, v in sub_hour.items():
			week_d = sub_hour[k] - sub_hour_b[k]
			incre = float(sub_b[k]) - float(sub_hour_b[k])
			# rate = round(incre / float(sub_hour_b[k]), 2)
			rate = mynum.float_decimal2(incre / float(sub_hour_b[k]), fh=True)
			estimatecount = float(sub_hour[k]) + float(sub_hour[k]) * rate
			estimate_week_d = estimatecount - float(sub_b[k])
			ret[k] = estimate_week_d
		return ret

	def getweek_d(self, type, daytype='yesterday'):
		count = 0
		count_b = 0
		week_d = 0
		if daytype == 'yesterday':
			s = Sql(helper.get_time_yesterday())
			s_weekago = Sql(helper.get_time_weekago_yesterday())
		elif daytype == 'today':
			s = Sql(helper.get_time_today())
			s_weekago = Sql(helper.get_time_weekago_today())

		if type == 'dau':
			count = s.get_dau()
			count_b = s_weekago.get_dau()
			week_d = count - count_b
			return count, count_b, week_d

		elif type == 'install':
			count = s.get_totalinstall()
			count_b = s_weekago.get_totalinstall()
			week_d = count - count_b
			return count, count_b, week_d

		elif type == 'install_zd':
			count = s.get_install_zd()
			count_b = s_weekago.get_install_zd()
			week_d = count - count_b
			return count, count_b, week_d

		elif type == 'install_nt':
			count = s.get_install_nt()
			count_b = s_weekago.get_install_nt()
			week_d = count - count_b
			return count, count_b, week_d

		elif type == 'dgpushdb':
			count = s.get_dg_push_duba()
			count_b = s_weekago.get_dg_push_duba()
			week_d = count - count_b
			return count, count_b, week_d

		elif type == 'lb_newuninst':
			totalinstall = s.get_lb_newinst_total()
			totalinstall_b = s_weekago.get_lb_newinst_total()
			newuninst = s.get_lb_newuninst()
			newuninst_b = s_weekago.get_lb_newuninst()
			return totalinstall, newuninst, totalinstall_b, newuninst_b

		elif type == 'db_newinst_uninst':
			totalinstall = s.get_db_newinst_total()
			totalinstall_b = s_weekago.get_db_newinst_total()
			newuninst = s.get_db_newuninst_bytid('all', 'all')
			newuninst_b = s_weekago.get_db_newuninst_bytid('all', 'all')
			return totalinstall, newuninst, totalinstall_b, newuninst_b

	def getdau_week_d_sub(self):
		ret_zd = {}
		dataweek_zd = DateWeek()
		dataweek_nt = DateWeek()
		dau_sub = Sql(helper.get_time_yesterday())
		dau_sub_week_d = Sql(helper.get_time_weekago_yesterday())
		sub_zd, sub_nt = dau_sub.get_dau_bychannel()
		sub_zd_b, sub_nt_b = dau_sub_week_d.get_dau_bychannel()
		dataweek_zd.count = sub_zd['主动安装渠道'] + sub_zd['腾讯视频渠道']
		dataweek_zd.count_weekago = sub_zd_b['主动安装渠道'] + sub_zd_b['腾讯视频渠道']

		for k,v in sub_nt.items():
			dataweek_nt.count = v
			dataweek_nt.count_weekago = sub_nt_b[k]

		return dataweek_zd,dataweek_nt, sub_zd['主动安装渠道'] - sub_zd_b['主动安装渠道'], sub_zd['腾讯视频渠道'] - sub_zd_b['腾讯视频渠道']

	def getdgpushdb_sub(self):
		ret = {}
		sub = {}
		sub_b = {}
		dgpushdb = Sql(helper.get_time_today())
		dgpushdb_b = Sql(helper.get_time_weekago_today())
		sub = dgpushdb.get_dg_push_duba_bychannel()
		sub_b = dgpushdb_b.get_dg_push_duba_bychannel()
		for k,v in sub.items():
			ret[k] = v - sub_b[k]
		return sub, sub_b, ret

	def getinstallzd_sub(self):
		ret = {}
		dataweek_kff = DateWeek()
		install_zd = Sql(helper.get_time_yesterday())
		install_zd_b = Sql(helper.get_time_weekago_yesterday())

		sub = install_zd.get_install_zd_bychannel()
		sub_b = install_zd_b.get_install_zd_bychannel()
		for k,v in sub.items():
			ret[k] = v - sub_b[k]

		install_kff = install_zd.get_install_kff()
		install_kff_b = install_zd_b.get_install_kff()
		dataweek_kff.count = install_kff
		dataweek_kff.count_weekago = install_kff_b
		return ret, dataweek_kff

	def getinstallnt_sub(self):
		ret={}
		install_nt = Sql(helper.get_time_yesterday())
		install_nt_b = Sql(helper.get_time_weekago_yesterday())
		install_xxl_d = install_nt.get_install_xxl() - install_nt_b.get_install_xxl()
		install_xzq_d = install_nt.get_install_xzq() - install_nt_b.get_install_xzq()
		ret['毒霸信息流'] = install_xxl_d
		ret['勋 章 墙'] = install_xzq_d
		return ret

	#主动安装构成
	def get_dau_zhudong_haswt(self, dau_sub):
		return dau_sub['resident_2228'] + dau_sub['resident_zhudong']

	def get_lb_totalinstall(self):
		sql = Sql(helper.get_time_yesterday())
		return sql.get_lb_newuninst()

	def get_lb_liucun1d_rate_all(self):
		# 1日留存最早是前天的
		date_1d = helper.get_time_bydiff(helper.get_time_yesterday(), 1)
		date_1d_weekago = helper.get_time_bydiff(date_1d, 7)
		da = Datanalyzer()
		liucun1d_rate = da.get_lb_1dliucun('all', date_1d)
		liucun1d_rate_b = da.get_lb_1dliucun('all', date_1d_weekago)
		liucun1d_rate_weekd = mynum.float_decimal2((liucun1d_rate - liucun1d_rate_b), fh=True)
		return liucun1d_rate, liucun1d_rate_weekd

	def get_lb_liucun7d_rate_all(self):
		#最早的7日留存为昨天再减7天
		date_7d = helper.get_time_bydiff(helper.get_time_yesterday(), 7)
		date_7d_weekago = helper.get_time_bydiff(date_7d, 7)
		da = Datanalyzer()
		liucun7d_rate = da.get_lb_7dliucun('all', date_7d)
		liucun7d_rate_b = da.get_lb_7dliucun('all', date_7d_weekago)
		liucun7d_rate_weekd = mynum.float_decimal2((liucun7d_rate - liucun7d_rate_b), fh=True)
		return liucun7d_rate, liucun7d_rate_weekd

	def addfixedchannel(self, pidlist):
		for k,v  in LB_PID_FIXED.items():
			if v not in pidlist:
				pidlist.append(v)

		return pidlist

	def addfixedchannel_db(self, channeltuple):
		temp = ()
		temp_super = ()
		for k,v in DB_CHANNEL_FIXED.items():
			if k not in channeltuple:
				temp = temp + k

		if len(temp) > 0:
			temp_super = ((temp),)
			channeltuple = channeltuple + temp_super
			return channeltuple
		else:
			return channeltuple

	def gettopchannel_hasfixed(self, pidlist, topnum, fixed_channel):
		ret = []
		count = 0

		if len(fixed_channel) >= topnum:
			return fixed_channel

		for i in pidlist:
			if i in fixed_channel:
				pidlist.remove(i)

		ret = fixed_channel + pidlist[ : topnum - len(fixed_channel)]
		return ret

	def gettopchannel_hasfixed_db(self, channeltuple, topnum, fixed_channel):
		ret = ()
		count = 0

		if len(fixed_channel) >= topnum:
			return fixed_channel

		for i in channeltuple:
			if i in fixed_channel:
				channeltuple.remove(i)

		ret = fixed_channel + channeltuple[ : topnum - len(fixed_channel)]
		return ret



	def get_lb_liucun_by_channel(self):
		liucun1d_rate_dict = {}
		ret_b = {}
		ret_d = {}
		ret_d_sort = {}
		day_1d = helper.get_time_yesterday()
		day_inst1d = helper.get_time_bydiff(helper.get_time_yesterday(), 1)

		s = Sql(day_1d)
		s_yesterday = Sql(day_inst1d)
		s_weekago = Sql(helper.get_time_bydiff(day_1d, 7))
		s_weekago_yesterday = Sql(helper.get_time_bydiff(day_inst1d, 7))

		dict_lbnewinst = s_yesterday.get_lb_newinst_bychannel()
		# print dict_lbnewinst
		pidlist_top = helper.sortdictbyvalue(dict_lbnewinst)[:LB_FILTER_BY_INST]
		pidlist_top = self.addfixedchannel(pidlist_top)
		# print pidlist_top
		# dict_lbnewuninst = s.get_lb_newuninst_bychannel(pidlist_top)
		dict_lbnewuninst = s_yesterday.get_lb_newuninst_bychannel(pidlist_top)
		dict_liucun1d = s.get_lb_liucun_1d_bychannel(pidlist_top)
		# print '-' * 50
		# print dict_lbnewinst
		# print dict_lbnewuninst
		# print dict_liucun1d
		self.logger.outMsg(dict_lbnewinst)
		self.logger.outMsg(dict_lbnewuninst)
		self.logger.outMsg(dict_liucun1d)

		dict_lbnewinst_b = s_weekago_yesterday.get_lb_newinst_bychannel()
		pidlist_top_b = helper.sortdictbyvalue(dict_lbnewinst_b)[:LB_FILTER_BY_INST]
		pidlist_top_b = self.addfixedchannel(pidlist_top_b)
		dict_liucun1d_b = s_weekago.get_lb_liucun_1d_bychannel(pidlist_top_b)
		# print '-' * 50
		# print dict_lbnewinst_b
		# print dict_liucun1d_b
		for k in pidlist_top:
			temp = k.replace('_inst', '', 1)
			liucun1d_rate_dict[k] = mynum.getrate_float(dict_liucun1d[temp], dict_lbnewinst[k])

			try:
				ret_b[k] = mynum.getrate_float(dict_liucun1d_b[temp], dict_lbnewinst_b[k])
			except KeyError as e:
				ret_b[k] = 0
		# print ret
		# print ret_b

		for i in pidlist_top:
			if i in pidlist_top_b:
				ret_d[i] = mynum.float_decimal2(liucun1d_rate_dict[i] - ret_b[i], fh=True)
				ret_d_sort[i] = abs(mynum.float_decimal2(liucun1d_rate_dict[i] - ret_b[i]))

		# print '-' * 20
		# print ret_d
		# print ret_d_sort
		keylist = helper.sortdictbyvalue(ret_d_sort)
		keylist_final = self.gettopchannel_hasfixed(keylist, LB_MAX_REPORT_COUNT, [x for k, x in LB_PID_FIXED.items()])
		# print keylist
		return keylist_final,dict_lbnewinst, dict_lbnewuninst, liucun1d_rate_dict, ret_d

	def get_lb_newinst_by_channel(self):
		ret = []
		ret_d = {}
		s = Sql(helper.get_time_yesterday())
		s_weekago = Sql(helper.get_time_weekago_yesterday())
		dict_lbnewinst = s.get_lb_newinst_bychannel()
		dict_lbnewinst_b = s_weekago.get_lb_newinst_bychannel()
		for k,v in dict_lbnewinst.items():
			try:
				temp = dict_lbnewinst_b[k]
			except KeyError as e:
				temp = 0
			ret_d[k] = abs(float('%.2f' % (v - temp)))

		ret = helper.sortdictbyvalue(ret_d)
		return ret

	def get_db_liucun_rate_all(self):
		date = helper.get_time_bydiff(helper.get_time_yesterday(), 1)
		date_weekage = helper.get_time_bydiff(helper.get_time_yesterday(), 7)
		da = Datanalyzer()
		liucun1d_rate = da.get_db_1dliucun('all', 'all', date)
		liucun1d_rate_b = da.get_db_1dliucun('all', 'all', date_weekage)
		liucun1d_rate_weekd = mynum.float_decimal2((liucun1d_rate - liucun1d_rate_b), fh=True)

		liucun7d_rate = da.get_db_7dliucun('all', 'all', date_weekage)
		liucun7d_rate_b = da.get_db_7dliucun('all', 'all', helper.get_time_bydiff(date_weekage, 7))
		liucun7d_rate_weekd = mynum.float_decimal2((liucun7d_rate - liucun7d_rate_b), fh=True)
		return liucun1d_rate, liucun1d_rate_weekd, liucun7d_rate, liucun7d_rate_weekd

	def get_db_liucun_by_channel(self):
		liucun1d_rate_dict = {}
		liucun1d_rate_dict_b = {}
		liucun1d_weekd_rate = {}
		liucun1d_weekd_rate_sort = {}

		reportday = helper.get_time_yesterday()
		day_inst1d = helper.get_time_bydiff(helper.get_time_yesterday(), 1)
		day_inst1d_weekago = helper.get_time_bydiff(day_inst1d, 7)

		s = Sql(reportday)
		s_inst1d = Sql(day_inst1d)
		s_inst1d_weekago = Sql(helper.get_time_bydiff(day_inst1d, 7))

		# print '-' * 30
		channel_tuple = s_inst1d.get_db_tid1_and_tid2()[:DB_FILTER_BY_INSTOP]
		# print len(channel_tuple)
		# print channel_tuple
		channelist_top = self.addfixedchannel_db(channel_tuple)
		# print len(channelist_top)
		# print channelist_top
		# print '-' * 30

		dict_dbnewinst = s_inst1d.get_db_newinst_bychannel(channelist_top)
		# print dict_dbnewinst
		dict_dbnewuninst = s_inst1d.get_db_newuninst_bychannel(channelist_top)
		# print dict_dbnewuninst
		# print dict_dbnewuninst
		# for k,v in dict_dbnewuninst.items():
		# 	print k,v

		dict_liucun1d = s_inst1d.get_db_1dliucun_bychannel(day_inst1d, channelist_top)
		# print dict_liucun1d
		# for k,v in dict_liucun1d.items():
		# 	print k,v

		channel_tuple_b = s_inst1d_weekago.get_db_tid1_and_tid2()[:DB_FILTER_BY_INSTOP]
		channelist_top_b = self.addfixedchannel_db(channel_tuple_b)
		dict_dbnewinst_b = s_inst1d_weekago.get_db_newinst_bychannel(channelist_top_b)
		dict_liucun1d_b = s_inst1d_weekago.get_db_1dliucun_bychannel(day_inst1d_weekago, channelist_top_b)

		for i in channelist_top:
			liucun1d_rate_dict[i] = mynum.getrate_float(dict_liucun1d[i], dict_dbnewinst[i])
			try:
				liucun1d_rate_dict_b[i] = mynum.getrate_float(dict_liucun1d_b[i], dict_dbnewinst_b[i])
			except KeyError as e:
				liucun1d_rate_dict_b[i] = 0

		for i in channelist_top:
			if i in channelist_top_b:
				liucun1d_weekd_rate[i] = mynum.float_decimal2(liucun1d_rate_dict[i] - liucun1d_rate_dict_b[i], fh=True)
				liucun1d_weekd_rate_sort[i] = abs(mynum.float_decimal2(liucun1d_rate_dict[i] - liucun1d_rate_dict_b[i]))

		keylist = helper.sortdictbyvalue(liucun1d_weekd_rate_sort)
		keylist_final = self.gettopchannel_hasfixed_db(keylist, DB_MAX_REPORT_COUNT, [k for k,v in DB_CHANNEL_FIXED.items()])
		# print '-' * 30
		# print keylist
		# print '-' * 30
		# print keylist_final
		# print '-' * 30

		return keylist_final, dict_dbnewinst, dict_dbnewuninst, liucun1d_rate_dict, liucun1d_weekd_rate


	def start_analysis_dau(self):
		self.logger.outMsg('start analysis dau...')
		#分析活跃
		dau, dau_b, dau_week_d = self.getweek_d('dau')
		dau_rate = mynum.getrate_str(dau_week_d, dau_b)

		dau_sub_zd, dau_sub_nt, dau_channel_zd_d, dau_channel_tx_d= self.getdau_week_d_sub()
		#主动安装差值
		week_d_zd = dau_sub_zd.count - dau_sub_zd.count_weekago
		dau_zhudong_rate = mynum.getrate_str(week_d_zd, dau_sub_zd.count_weekago)

		#内推安装
		week_d_nt = dau_sub_nt.count - dau_sub_nt.count_weekago
		rate_d_nt = mynum.getrate_str(week_d_nt, dau_sub_nt.count_weekago)

		dgdau = Dgdau()
		dgdau.setvalue(dau, dau_week_d, dau_rate, dau_sub_zd.count, dau_sub_nt.count, week_d_zd, dau_zhudong_rate, week_d_nt, rate_d_nt, dau_channel_zd_d, dau_channel_tx_d)

		self.logger.outMsg('start analysis install...')
		#分析安装
		install, install_b, install_week_d = self.getweek_d('install')
		install_rate = mynum.getrate_str(install_week_d, install_b)

		install_zd, install_zd_b, install_zd_week_d = self.getweek_d('install_zd')
		install_zd_rate = mynum.getrate_str(install_zd_week_d, install_zd_b)

		install_nt, install_nt_b, install_nt_week_d = self.getweek_d('install_nt')
		install_nt_rate = mynum.getrate_str(install_nt_week_d, install_nt_b)
		install_nt_list = [install_nt, install_nt_week_d, install_nt_rate]

		install_zd_sub, dataweek_kff = self.getinstallzd_sub()
		install_kff_week_d = dataweek_kff.count - dataweek_kff.count_weekago
		install_kff_rate = mynum.getrate_str(install_kff_week_d, dataweek_kff.count_weekago)

		install_nt_sub = self.getinstallnt_sub()


		dgi = Dginstall()
		dgi.setvalue(install, install_week_d, install_rate, install_zd, install_zd_week_d, install_zd_rate, install_nt_list, install_zd_sub, install_nt_sub, dataweek_kff.count, install_kff_rate, install_kff_week_d)


		dgbase = Dgbase(self.work_dir)
		reportext_dgi_install = dgbase.formatext_dau_install(dgdau, dgi)
		self.logger.outMsg('start_analysis_dau end...')
		return reportext_dgi_install

	def start_analysis_dgpush(self):
		self.logger.outMsg('start analysis dgpushduba...')
		h_time = helper.get_recent_hour()
		self.logger.outMsg(h_time)
		dgpushdb, dgpushdb_b, dgpushdb_d = self.getweek_d('dgpushdb', 'today')
		dgpushdb_rate = mynum.getrate_str(dgpushdb_d, dgpushdb_b)
		estimatecount, estimate_weed_d, estimate_rate = self.get_estimatedgpush(hourtime=h_time)
		dgpushdb_sub_d = self.get_estimatedgpush_sub(hourtime=h_time)

		dgp = Dgpushduba()
		dgp.setvalue(dgpushdb, dgpushdb_d, dgpushdb_rate, dgpushdb_sub_d, estimatecount, estimate_weed_d, estimate_rate)

		dgbase = Dgbase(self.work_dir)
		reportext_dgpush = dgbase.formatext_dgpush(dgp)
		logger2.outMsg('end...')
		return reportext_dgpush

	def start_analysis_lbpcliucun(self):
		self.logger.outMsg('start analysis lbpcliucun...')
		totalinstall, newuninst, totalinstall_b, newuninst_b = self.getweek_d('lb_newuninst')
		newuninst_rate = mynum.float_decimal2((float(newuninst) / float(totalinstall)) * 100)
		newuninst_rate_b = mynum.float_decimal2((float(newuninst_b) / float(totalinstall_b)) * 100)
		temp = newuninst_rate - newuninst_rate_b
		week_d_rate = mynum.float_decimal2(temp, fh=True)

		liucun1d_rate, liucun1d_rate_weekd = self.get_lb_liucun1d_rate_all()
		liucun7d_rate, liucun7d_rate_weekd = self.get_lb_liucun7d_rate_all()

		lbliucun = LBliucun()
		lbliucun.channeltop, lbliucun.newinst_dict, lbliucun.newuninst_dict, lbliucun.liucun1d_rate_dict, lbliucun.liucun1d_rate_weekd_dict=self.get_lb_liucun_by_channel()
		lbliucun.setvalue(totalinstall, newuninst, newuninst_rate, week_d_rate, liucun1d_rate, liucun1d_rate_weekd, liucun7d_rate, liucun7d_rate_weekd)
		dgbase = Dgbase(self.work_dir)
		reportlbliucun = dgbase.formatext_lbliucun(lbliucun)
		self.logger.outMsg('...end')
		return reportlbliucun

	def start_analysis_dbliucun(self):
		self.logger.outMsg('start analysis dbliucun...')
		totalinstall, newuninst, totalinstall_b, newuninst_b = self.getweek_d('db_newinst_uninst')
		totalinstall_dif = totalinstall - totalinstall_b
		db_totalinst_d_rate = mynum.getrate_str(totalinstall_dif, totalinstall_b)
		newuninst_rate = mynum.float_decimal2((float(newuninst) / float(totalinstall)) * 100)
		newuninst_rate_b = mynum.float_decimal2((float(newuninst_b) / float(totalinstall_b)) * 100)
		newuninst_d_rate = mynum.float_decimal2(newuninst_rate - newuninst_rate_b, fh=True)

		self.logger.outMsg('start get_db_liucun_rate_all...')
		liucun1d_rate, liucun1d_rate_weekd, liucun7d_rate, liucun7d_rate_weekd = self.get_db_liucun_rate_all()

		dbliucun = DBliucun()
		dbliucun_basic = LiuCunBasic()
		self.logger.outMsg('start get_db_liucun_by_channel...')
		dbliucun.channeltop, dbliucun.dict_newinst, dbliucun.dict_newuninst, dbliucun.dict_liucun1d_rate, dbliucun.dict_liucun1d_rate_weekd = self.get_db_liucun_by_channel()
		dbliucun_basic.setvalue(totalinstall,newuninst, newuninst_rate, newuninst_d_rate,liucun1d_rate, liucun7d_rate, liucun1d_rate_weekd, liucun7d_rate_weekd)
		dbliucun.setvalue(dbliucun_basic, totalinstall_dif, db_totalinst_d_rate)

		dgbase = Dgbase(self.work_dir)
		self.logger.outMsg('start formatext_dbliucun...')
		reportdbliucun = dgbase.formatext_dbliucun(dbliucun)
		self.logger.outMsg('...end')
		return reportdbliucun


if __name__ == '__main__':
	if len(sys.argv) == 2:
		a = Analyzer(os.path.dirname(sys.argv[0]))
		logger2 = Log(os.path.join(os.path.dirname(sys.argv[0]), 'log', 'dg_report.txt'))

		if sys.argv[1] == 'reportdgdau':
			a.logger.outMsg('start reportdgdau...')
			id, sender = getidandsender(sys.argv[0], sys.argv[1])
			text = a.start_analysis_dau()
			print text
			# ret = sendwxmsg(text, id, sender)
			a.logger.outMsg('end...')
		elif sys.argv[1] == 'reportdgpush':
			a.logger.outMsg('start reportdgpush...')
			id, sender = getidandsender(sys.argv[0], sys.argv[1])
			text = a.start_analysis_dgpush()
			# sendwxmsg(text, id, sender)
			print text
			a.logger.outMsg('end...')
		elif sys.argv[1] == 'reportlbliucun':
			id, sender = getidandsender(sys.argv[0], sys.argv[1])
			a.logger.outMsg('start reportlbliucun...')
			text = a.start_analysis_lbpcliucun()
			print text
			# sendwxmsg(text, id, sender)
		elif sys.argv[1] == 'reportdbliucun':
			ret = getidandsender(sys.argv[0], sys.argv[1])
			id, sender = getidandsender(sys.argv[0], sys.argv[1])
			a.logger.outMsg('start reportdbliucun...')
			text = a.start_analysis_dbliucun()
			print text
			# sendwxmsg(text, id, sender)
