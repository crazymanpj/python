#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-03-31
# Author:  pangjian
# version: 1.0
# 用于获取导航跑的性能数据

import requests
import mysqlhelper
import urlperfdata
import chardet
import time
import os
import sys
import json

def detail_to_db2(url_json, dataid):
	r = requests.get(url=url_json)
	print type(r)
	# print r.text
	# print r.json()[0]['StatusCode']
	print len(r.json())
	for i in r.json():
		upd = urlperfdata.urlperfdata()
		upd.StatusCode = i["StatusCode"]
		print i["StatusCode"]
		upd.url =  i["url"]
		upd.ReasonPhrase = i["ReasonPhrase"]
		upd.FromCache = i["FromCache"]
		upd.RequestStartTime = i["RequestStartTime"]
		upd.RequestEndTime = i["RequestEndTime"]
		upd.ResponseSize = i["ResponseSize"]
		upd.ResponseDuration = i["ResponseDuration"]
	#-----------------------------------------------------
		upd.ResponseWaitingDuration = i["ResponseWaitingDuration"]
		upd.ResponseDownloadDuration = i["ResponseDownloadDuration"]
		upd.ResponseDNSLookupDuration = i["ResponseDNSLookupDuration"]
		upd.ResponseMethod = i["ResponseMethod"]
		upd.Expires = i["Expires"]
		upd.width = i["width"]
		upd.height = i["height"]
		upd.hasKeepAlive = i["hasKeepAlive"]
		upd.hasGZip = i["hasGZip"]
		upd.hasCookie = i["hasCookie"]
	#-----------------------------------------------------------------
		upd.hasCache = i["hasCache"]
		upd.hasExpires = i['hasExpires']
		upd.isFromCDN = i['isFromCDN']
		upd.isImgFile = i["isImgFile"]
		upd.isPng = i["isPng"]
		upd.isJpg = i["isJpg"]
		upd.isGif = i["isGif"]
		upd.isIco = i["isIco"]
		upd.isSvg = i["isSvg"]
		upd.isCssFile = i["isCssFile"]
	#---------------------------------------------------------------
		upd.isJsFile = i["isJsFile"]
		upd.isDocFile = i["isDocFile"]
		upd.isAudioFile = i["isAudioFile"]
		upd.isVideoFile = i["isVideoFile"]
		upd.isFontFile = i["isFontFile"]
		upd.isOtherFile = i["isOtherFile"]
		upd.isHttp200 = i["isHttp200"]
		upd.isHttp301 = i["isHttp301"]
		upd.isHttp302 = i["isHttp302"]
		upd.isHttp304 = i["isHttp304"]
		upd.isHttp404 = i["isHttp404"]
	# for k,v in i.items():
	# 	print "%s: %s"%(k, v)
		# j = j + 1
		print "-" * 100
		print str(upd.ResponseWaitingDuration)
	# print "count" + str(j)
	# sql = """insert into dh_perfdata_detail values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
 # %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
 # %s, %s, %s, %s, %s, %s, %s, %s, %s)"""%(i["StatusCode"], i["url"], \
 # 		i["ReasonPhrase"], i["FromCache"], i["RequestStartTime"], i["RequestEndTime"], \
	# 	i["ResponseSize"], i["ResponseDuration"], i["ResponseWaitingDuration"], i["ResponseDownloadDuration"], i["ResponseDNSLookupDuration"],\
	# 	i["ResponseMethod"], upd.Expires, i["width"], i["height"], i["hasKeepAlive"], i["hasGZip"], i["hasCookie"], i["hasCache"], i["hasExpires"],\
	# 	i["isFromCDN"], i["isImgFile"], i["isPng"], i["isJpg"], i["isGif"], i["isIco"], i["isSvg"], i["isCssFile"], i["isJsFile"], i["isDocFile"],\
	# 	i["isAudioFile"], i["isVideoFile"], i["isFontFile"], i["isOtherFile"], i["isHttp200"], i["isHttp301"], i["isHttp302"], i["isHttp304"], i["isHttp404"])
		sql = """insert into dh_perfdata_detail values(%d, %d, '%s', '%s', '%s', %s, %s, %s, %s, %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
		'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(0, dataid, \
		upd.StatusCode, upd.url, upd.ReasonPhrase, upd.FromCache, upd.RequestStartTime, upd.RequestEndTime,upd.ResponseSize, upd.ResponseDuration, \
		upd.ResponseWaitingDuration, upd.ResponseDownloadDuration, upd.ResponseDNSLookupDuration, upd.ResponseMethod, upd.Expires, upd.width, upd.height, upd.hasKeepAlive, upd.hasGZip, upd.hasCookie,\
		upd.hasCache, upd.hasExpires, upd.isFromCDN, upd.isImgFile, upd.isPng, upd.isJpg, upd.isGif, upd.isIco, upd.isSvg, upd.isCssFile,\
		upd.isJsFile, upd.isDocFile, upd.isAudioFile, upd.isVideoFile, upd.isFontFile, upd.isOtherFile, upd.isHttp200, upd.isHttp301, upd.isHttp302, upd.isHttp304, upd.isHttp404)
	# print sql
		mysql = mysqlhelper.MysqlHelper()
		mysql.execute_sql(sql)


def detail_to_db(jsondata, dataid):
	# r = requests.get(url=url_json)
	# print type(r)
	# print r.text
	# print r.json()[0]['StatusCode']
	# print len(jsondata)
	# print json.loads(jsondata)
	print len(jsondata)
	for i in jsondata:
		upd = urlperfdata.urlperfdata()
		upd.StatusCode = i["StatusCode"]
		upd.url =  i["url"]
		upd.ReasonPhrase = i["ReasonPhrase"]
		upd.FromCache = i["FromCache"]
		upd.RequestStartTime = i["RequestStartTime"]
		upd.RequestEndTime = i["RequestEndTime"]
		upd.ResponseSize = i["ResponseSize"]
		upd.ResponseDuration = i["ResponseDuration"]
	#-----------------------------------------------------
		upd.ResponseWaitingDuration = i["ResponseWaitingDuration"]
		upd.ResponseDownloadDuration = i["ResponseDownloadDuration"]
		upd.ResponseDNSLookupDuration = i["ResponseDNSLookupDuration"]
		upd.ResponseMethod = i["ResponseMethod"]
		upd.Expires = i["Expires"]
		upd.width = i["width"]
		upd.height = i["height"]
		upd.hasKeepAlive = i["hasKeepAlive"]
		upd.hasGZip = i["hasGZip"]
		upd.hasCookie = i["hasCookie"]
	#-----------------------------------------------------------------
		upd.hasCache = i["hasCache"]
		upd.hasExpires = i['hasExpires']
		upd.isFromCDN = i['isFromCDN']
		upd.isImgFile = i["isImgFile"]
		upd.isPng = i["isPng"]
		upd.isJpg = i["isJpg"]
		upd.isGif = i["isGif"]
		upd.isIco = i["isIco"]
		upd.isSvg = i["isSvg"]
		upd.isCssFile = i["isCssFile"]
	#---------------------------------------------------------------
		upd.isJsFile = i["isJsFile"]
		upd.isDocFile = i["isDocFile"]
		upd.isAudioFile = i["isAudioFile"]
		upd.isVideoFile = i["isVideoFile"]
		upd.isFontFile = i["isFontFile"]
		upd.isOtherFile = i["isOtherFile"]
		upd.isHttp200 = i["isHttp200"]
		upd.isHttp301 = i["isHttp301"]
		upd.isHttp302 = i["isHttp302"]
		upd.isHttp304 = i["isHttp304"]
		upd.isHttp404 = i["isHttp404"]
	# for k,v in i.items():
	# 	print "%s: %s"%(k, v)
		# j = j + 1
		print "-" * 100
		print str(upd.ResponseWaitingDuration)
	# print "count" + str(j)
	# sql = """insert into dh_perfdata_detail values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
 # %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,\
 # %s, %s, %s, %s, %s, %s, %s, %s, %s)"""%(i["StatusCode"], i["url"], \
 # 		i["ReasonPhrase"], i["FromCache"], i["RequestStartTime"], i["RequestEndTime"], \
	# 	i["ResponseSize"], i["ResponseDuration"], i["ResponseWaitingDuration"], i["ResponseDownloadDuration"], i["ResponseDNSLookupDuration"],\
	# 	i["ResponseMethod"], upd.Expires, i["width"], i["height"], i["hasKeepAlive"], i["hasGZip"], i["hasCookie"], i["hasCache"], i["hasExpires"],\
	# 	i["isFromCDN"], i["isImgFile"], i["isPng"], i["isJpg"], i["isGif"], i["isIco"], i["isSvg"], i["isCssFile"], i["isJsFile"], i["isDocFile"],\
	# 	i["isAudioFile"], i["isVideoFile"], i["isFontFile"], i["isOtherFile"], i["isHttp200"], i["isHttp301"], i["isHttp302"], i["isHttp304"], i["isHttp404"])
		sql = """insert into dh_perfdata_detail values(%d, %d, '%s', '%s', '%s', %s, %s, %s, %s, %s, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',\
		'%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')"""%(0, dataid, \
		upd.StatusCode, upd.url, upd.ReasonPhrase, upd.FromCache, upd.RequestStartTime, upd.RequestEndTime,upd.ResponseSize, upd.ResponseDuration, \
		upd.ResponseWaitingDuration, upd.ResponseDownloadDuration, upd.ResponseDNSLookupDuration, upd.ResponseMethod, upd.Expires, upd.width, upd.height, upd.hasKeepAlive, upd.hasGZip, upd.hasCookie,\
		upd.hasCache, upd.hasExpires, upd.isFromCDN, upd.isImgFile, upd.isPng, upd.isJpg, upd.isGif, upd.isIco, upd.isSvg, upd.isCssFile,\
		upd.isJsFile, upd.isDocFile, upd.isAudioFile, upd.isVideoFile, upd.isFontFile, upd.isOtherFile, upd.isHttp200, upd.isHttp301, upd.isHttp302, upd.isHttp304, upd.isHttp404)
	# print sql
		mysql = mysqlhelper.MysqlHelper()
		mysql.execute_sql(sql)

