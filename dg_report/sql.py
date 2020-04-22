#encoding=utf-8
# Date:    2017-10-10
# Author:  pangjian
# version: 1.0

import mysqlhelper
from config import DG_DAU_CHANNEL_ZD, DG_DAU_CHANNEL_NT, DG_PUSH_DUBA_TOD2,DB_CHANNEL_NEW
from config import DG_INSTALL_BZ,DG_INSTALL_FENFA, DG_INSTALL_ZD_CHANNEL, LB_PID_LIKE
from config import DB_CHANNEL, LB_PROMOTION_CHANNEL
import helper

class Sql(object):
	"""docstring for Sql"""
	def __init__(self, date):
		super(Sql, self).__init__()
		self.date = date

	def get_dau(self):
		sql = "select resident_all from dg_resident_install where date='%s'"%(self.date,)
		ret = mysqlhelper.query_data(sql)
		return ret[0][0]

	def get_dau_bychannel(self):
		ret_zd = {}
		ret_nt = {}

		for k, v in DG_DAU_CHANNEL_ZD.items():
			sql = "select %s from dg_resident_install where date='%s'"%(v, self.date)
			ret_zd[k] = mysqlhelper.query_data_retsingledata(sql)

		for k, v in DG_DAU_CHANNEL_NT.items():
			sql = "select %s from dg_resident_install where date='%s'" % (v, self.date)
			ret_nt[k] = mysqlhelper.query_data_retsingledata(sql)

		return ret_zd, ret_nt

	#总安装
	def get_totalinstall(self):
		sql = "select install_suc_all from dg_resident_install where date='%s'"%(self.date,)
		return mysqlhelper.query_data_retsingledata(sql)

	#主动安装
	def get_install_zd(self):
		sql = "select install_suc_zhudong from dg_resident_install where date='%s'"%(self.date,)
		return mysqlhelper.query_data_retsingledata(sql)
	#内推安装
	def get_install_nt(self):
		sql = "select install_suc_2214 from dg_resident_install where date='%s'" % (self.date,)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_install_bychannel(self):
		ret = []
		for i in DG_INSTALL_CHANNEL:
			sql = "select %s from dg_resident_install where date='%s'"%(i, self.date)
			ret.append(mysqlhelper.query_data_retsingledata(sql))

		return ret

	def get_install_bypid(self):
		pass

	#主动安装分渠道
	def get_install_zd_bychannel(self):
		ret = {}
		for k, v in DG_INSTALL_ZD_CHANNEL.items():
			sql = "select sum(%s) from dg_install_pid where date='%s'" % (v, self.date)
			ret[k] = mysqlhelper.query_data_retsingledata(sql)
		return ret

	#标准版
	def get_install_bz(self):
		sql = "select sum(pid_1000) from dg_install_pid where date='%s'" % (self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	#套装版（阿拉丁）安装
	def get_install_ald(self):
		sql = "select sum(pid_1150) from dg_install_pid where date='%s'"%(self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	#网卡版安装
	def get_install_wkb(self):
		sql = "select sum(pid_1300) from dg_install_pid where date='%s'"%(self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	#可分发安装
	def get_install_kff(self):
		sqltext = ''
		for i in DG_INSTALL_FENFA:
			if sqltext == '':
				sqltext = sqltext + i
			else:
				sqltext = sqltext + '+' + i

		sql = "select sum(%s) from dg_install_pid where date='%s'" % (sqltext, self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	#毒霸信息流
	def get_install_xxl(self):
		sql = "select sum(pid_2214) from dg_install_pid where date='%s'"%(self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	#勋章墙
	def get_install_xzq(self):
		sql = "select sum(pid_1170) from dg_install_pid where date='%s'" % (self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_dg_push_duba(self, hour=23):
		sql = "select sum(new_install) from duba_newinstall_waitui_ss where date='%s' and ((tid1=10 and tid2 in (164,165,167)) or (tid1=48 and tid2 in (545,33)))  and hour <= %d"%(self.date, hour)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_dg_push_duba_bychannel(self, hour=23):
		ret = {}
		for i in DG_PUSH_DUBA_TOD2:
			sql = "select sum(new_install) from duba_newinstall_waitui_ss where date='%s' and tid1=10 and tid2=167 and tod1=910 and tod2=%s and hour <= %d"%(self.date, i, hour)
			ret[i] = mysqlhelper.query_data_retsingledata(sql)

		return ret


	#猎豹浏览器留存数据
	def get_lb_newinst_total(self):
		sql = "select newinst from lb_newinst_pid where date='%s'"%(self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_lb_newuninst(self):
		sql = "select newuninst from lb_pc_newinst_liucun where date='%s' and ver='all' and pid='all'"%(self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_lb_newinst_bypid(self, pid):
		sql = "select newinst from lb_pc_newinst_liucun where date='%s' and ver='all' and pid='%s'"%(self.date, pid)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_lb_newinst_promotion_bypid(self, pid):
		sql = "select newinst from lb_urlchoose_retain where date='%s' and lbver='all' and pid='%s' and tryno='all'"%(self.date, pid)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_lb_liucun_1d_bypid(self, pid):
		sql = "select liucun_1d from lb_pc_newinst_liucun where date='%s' and ver='all' and pid='%s'"%(self.date, pid)
		return  mysqlhelper.query_data_retsingledata(sql)

	def get_lb_liucun1d_promotion_bypid(self, pid):
		sql = "select liucun_1d from lb_urlchoose_retain where date='%s' and lbver='all' and pid='%s' and tryno='all'"%(self.date, pid)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_lb_liucun_7d_bypid(self, pid):
		sql = "select liucun_7d from lb_pc_newinst_liucun where date='%s' and ver='all' and pid='%s'"%(self.date, pid)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_lb_newinst_bychannel(self):
		sql = "select * from lb_newinst_pid where date='%s'"%(self.date)
		ret = mysqlhelper.query_data_original(sql)
		print ret
		for k,v in ret.items():
			if k.find('_inst') < 0:
				del ret[k]
				continue

			temp = k.replace('_inst', '')
			if temp in LB_PROMOTION_CHANNEL:
				sql = "select newinst from lb_urlchoose_retain where date='%s' and lbver='all' and pid='%s' and tryno='all'"%(self.date, temp)
				ret[k] = mysqlhelper.query_data_retsingledata(sql)
		return ret

	def get_lb_newuninst_bychannel(self, pidlist):
		ret = {}
		for k in pidlist:
			k = k.replace('_inst', '', 1)
			if k in LB_PID_LIKE:
				temp = "%" + k + "%"
				sql = "select sum(newuninst) from lb_pc_newinst_liucun where date='%s' and pid like '%s' and ver='all'" % (self.date, temp)
			else:
				sql = "select newuninst from lb_pc_newinst_liucun where date='%s' and pid='%s' and ver='all'"%(self.date, k)
			ret[k] = mysqlhelper.query_data_retsingledata(sql)

		return ret

	def get_lb_liucun_1d_bychannel(self, pidlist):
		ret = {}
		for k in pidlist:
			k = k.replace('_inst', '', 1)
			if k in LB_PID_LIKE:
				temp = "%" + k + "%"
				sql = "select sum(liucun_1d) from lb_pc_newinst_liucun where date='%s' and pid like '%s' and ver='all'" % (self.date, temp)
			elif k in LB_PROMOTION_CHANNEL:
				sql = "select liucun_1d from lb_urlchoose_retain where date='%s' and lbver='all' and pid='%s' and tryno='all'"%(self.date, k)
			else:
				sql = "select liucun_1d from lb_pc_newinst_liucun where date='%s' and pid='%s' and ver='all'"%(self.date, k)

			ret[k] = mysqlhelper.query_data_retsingledata(sql)
		return ret

	def get_lb_liucun7d_bychannel(self, dict_newinst):
		ret = {}
		for k, v in dict_newinst.items():
			k = k.replace('_inst', '', 1)
			if k in LB_PID_LIKE:
				temp = "%" + k + "%"
				sql = "select sum(liucun_7d) from lb_pc_newinst_liucun where date='%s' and pid like '%s' and ver='all'" % (self.date, temp)
			elif k in LB_PROMOTION_CHANNEL:
				sql = "select liucun_7d from lb_urlchoose_retain where date='%s' and lbver='all' and pid='%s' and tryno='all'"%(self.date, k)
			else:
				sql = "select liucun_7d from lb_pc_newinst_liucun where date='%s' and pid='%s' and ver='all'"%(self.date, k)

			ret[k] = mysqlhelper.query_data_retsingledata(sql)

		return ret

	#毒霸留存数据
	def get_db_newinst_total(self):
		sql = "select new_install_uuids from duba_tid1_tid2_detail_install where date='%s' and tryno='all' and tid1='all' and tid2='all'"%(self.date)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_db_newuninst_bytid(self, tid1, tid2):
		sql = "select install_uninstall_uuids from duba_tid1_tid2_detail_install_uninstall_new where date='%s' and tryno='all' and tid1='%s' and tid2='%s'"%(self.date, tid1, tid2)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_db_newinst_bytid(self, tid1, tid2):
		sql = "select new_install_uuids from duba_tid1_tid2_detail_install where date='%s' and tryno='all' and tid1='%s' and tid2='%s'"%(self.date, tid1, tid2)
		return mysqlhelper.query_data_retsingledata(sql)

	# def get_db_liucun_all_1d(self):
	# 	reportdate = helper.get_time_bydiff(self.date, -1)
	# 	sql = "select retain_users from duba_tid_retention where date='%s' and ins_dt='%s' and tid1='-1' and tid2='-1'"%(reportdate, self.date)
	# 	print(sql)
	# 	return mysqlhelper.query_data_retsingledata(sql)
    #
	# def get_db_liucun_all_7d(self):
	# 	reportdate = helper.get_time_bydiff(self.date, -7)
	# 	sql = "select retain_users from duba_tid_retention where date='%s' and ins_dt='%s' and tid1='-1' and tid2='-1'"%(reportdate, self.date)
	# 	print(sql)
	# 	return mysqlhelper.query_data_retsingledata(sql)
	def get_db_tid1_and_tid2(self):
		sql = "select tid1,tid2 from duba_install_tid_uuid_stat where date='%s' group by tid1,tid2 order by new_install desc limit 1000"%(self.date)
		ret = mysqlhelper.query_data(sql)
		return ret

	def get_db_1dliucun_bytid_instdate(self, tid1, tid2):
		reportdate = helper.get_time_bydiff(self.date, -1)
		sql = "select retain_users from duba_tid_retention where date='%s' and ins_dt='%s' and tid1='%s' and tid2='%s'"%(reportdate, self.date, tid1, tid2)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_db_7dliucun_bytid_instdate(self, tid1, tid2):
		reportdate = helper.get_time_bydiff(self.date, -7)
		sql = "select retain_users from duba_tid_retention where date='%s' and ins_dt='%s' and tid1='%s' and tid2='%s'"%(reportdate, self.date, tid1, tid2)
		return mysqlhelper.query_data_retsingledata(sql)

	def get_db_newinst_bychannel(self, channeltuple):
		ret = {}
		for i in channeltuple:
			ret[i] = self.get_db_newinst_bytid(i[0], i[1])

		return ret

	def get_db_newuninst_bychannel(self, channeltuple):
		ret = {}

		for i in channeltuple:
			ret[i] = self.get_db_newuninst_bytid(i[0], i[1])

		return ret

	def get_db_1dliucun_bychannel(self, instdate, channeltuple):
		ret = {}

		for i in channeltuple:
			ret[i] = self.get_db_1dliucun_bytid_instdate(i[0], i[1])

		return ret

if __name__=='__main__':
	s = Sql('2018-01-23')
	# for k,v in DB_CHANNEL.items():
	# 	print k, v
	# print s.get_db_newinst_total()
	# print s.get_db_newuninst_total()
	# print s.get_db_liucun_bytid_instdate('2018-01-09', '-1', '-1')
	# print s.get_db_newinst_bychannel()
	# print s.get_db_newinst_total()
	# ret = s.get_db_tid1_and_tid2()
	# print s.get_db_newinst_bychannel(ret)
	# print s.get_db_liucun_bychannel('2018-01-04')
	print s.get_lb_newinst_bychannel()
