#encoding=utf-8
import MySQLdb


#远程数据库 
def remotemysql():
	try:
		conn=MySQLdb.connect(host='xxx',user='xxx',passwd='xxx',db='xxx',port=xxx)
		cur=conn.cursor()
		cur.execute('')
		print cur.fetchall()
		cur.close()
		conn.close()
	except MySQLdb.Error,e:
		print "Mysql Error %d: %s" % (e.args[0], e.args[1])


remotemysql()

#数据库表达式
#mysql
# cur.execute("select * from user where userid = '%s' and password = '%s'" %(userid,password))

# tp = "all"
# sql = 'select * from dhlog_loading_data_percent where tp = "all" and br = "chrome" and brv = "all"'

# id="sfe"
# subchannel = "eee"
# print r"SELECT path from info_path where file_id=? and subchannel=?", (id,subchannel)

# tp ="all"
# br="fe"
# starttime="2334"
# endtime="233"
# print "select * from dhlog_loading_data_percent where tp ='%s' and br = '%s' and brv = 'all' and date between '%s' and '%s'"%(tp, br, starttime, endtime)