def getchannelfromurl(url):
	return os.path.basename(url).split(".")[0]


def datalist_to_db(url, imagefilepath):
	channel = ""
	channel = getchannelfromurl(url)
	run_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	sql = "insert into dh_perfdata_runresult values(%d, '%s', '%s', '%s', '%s')"%(0, run_time, url, channel, imagefilepath)
	m_sql = mysqlhelper.MysqlHelper()
	m_sql.execute_sql(sql)

def getlastid():
	sql = "select * from dh_perfdata_runresult order by '-id'"
	m_sql = mysqlhelper.MysqlHelper()
	return m_sql.query_data(sql)[0][0]

def getlastmodifyfilefrompath(path):
	print path
	m_list = []
	for parent, dirnames, filenames in os.walk(path):
		for file in filenames:
			file = file.strip("pcrelust")
			m_list.append(int(file.split(".")[0]))
	m_list.sort()
	key =  str(m_list[-1])
	for parent, dirnames, filenames in os.walk(path):
		for file in filenames:
			if file.find(key) >= 0:
				return os.path.join(parent, file)

def getimagepath(keyword):
	path = r"http://10.20.216.222/img/"
	return os.path.join(path, keyword + ".jpg")

def getkeyword(path):
	m_file = open(os.path.join(path, "runner.txt"), "r")
	text = m_file.read()
	m_file.close()
	return text

def getjsondatafromfile(filepath):
	m_file = open(filepath, "r")
	content =  m_file.read()
	jsondata = json.loads(content)
	m_file.close()
	return jsondata


if __name__ == '__main__':
	if len(sys.argv) == 3:
		ret = getkeyword(sys.argv[2])
		print ret
		data = getjsondatafromfile(os.path.join(sys.argv[2], ret + ".json"))
		iamgepath = getimagepath(ret)
		print iamgepath
		datalist_to_db(sys.argv[1], iamgepath)
		dataid = getlastid()
		detail_to_db(data, dataid)