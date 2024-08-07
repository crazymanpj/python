#coding=utf-8
#解析发布数据记录，写入数据库
from SearchMail import MailManager
from MysqlHelper import MysqlHelper
import myconfig
import sys

def getdatapathlistfromdb(channel, subchannel, num):
	sql = "select path_223 from dubadata_data where language = '%s' and channel= '%s' and status = 1 order by id desc limit %d"%(channel,subchannel,num)
	mysqlhelper = MysqlHelper()
	datalist = mysqlhelper.query_data(sql)
	return datalist

def getalldatapathlistfromdb():
	sql = "select path_223 from dubadata_data where status = 1"
	mysqlhelper = MysqlHelper()
	datalist = mysqlhelper.query_data(sql)
	return datalist

def getdatapathlistfromdblimit(start):
	sql = "select id, path_223 from dubadata_data where status = 1 and id > %s"%(start,)
	mysqlhelper = MysqlHelper()
	datalist = mysqlhelper.query_data(sql)
	return datalist

def getdatapathfromdblimitbyid(id):
	sql = "select path_223 from dubadata_data where status = 1 and id = %s"%(id,)
	mysqlhelper = MysqlHelper()
	datalist = mysqlhelper.query_data(sql)
	return datalist


sourcedata = []
endid = 0
#datapath = getdatapathlistfromdb("kav2010", "1509", 100)
#datapath = getdatapathlistfromdb("kav2010", "1338", 10)
#datapath = getalldatapathlistfromdb()
start_num = myconfig.getconfigvalue("mailconfig.ini", "searchmail", "start")
print start_num
#datapath = getdatapathlistfromdblimit(start_num)
ret = getdatapathlistfromdblimit(start_num)
mailmanager = MailManager()
for i in ret:
	sourcedata.append(i[1])
	endid = i[0]
mailmanager.searchmailbyarray(sourcedata)
print "endid: " + str(endid)
myconfig.writeinivalue("mailconfig.ini", "searchmail", "start", endid)

