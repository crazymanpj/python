# !/usr/bin/env python
# encoding=utf-8
# Date:    2017-02-22
# Author:  pangjian
import json
import requests
import cookielib
import sys
from common import winhelper
from config import dataconfig
import time
import datetime
import os

def login(username, password, session):
	body_value = {u"email": username, u"password": password}
	r = session.post(dataconfig.LOGIN_URL, data=body_value)
	# print r.text
	# print r.cookies
	#失败处理
	return r

def data_create(dirpath, product, language, channel, session):
	print "==============data_create============="
	print dirpath
	print product
	print language
	print channel
	body_value = {u"path": dirpath, u"product": product, u"language": language, u"channel":channel, u"forcereboot":0, u"nosigncheck":0}
	body_json = json.dumps(body_value)
	# print body_value
	# print body_json
	r = session.post(dataconfig.DATA_CREATE_URL, data=body_json)
	# print r.text
	# print r.request.body
	return r

def data_publish(pubid, session):
	print "=================data_publish=========="
	print pubid
	body_value = {u"id": pubid}
	print body_value
	r = session.post(dataconfig.DATA_PUBLISH_URL, data=body_value)
	# print r.text
	return r

def iscallinterface_success(ret_json):
	if ret_json['errcode'] == 0:
		print "call success"
		return True
	else:
		print "call fail"
		return False

def calldatacreateloop(packagepath, channel, session, looptimes):
	for i in range(0, looptimes):
		print "create data failed, try to recreate..."
		starttime = datetime.datetime.now()
		winhelper.waitfortime_second(starttime, 250, 20)
		ret_json = data_create(packagepath, dataconfig.PROCDUCt_SJZS, dataconfig.LANGUAGE_SJZS, channel, session)
		if iscallinterface_success(json.loads(ret_json.text)) == True:
			ret_createdata = json.loads(ret_json.text)
			return ret_createdata
		else:
			print json.loads(ret_json.text)['msg']
	return False

def calldatapubloop(pubid, session, looptimes):
	for i in range(0, looptimes):
		print "pub data fail, try to repub..."
		starttime = datetime.datetime.now()
		winhelper.waitfortime_second(starttime, 250, 20)
		ret_json = data_publish(pubid, session)
		if iscallinterface_success(json.loads(ret_json.text)) == True:
			return True
		else:
			print json.loads(ret_json.text)['msg']
	return False

def autotask_sjzsrcmdpackagepub(packagepath, channellist, session):
	looptime = 0 
	starttime = datetime.datetime.now()
	for i in channellist:
		retdata = data_create(packagepath, dataconfig.PROCDUCt_SJZS, dataconfig.LANGUAGE_SJZS, i, session)
		ret_createdata = json.loads(retdata.text)
		if iscallinterface_success(ret_createdata) == False:
			print "create data failed"
			print ret_createdata['msg']
			ret = calldatacreateloop(packagepath, i, session, 2)
			if ret == False:
				return False
			else:
				ret_createdata = ret

		pubid = ret_createdata['common']['id']
		print pubid

		if looptime > 0:
			winhelper.waitfortime_second(starttime, 300, 20)

		retpub = data_publish(pubid, session)
		if iscallinterface_success(json.loads(retpub.text)) == False:
			print "publish data failed"
			print json.loads(retpub.text)['msg']
			if calldatapubloop(pubid, session, 2) == False:
				return False

		print datetime.datetime.now()
		starttime = datetime.datetime.now()
		looptime = looptime + 1
	return True

print "==================sjzs auto publish start....========================"

s = requests.Session()
ret = login(dataconfig.USERNAME, dataconfig.PASSWORD, s)
if iscallinterface_success(json.loads(ret.text)) == False:
	print "login failed"
	sys.exit()
packagepath = sys.argv[1]
ret = autotask_sjzsrcmdpackagepub(packagepath, dataconfig.SJZS_CHANNELLIST, s)
ret = True
if ret == True:
	print "autopublish task success, exit..."
else:
	print "autopublish task fail, exit..."
print "==================sjzs auto publish end....========================"
os.system("pause")