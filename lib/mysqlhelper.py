#coding=utf-8
import MySQLdb
import sys
class MysqlHelper(object):
	#用户名
	username = ""
	password = ""
	ip=""
	dbname=""
	port=3306


	"""docstring for MysqlHelper"""
	def __init__(self):
		super(MysqlHelper, self).__init__()
		#self.arg = arg
		self.username = "remoteedit"
		self.password = "259gHS7y"
		self.ip="10.20.220.57"
		self.dbname="dubavermgr"
		self.port=3306

	def query_data(self, sql):
		data = ""
		try:
			conn = MySQLdb.connect(host=self.ip, user=self.username, passwd=self.password, db=self.dbname, port=self.port)
			cur = conn.cursor()
			print "sql: " + sql
			#sql = MySQLdb.escape_string(sql)
			print "querydata: " + sql
			cur.execute(sql)
			rows = cur.fetchall()
			data = rows
		except MySQLdb.Error, e:
			print str(e)
			print "Connet mysql db error..."
			sys.exit()

		return data

	#by pj 8.3
	def execute_sql_mailinfo(self, sql, mailinfo):
		print sql
		try:
			conn = MySQLdb.connect(host=self.ip, user=self.username, passwd=self.password, db=self.dbname, port=self.port)
			cur = conn.cursor()
			conn.set_character_set('utf8')
			cur.execute('SET NAMES utf8;')
			cur.execute('SET CHARACTER SET utf8;')
			cur.execute('SET character_set_connection=utf8;')

			print mailinfo.publishtime
			print type(mailinfo.publishtime)
			cur.execute(sql, (mailinfo.data_id, mailinfo.mailtitle, mailinfo.tester, mailinfo.publishtime, mailinfo.mailid, mailinfo.pd, mailinfo.isqualified, mailinfo.fileinfo, mailinfo.changelist, mailinfo.checklist, mailinfo.notpassreason, mailinfo.datapath, mailinfo.channel, mailinfo.subchannel))
			conn.commit()
			conn.close()
			cur.close()
		except MySQLdb.Error, e:
			print str(e)
			print "Execute mysql db error..."
			sys.exit()


#sql = "select mailtitle from dubadata_mailinfo"
#sqlmanager = MysqlHelper()
#ret = sqlmanager.query_data(sql)
#for i in ret:
#	print str(i) 