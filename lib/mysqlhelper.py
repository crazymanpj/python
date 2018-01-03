#encoding=utf-8
import MySQLdb
import config
import sys

#查询目标数据
def query_data(sql):
    data = None
    try:
        conn = MySQLdb.connect(host=config.MYSQL_DB_HOST,user=config.MYSQL_DB_USER,passwd=config.MYSQL_DB_PASSWORD,db=config.MYSQL_DB_NAME,port=config.MYSQL_DB_PORT,charset='utf8')
        cur = conn.cursor();
        cur.execute(sql)
        rows = cur.fetchall()
        data = rows
    except MySQLdb.Error, e:
        IS_Connect = False
        #若出现异常，打印信息
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)
    return data

def execute_sql(sql):
    try:
        conn = MySQLdb.connect(host=MYSQL_DB_HOST,user=config.MYSQL_DB_USER,passwd=config.MYSQL_DB_PASSWORD,db=config.MYSQL_DB_NAMEE,port=config.MYSQL_DB_PORT,charset='utf8')
        cur = conn.cursor();
        cur.execute(sql)
        conn.commit()
        conn.close()
        cur.close()
        print 'db commit'
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        conn.rollback()
        conn.close()
        cur.close()
        return False
    return True

def query_data_retsingledata(sql):
    return query_data(sql)[0][0]

def query_data_original(sql):
    data = {}
    try:
        conn = MySQLdb.connect(host=config.MYSQL_DB_HOST, user = config.MYSQL_DB_USER, passwd = config.MYSQL_DB_PASSWORD, db=config.MYSQL_DB_NAME, port=config.MYSQL_DB_PORT, charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        rows = cur.fetchall()
        descriptionlist =  cur.description
        for (i,j) in zip(rows[0], descriptionlist):
            data[j[0]] = i
        return data
    except MySQLdb.Error, e:
        print "Error %d: %s" % (e.args[0],e.args[1])
        sys.exit(1)

    return rows