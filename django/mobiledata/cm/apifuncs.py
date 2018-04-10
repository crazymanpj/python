#!/usr/bin/env python
#encoding=utf-8
# Date:    2016-10-20
# Author:  pangjian
# version: 1.0
from models import SideBar,SideBarGroup, Procduct, FileType, Channel, PublishRecord, Package, PluginType,HostVer,ApkVer, PluginVer, IIDcode
from models import Plugin
import json
import logging
from common import myjson, androidhelper
from django.core.paginator import Paginator
import traceback
from django.db.models import Q
import time
from django.core.exceptions import ObjectDoesNotExist
import re

logger = logging.getLogger('mobiledata_cm')


def API_GetSideBarInfo():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	grouplist = []
	groups = SideBarGroup.objects.all().filter(status=1)
	for i in groups:
		group = {
			u"groupname" : i.group,
			u"sidebars" : [],
		}

		sidebars = SideBar.objects.all().filter(group = i.id, status=1)
		for j in sidebars:
			sidebar = {
				u"name" : j.name,
				u"url" : j.url,
			}
			group['sidebars'].append(sidebar)

		grouplist.append(group)

	itemlistname ="grouplist"
	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, grouplist)
	#logger.debug(ret_json)
	return ret_json

#API_GetSideBarInfo()

def API_GetSelectList():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	selectlist = {
		'product': [],
		'hostver': [],
		'channel':[],
		'apkver' :[],
	}
	products = Procduct.objects.all()
	for i in products:
		selectlist['product'].append(i.description)

	# filetypes = FileType.objects.all()
	# for i in filetypes :
	# 	selectlist['filetype'].append(i.description)
	hostverlist = HostVer.objects.all().filter(status=1).order_by('-hostver')
	for i in hostverlist:
		selectlist['hostver'].append(i.hostver)

	channels = Channel.objects.all().filter(status=1).order_by('-channelnum')
	for i in channels:
		temp = str(i.channelnum) + '(' + i.description + ')'
		selectlist['channel'].append(temp)

	apkvers = ApkVer.objects.all().filter(status=1).order_by('-apkver')
	for i in apkvers:
		selectlist['apkver'].append(i.apkver)

	itemlistname = 'selectlist'
	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, selectlist)
	#logger.debug(ret_json)
	return ret_json 

def API_CreatPublishRecord(filetype, channel, publishtime, filepath, details, user, hostver):
	record = PublishRecord(filetype=filetype, channel=channel, publishtime=publishtime, filepath=filepath, details=details, opuser=user, hostver=hostver)
	record.save()
	return True

def API_CreatePackage(apkver, packagepath, hostver, packagemd5, packagesize, channel, publishtime, iid_code, flag, opuser, remarks=u"", issync=0):
	package = Package(apkver=apkver, packagepath=packagepath, hostver=hostver, packagemd5=packagemd5, packagesize=packagesize, channel=channel, publishtime=publishtime, iid_code=iid_code, flag=flag, opuser=opuser, remarks=remarks, issync=issync)
	package.save()
	return True

def API_CreateHostver(hostver, status=1):
	addtime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
	hv = HostVer(hostver=hostver, addtime=addtime, status=1)
	hv.save()
	return True

def API_CreateApkver(apkver, status=1):
	addtime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
	a = ApkVer(apkver=apkver, addtime=addtime, status=1)
	a.save()
	return True

def API_CreatePluginver(pluginver, status=1):
	addtime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
	p = PluginVer(pluginver=pluginver, addtime=addtime, status=1)
	p.save()
	return True

def API_CreateIIDcode(iidcode, status=1):
	addtime = time.strftime("%Y-%m-%d", time.localtime(time.time()))
	i = IIDcode(iidcode=iidcode, addtime=addtime, status=1)
	i.save()
	return True

def API_CreateChannel(channel, opuser, description="", status=1):
	addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	c = Channel(channelnum=channel, description=description, addtime=addtime, status=1, opuser =opuser)
	c.save()
	return true

def API_ModifyPackage(pid, apkver, packagepath, hostver, packagemd5, packagesize, channel, publishtime, iid_code, flag, remarks=u"", issync=0):
	package = Package.objects.all().get(id=pid)
	package.apkver = apkver
	package.packagepath = packagepath
	package.hostver = hostver
	package.packagemd5 = packagemd5
	package.packagesize = packagesize
	package.channel = channel
	package.publishtime = publishtime
	package.iid_code = iid_code
	package.flag = flag
	package.remarks = remarks
	package.issync = issync
	package.save()
	return True

def API_ModityChannel(pid, channelnum, opuser, description, status=1):
	addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	channel = Channel.objects.all().get(id=pid)
	channel.addtime = addtime
	channel.channelnum = int(channelnum)
	channel.opuser = opuser
	channel.description = description
	channel.save()
	return True

def API_CreatePlugin(publishid, pluginver, hostver, pluginmd5, plugintype, pluginsize, channel, publishtime):
	plugin = Plugin(publishid=publishid, pluginver=pluginver,hostver=hostver,pluginmd5=pluginmd5,plugintype=plugintype, pluginsize=pluginsize,channel=channel,publishtime=publishtime)
	plugin.save()
	return True

def API_AddPublishRecord(jsondata, user, username):
	logger.debug(jsondata)
	channeltext = ""
	plugintext = ""
	filepathlist = ""
	isapkhasdata = 1
	msg = "提交成功!"
	errorcode = "0"
	version = "1.0"

	if not user.is_authenticated():
		msg = "请先登录，谢谢"
		errorcode = "403"
		logger.debug("not login, exit...")
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return ret_json

	try:
		# filetype = jsondata.get('filetype', None)
		hostver = jsondata.get('hostver', None)
		channels = jsondata.get('channel', None)
		for i in channels:
			channeltext = channeltext + i + "\r\n"
		publishtime = jsondata.get('publishtime', None)
		apkpath = jsondata.get('apkpath', None)
		if apkpath == None or len(apkpath) == 0:
			logger.debug("安装包为空")
			isapkhasdata = 0
		pluginlist = jsondata.get('pluginlist', None)
		if pluginlist == None or len(pluginlist) == 0:
			logger.debug("插件列表为空")
		for i in pluginlist:
			plugintext = plugintext + i + "\r\n"
		details = jsondata.get('details', None)

		# logger.debug(filetype)
		logger.debug(hostver)
		logger.debug(channeltext)
		logger.debug(publishtime)
		logger.debug(apkpath)
		logger.debug(plugintext) 
		logger.debug(details)
	except Exception,e:
		traceback.print_exc()
		logger.debug("get PublishRecord error")
		msg = "get PublishRecord error"
		errorcode = "-1"
		return myjson.generatecommonjson(msg, errorcode, version)

	#将安装包和插件信息记录到数据库
	if isapkhasdata:
		# channeltext = channeltext.strip("")
		# publishrecord = PublishRecord(filetype="安装包", channel=channeltext, publishtime=publishtime, filepath=apkpath, details=details, opuser=user, hostver=hostver)
		# publishrecord.save()
		#验证安装包信息
		if androidhelper.verifypackage(apkpath) == False:
			msg = "安装包路径信息校验失败，请检查是否填对相应的控件框"
			errorcode = "101"
			return myjson.generatecommonjson(msg, errorcode, version)

		API_CreatPublishRecord("安装包", channeltext, publishtime, apkpath, details, username, hostver)
		for i in channels:
			logger.debug("API_AddPackageRecord")
			getrecord = PublishRecord.objects.order_by('-id')
			channeltemp = Channel.objects.all().get(description=i)
			filetypetemp = FileType.objects.all().get(description="安装包")
			logger.debug(getrecord[0].id)
			API_AddPackageRecord(apkpath, getrecord[0].id, channeltemp.channelnum, publishtime, hostver)

	if plugintext != "":
		#验证插件信息
		for i in pluginlist:
			if androidhelper.verifyplugin(i) == False:
				msg = "插件路径验证失败，请检查是否填对相应的控件框"
				errorcode = "102"
				return myjson.generatecommonjson(msg, errorcode, version)

		for i in pluginlist:
			# publishrecord = PublishRecord(filetype="插件", channel=channeltext, publishtime=publishtime, filepath=i, details=details, opuser=user, hostver=hostver)
			# publishrecord.save()
			API_CreatPublishRecord("插件", channeltext, publishtime, i, details, username, hostver)
			for j in channels:
				logger.debug("API_AddPlugInRecord()")
				getrecord = PublishRecord.objects.order_by('-id')
				channeltemp = Channel.objects.all().get(description=j)
				filetypetemp = FileType.objects.all().get(description="插件")
				logger.debug(getrecord[0].id)
				API_AddPlugInRecord(i, getrecord[0].id, channeltemp.channelnum, publishtime, hostver)
	# logger.debug(filepathlist)
	# #暂时测试代码
	# ret_json = myjson.generatecommonjson("ok", 'null', '1.0')
	# return ret_json

	# #将安装包和插件信息记录到数据库
	# for i in channels:
	# 	getrecord = PublishRecord.objects.order_by('-id')
	# 	channeltemp = Channel.objects.all().get(description=i)
	# 	filetypetemp = FileType.objects.all().get(description=filetype)
	# 	logger.debug(getrecord[0].id)

	# 	if filetypetemp.id == 1 :
	# 		logger.debug("API_AddPackageRecord")
	# 		API_AddPackageRecord(jsondata, getrecord[0].id, channeltemp.channelnum, publishtime)
	# 	else:
	# 		logger.debug("API_AddPlugInRecord()")
	# 		API_AddPlugInRecord(jsondata, getrecord[0].id, channeltemp.channelnum, publishtime)
	return myjson.generatecommonjson(msg, errorcode, version)

def API_GetPublishRecord():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	datalist = []
	itemlistname = "datalist"
	records = PublishRecord.objects.all().order_by('-publishtime')
	for i in records:
		templist = {
		u"id" : i.id,
		u"filetype" : i.filetype,
		u"publishtime" : i.publishtime,
		u"channel" : i.channel,
		u"details" : i.details,
		u"filepath" : i.filepath
		}
		datalist.append(templist)
	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, datalist)
	# logger.debug(ret_json)
	return ret_json

def API_AddPackageRecord(filepath, pubid, channelnum, publishtime, hostver):
	logger.debug("id is:=====")
	logger.debug(pubid)
	print pubid
	publishid = pubid
	packagepath = filepath
	apkFilePath = androidhelper.getfilepath(packagepath)
	logger.debug(apkFilePath)
	apkver = androidhelper.getApkVersionCode(apkFilePath)
	logger.debug(apkver)
	# hostver = androidhelper.getpackagehostver(apkFilePath)
	apkpluginfo = androidhelper.getapkpluginfo(apkFilePath)
	packagemd5 = androidhelper.getmd5(apkFilePath)
	packagesize = androidhelper.getfilesize(apkFilePath)
	channel = channelnum

	package = Package(publishid=publishid, apkver=apkver, packagepath=packagepath, hostver=hostver, packagemd5=packagemd5, packagesize=packagesize,channel=channel, publishtime=publishtime, apkpluginfo=apkpluginfo)
	package.save()
	return True

def API_AddPlugInRecord(filepath, pubid, channelnum, publishtime, hostver):
	publishid = pubid
	# hostverlist = jsondata.get('hostver', None)
	# for i in hostverlist:
	# 	hostver = hostver + i + "\r\n"
	# print hostver
	logger.debug(hostver)
	pluginpath = filepath
	pluginfilepath = androidhelper.getfilepath(pluginpath)
	pluginver = androidhelper.getpluginver(pluginfilepath)
	pluginmd5 = androidhelper.getmd5(pluginfilepath)
	pluginsize = androidhelper.getfilesize(pluginfilepath)
	channel = channelnum
	plugintype = androidhelper.getplugintype(pluginfilepath)

	plugin = Plugin(publishid = publishid, pluginver=pluginver, hostver=hostver, pluginpath=pluginpath, pluginmd5=pluginmd5, plugintype=plugintype, pluginsize=pluginsize, channel=channel, publishtime=publishtime)
	plugin.save()
	return True

def API_GetPublishData(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	datalist = []
	itemlistnames = []
	datalists = []

	pagenum = received_json_data.get('page', None)
	channel = received_json_data.get('channel', None)
	# if channel == "全网渠道":
	# 	channel = 999999
	hostver = received_json_data.get('hostver', None)
	apkver = received_json_data.get('apkver', None)
	logger.debug(channel)
	logger.debug(hostver)
	logger.debug(apkver)

	records = Package.objects.all().order_by('-publishtime')

	if channel != None:
		m = re.match('(\d+)(.)', str(channel))
		channel = m.group(1)
		logger.debug(channel)
		logger.debug("channel != None")
		records = records.all().filter(channel=channel).order_by('-publishtime')
	if hostver != None:
		logger.debug("hostver != None:")
		records = records.all().filter(hostver=hostver).order_by('-publishtime')
	if apkver != None:
		logger.debug("apkver != None")
		records = records.all().filter(apkver=apkver).order_by('-publishtime')


	logger.debug(pagenum)
	p = Paginator(records, 20)
	totalpage = p.num_pages
	logger.debug(totalpage)
	page = p.page(pagenum)
	recordsbypage = page.object_list

	for i in recordsbypage:
		try:
			chanins = Channel.objects.all().filter(channelnum=int(i.channel))
			tempchannel = chanins[0].description
			if tempchannel == "":
				tempchannel = i.channel
		except:
			tempchannel = i.channel

		# if tempchannel == "999999":
		# 	tempchannel = "全网渠道"
		templist = {
		u"id" : i.id,
		u"apkver" : i.apkver,
		u"packagepath" : i.packagepath,
		u"hostver" : i.hostver,
		u"packagemd5" : i.packagemd5,
		u"packagesize": i.packagesize,
		u"channel" : tempchannel,
		u"publishtime" : i.publishtime,
		u"iidcode" : i.iid_code,
		u"opuser" : i.opuser,
		u"flag" : i.flag,
		u"remarks" : i.remarks
		}
		datalist.append(templist)
	itemlistnames.append("datalist")
	datalists.append(datalist)
	itemlistnames.append("pagecount")
	datalists.append(totalpage)
	logger.debug(datalists)
	logger.debug("-"*100)
	ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, datalists)
	logger.debug(ret_json)
	return ret_json

def API_GetHostVer():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	itemlist = []
	ret_json = {}
	itemlistname = "hostverlist"
	hostverlist = HostVer.objects.all().filter(status=1)

	for i in hostverlist:
		temp = {
		u"id" : i.id,
		u"hostver" : i.hostver
		}
		itemlist.append(temp)

	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlist)
	logger.debug(ret_json)
	return ret_json

def API_GetChannelList():
	msg = 'ok'
	version = '1.0'
	errorcode = 0
	itemlists = []
	ret_json = {}
	itemlistname = "data"
	channellist = Channel.objects.all().filter(status=1)

	for i in channellist:
		itemlist = {
			u"id" : i.id,
			u"channelnum" : i.channelnum,
			u"description": i.description,
			u"addtime" : i.addtime,
			u"status" : i.status,
			u"opuser" : i.opuser
		}
		itemlists.append(itemlist)

	ret_json =myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlists)
	logger.debug(ret_json)
	return ret_json

def API_GetSearchChannelData():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	itemlist = []
	filetypelist = []
	ret_json = {}
	itemlistnames = []
	datalists = []
	channellist = Channel.objects.all().filter(status=1)
	typelist = FileType.objects.all()

	for i in channellist:
		itemlist.append(i.description)
	itemlistnames.append("channellist")
	datalists.append(itemlist)

	for j in typelist:
		filetypelist.append(j.description)
	itemlistnames.append("filetypelist")
	datalists.append(filetypelist)

	ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, datalists)
	logger.debug(ret_json)
	return ret_json

def API_GetSearchPluginData():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	itemlist = []
	pluginverlistset = set()
	pluginverlist = []
	ret_json = {}
	itemlistnames = []
	itemlists = []
	channellist = Channel.objects.all().filter(status=1)
	pluginlist = Plugin.objects.all()

	for i in channellist:
		itemlist.append(i.description)
	itemlistnames.append("channellist")
	itemlists.append(itemlist)

	for i in pluginlist:
		pluginverlistset.add(i.plugintype)

	for i in pluginverlistset:
		pluginverlist.append(i)
	itemlistnames.append("plugintypelist")
	itemlists.append(pluginverlist)

	ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, itemlists)
	logger.debug(ret_json)
	return ret_json

def API_GetSearchPackageData():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	itemlist = []
	packageverlistset = set()
	packageverlist = []
	ret_json = {}
	itemlistnames = []
	itemlists = []
	channellist = Channel.objects.all().filter(status=1)
	packagelist = Package.objects.all()

	for i in channellist:
		itemlist.append(i.description)
	itemlistnames.append("channellist")
	itemlists.append(itemlist)

	for i in packagelist:
		packageverlistset.add(i.apkver)

	for i in packageverlistset:
		packageverlist.append(i)
	itemlistnames.append("packagelist")
	itemlists.append(packageverlist)

	ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, itemlists)
	logger.debug(ret_json)
	return ret_json

def API_GetSearchHostData():
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	itemlist = []
	hostverlistset = set()
	itemlist2 = []
	itemlist3 = []
	ret_json = {}
	itemlistnames = []
	itemlists = []
	channellist = Channel.objects.all().filter(status=1)
	hostverlist = HostVer.objects.all().filter(status=1)
	filetypelist = FileType.objects.all()

	for i in channellist:
		itemlist.append(i.description)
	itemlistnames.append("channellist")
	itemlists.append(itemlist)

	for i in hostverlist:
		hostverlistset.add(i.hostver)

	for i in hostverlistset:
		itemlist2.append(i)
	itemlistnames.append("hostverlist")
	itemlists.append(itemlist2)

	for i in filetypelist:
		itemlist3.append(i.description)
	itemlistnames.append("filetypelist")
	itemlists.append(itemlist3)

	ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, itemlists)
	logger.debug(ret_json)
	return ret_json

def API_SearchChannel(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	datalist = []
	# itemlistnames = []
	# itemlists = []
	itemlistname = "datalist"
	channel = received_json_data.get('channel', None)
	filetype = received_json_data.get('filetype', None)
	logger.debug(channel)
	logger.debug(filetype)

	if filetype:
		records = PublishRecord.objects.all().filter(filetype=filetype, channel__contains=channel).order_by('-publishtime')
		for i in records:
			templist = {
			u"id" : i.id,
			u"publishtime" : i.publishtime,
			u"filetype" : i.filetype,
			u"channel" : i.channel,
			u"details" : i.details,
			u"filepath" : i.filepath,
			u"user" : i.opuser
			}
			datalist.append(templist)

		ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, datalist)
	else:
		records = PublishRecord.objects.all().filter(channel__contains=channel).order_by('-publishtime')
		for i in records:
			templist = {
			u"id" : i.id,
			u"publishtime" : i.publishtime,
			u"filetype" : i.filetype,
			u"channel" : i.channel,
			u"details" : i.details,
			u"filepath" : i.filepath,
			u"user" : i.opuser
			}
			datalist.append(templist)
		ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, datalist)
	# itemlistnames.append("datalist")
	# itemlists.append(templist)
	# elif filetypetemp.id == 2:
	# 	plugins = Plugin.objects.all().filter(channel=channeltemp.channelnum)
	# 	for i in plugins:
	# 		templist = {
	# 		u"publishid" : i.publishid,
	# 		u"pluginver" : i.pluginver,
	# 		u"hostver" : i.hostver,
	# 		u"pluginpath" : i.pluginpath,
	# 		u"pluginmd5" : i.pluginmd5,
	# 		u"plugintype" : i.plugintype,
	# 		u"pluginsize" : i.pluginsize,
	# 		u"channel" : i.channel
	# 		}
	# 		datalist.append(templist)
	# 	itemlistnames.append("datalist")
	# 	itemlists.append(templist)

	# itemlistnames.append("filetype")
	# itemlists.append(filetypetemp.description)
	# ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, itemlists)
	
	logger.debug(ret_json)
	return ret_json

def API_SearchPlugin(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	itemlist = []
	itemlistname = "datalist"
	channel = received_json_data.get('channel', None)
	plugintype = received_json_data.get('plugintype', None)
	logger.debug(channel)
	logger.debug(plugintype)
	channel_temp = Channel.objects.all().get(description=channel) 
	# logger.debug(channel_temp.channelnum)
	if plugintype:
		logger.debug("plugintype is not null")
		plugins = Plugin.objects.all().filter(plugintype=plugintype, channel=channel_temp.channelnum).order_by('-publishtime')
	else:
		logger.debug("plugintype is null")
		plugins = Plugin.objects.all().filter(channel=channel_temp.channelnum).order_by('-publishtime')
	for i in plugins:
		templist = {
		u"publishid" : i.publishid,
		u"pluginver" : i.pluginver,
		u"hostver" : i.hostver,
		u"pluginpath" : i.pluginpath,
		u"pluginmd5" : i.pluginmd5,
		u"plugintype" : i.plugintype,
		u"pluginsize" : i.pluginsize,
		u"channel" : i.channel,
		u"publishtime": i.publishtime
		}
		itemlist.append(templist)

	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlist)
	logger.debug(ret_json)
	return ret_json

def API_SearchPackage(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	itemlist = []
	itemlistname = "datalist"
	channel = received_json_data.get('channel', None)
	apkver = received_json_data.get('apkver', None)
	isallver = received_json_data.get('isallver', None)
	channel_temp = Channel.objects.all().get(description=channel) 
	if isallver == 1:
		logger.debug("apkver is null")
		packages = Package.objects.all().filter(channel=channel_temp.channelnum).order_by('-publishtime')
	else:
		logger.debug("apkver is not null")
		packages = Package.objects.all().filter(apkver=apkver, channel=channel_temp.channelnum).order_by('-publishtime')
	for i in packages:
		templist = {
		u"publishid" : i.publishid,
		u"apkver" : i.apkver,
		u"hostver" : i.hostver,
		u"packagepath" : i.packagepath,
		u"channel" : i.channel,
		u"publishtime": i.publishtime,
		u"apkpluginfo" : i.apkpluginfo
		}
		itemlist.append(templist)

	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlist)
	logger.debug(ret_json)
	return ret_json

def API_SearchHostver(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	# itemlist = []
	# itemlistname = "datalist"
	packagelist = []
	pluginlist = []
	itemlistnames = []
	datalists = []
	channel = received_json_data.get('channel', None)
	hostver = received_json_data.get('hostver', None)
	# filetype = received_json_data.get('filetype', None)

	# filetype_temp = FileType.objects.all().get(description=filetype)
	channel_temp = Channel.objects.all().get(description=channel)
	# if filetype_temp.type == 'package':
	packages = Package.objects.all().filter(hostver=hostver, channel=channel_temp.channelnum).order_by('-publishtime')
	for i in packages:
		templist = {
		u"publishid" : i.publishid,
		u"apkver" : i.apkver,
		u"hostver" : i.hostver,
		u"packagepath" : i.packagepath,
		u"channel" : i.channel,
		u"publishtime": i.publishtime,
		u"apkpluginfo" : i.apkpluginfo
		}
		packagelist.append(templist)
	# elif filetype_temp.type == 'plugin':
		# logger.debug("插件")
	itemlistnames.append("packagelist")
	datalists.append(packagelist)
	plugins = Plugin.objects.all().filter(hostver__contains=hostver, channel=channel_temp.channelnum).order_by('-publishtime')
	for i in plugins:
		templist2 = {
		u"publishid" : i.publishid,
		u"pluginver" : i.pluginver,
		u"hostver" : i.hostver,
		u"pluginpath" : i.pluginpath,
		u"pluginmd5" : i.pluginmd5,
		u"plugintype" : i.plugintype,
		u"pluginsize" : i.pluginsize,
		u"channel" : i.channel,
		u"publishtime": i.publishtime
		}
		pluginlist.append(templist2)
	itemlistnames.append("pluginlist")
	datalists.append(pluginlist)
	# itemlistnames.append("filetype")
	# datalists.append(filetype)
	ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, datalists)
	logger.debug(ret_json)
	return ret_json	

def API_AddChannel(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	description = received_json_data.get('decription', None)
	channelnum = received_json_data.get('channelnum', None)
	addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	status = 1

	temp1 = Channel.objects.all().filter(channelnum=channelnum)
	temp2 = Channel.objects.all().filter(description=description)

	if temp1 or temp2:
		logger.debug("重复渠道")
		ret_json = myjson.generatecommonjson("该渠道已存在", -1, version)
		return ret_json

	newChannel = Channel(channelnum=channelnum, description=description, addtime=addtime, status=status)
	newChannel.save()
	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json

def API_AddHostver(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	hostver = received_json_data.get('hostver', None)
	#不允许添加重复的宿主版本号
	temp = HostVer.objects.all().filter(hostver=hostver)
	logger.debug("宿主版本号")
	if temp:
		logger.debug("重复宿主版本号")
		ret_json = myjson.generatecommonjson("该宿主版本号已存在", -1, version)
		return ret_json

	addtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	status = 1
	newHostver = HostVer(hostver=hostver, addtime=addtime, status=status)
	newHostver.save()
	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json

def API_PSChannelChange(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	pluginset = set()
	itemlist = []
	itemlistname = 'plugintypelist'
	channel = received_json_data.get('channel', None)
	logger.debug(channel)
	channeltemp = Channel.objects.all().get(description=channel)
	plugins = Plugin.objects.all().filter(channel = channeltemp.channelnum)
	for i in plugins:
		pluginset.add(i.plugintype)

	for i in pluginset:
		itemlist.append(i)
	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlist)
	return ret_json

def API_APKSChannelChange(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	apkverset =set()
	itemlist = []
	itemlistname = 'apkverlist'
	channel = received_json_data.get('channel', None)
	logger.debug(channel)
	channeltemp = Channel.objects.all().get(description=channel)
	apkverlist = Package.objects.all().filter(channel = channeltemp.channelnum)
	for i in apkverlist:
		apkverset.add(i.apkver)

	for i in apkverset:
		itemlist.append(i)

	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlist)
	logger.debug(ret_json)
	return ret_json

def API_HSChannelchange(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	hostverset =set()
	itemlist = []
	itemlistname = 'hostverlist'
	channel = received_json_data.get('channel', None)
	logger.debug(channel)
	channeltemp = Channel.objects.all().get(description=channel)
	hostverlist = Package.objects.all().filter(channel = channeltemp.channelnum)
	for i in hostverlist:
		temp = i.hostver.strip('\r\n')
		hostverset.add(temp)

	hostverlist = Plugin.objects.all().filter(channel = channeltemp.channelnum)
	for i in hostverlist:
		temp = i.hostver.strip('\r\n')
		hostverset.add(temp)

	for i in hostverset:
		itemlist.append(i)

	ret_json = myjson.generateitemjson(msg, errorcode, version, itemlistname, itemlist)
	return ret_json

def API_GetPublishDetailById(received_json_data):
	msg = 'ok'
	version = '1.0'
	errorcode = 'null'
	ret_json = {}
	pluginlist = []
	itemlistnames = []
	datalists = []

	publishid = received_json_data.get('id', None)
	logger.debug(publishid)

	package = Package.objects.all().get(id=publishid)
	plugins = Plugin.objects.all().filter(publishid=package.id)
	for i in plugins:
		templist = {
			u"id" : i.id,
			u"publishid" : i.publishid,
			u"pluginver" : i.pluginver,
			u"hostver" : i.hostver,
			u"pluginmd5" : i.pluginmd5,
			u"plugintype": i.plugintype,
			u"pluginsize" : i.pluginsize,
			u"channel" : i.channel,
			u"publishtime" : i.publishtime
		}
		pluginlist.append(templist)

	try:
		channel = Channel.objects.all().filter(channelnum=package.channel)
		tempchannel = str(channel[0].channelnum) + '(' + channel[0].description + ')'
	except:
		tempchannel = package.channel
	item = {
	u"id" : package.id,
	u"apkver" : package.apkver,
	u"packagepath" : package.packagepath,
	u"hostver" : package.hostver,
	u"packagemd5" : package.packagemd5,
	u"packagesize": package.packagesize,
	u"channel" : tempchannel,
	u"publishtime" : package.publishtime,
	u"iidcode" : package.iid_code,
	u"flag" : package.flag,
	u"opuser" : package.opuser,
	u"remarks" : package.remarks,
	u"issync" : package.issync,
	u"pluginfo" : pluginlist
	}
	

	ret_json = myjson.generateitemjson(msg, errorcode, version, "packagedetails", item)
	return ret_json

def API_SynChannelRecord(rec_json_data, user, username):
	msg = 'ok'
	version = '1.0'
	errorcode = '0'
	channeltext = ""

	synid = rec_json_data.get('synrecordid', None)
	channellist = rec_json_data.get('channellist', None)
	logger.debug(synid)
	logger.debug(channellist)
	logger.debug(user)

	# if synid != None:
	# 	record = PublishRecord.objects.get(id=synid)
	# 	logger.debug(record.channel)
	# 	text = record.channel.strip("\r\n")
	# 	channeltemp = Channel.objects.get(description=text)
	# 	logger.debug(channeltemp)
	# 	logger.debug(channeltemp.channelnum)

	if channellist == None:
		return

	# for i in channellist:
	# 	channeltext = channeltext + str(i) + "\r\n"

	#publishtime不对
	syntime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
	logger.debug(syntime)

	logger.debug("==============开始同步==============")
	rec_pacakge = Package.objects.get(id=synid)
	logger.debug(rec_pacakge)
	# logger.debug(rec_pacakge[0])
	for i in channellist:
		m = re.match('(\d+)(.)', str(i))
		channel = m.group(1)
		API_CreatePackage(rec_pacakge.apkver, rec_pacakge.packagepath, rec_pacakge.hostver, rec_pacakge.packagemd5, rec_pacakge.packagesize, channel, syntime, rec_pacakge.iid_code, rec_pacakge.flag, username, rec_pacakge.remarks, issync=1)
		packagerecord = Package.objects.all().order_by('-id')
		logger.debug(packagerecord[0].id)
		plugins = Plugin.objects.all().filter(publishid=rec_pacakge.id)
		for p in plugins:
			API_CreatePlugin(packagerecord[0].id, p.pluginver, p.hostver, p.pluginmd5, p.plugintype, p.pluginsize, channel, syntime)

	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json

def API_AddRecord(jsondata, user, username):
	msg = "ok"
	version = "1.0"
	errorcode = 0
	itemname ="data"
	item = {}

	logger.debug("API_AddRecord")
	logger.debug(user)
	logger.debug(username)


	hostver = jsondata.get("hostver")
	apkver = jsondata.get("apkver")
	packagepath = jsondata.get("packagepath")
	packagesize = jsondata.get("packagesize")
	logger.debug("gggggggggg:" + packagesize)
	packagemd5 = jsondata.get("packagemd5")
	channel = jsondata.get("channel")
	publishtime = jsondata.get("publishtime")
	iid_code = jsondata.get("iidcode")
	logger.debug("gggggggggg:" + str(iid_code))
	remarks = jsondata.get("remarks")
	flag = jsondata.get("flag")
	logger.debug(flag)
	API_CreatePackage(apkver, packagepath, hostver, packagemd5, packagesize, channel, publishtime, iid_code, flag, username, remarks)

	hv = HostVer.objects.all().filter(hostver=hostver)
	if not hv:
		logger.debug("need to add hostver")
		API_CreateHostver(hostver)

	a = ApkVer.objects.all().filter(apkver=apkver)
	if not a:
		logger.debug("need to add apkver")
		API_CreateApkver(apkver)

	i = IIDcode.objects.all().filter(iidcode=iid_code)
	if not i:
		logger.debug("need to add iidcode")
		API_CreateIIDcode(iid_code)

	c = Channel.objects.all().filter(channelnum=channel)
	if not c:
		logger.debug("need to add channel")
		API_CreateChannel(channel, username)

	pluginfo = jsondata.get("pluginfo")
	for i in pluginfo:
		logger.debug(i)
		pluginver = i["pluginver"]
		pluginhostver = i["hostver"]
		pluginmd5 = i["pluginmd5"]
		plugintype = i["plugintype"]
		pluginsize = i["pluginsize"]


		p = PluginVer.objects.all().filter(pluginver=pluginver)
		if not p:
			logger.debug("need to add pluginver")
			API_CreatePluginver(pluginver)

		packagerecord = Package.objects.all().order_by('-id')
		logger.debug(packagerecord[0].id)
		API_CreatePlugin(packagerecord[0].id, pluginver, pluginhostver, pluginmd5, plugintype, pluginsize, channel, publishtime)
	item = {
		u'id': packagerecord[0].id
	}
	ret_json = myjson.generateitemjson(msg, errorcode, version, itemname, item)
	return ret_json

def API_GetPackageInfoByid(jsondata):
	msg = 'ok'
	version = '1.0'
	errorcode = 0
	item = {}

	pid = jsondata.get("id")
	logger.debug(pid)
	package = Package.objects.all().get(id=pid)
	item = {
	u"id" : package.id,
	u"apkver" : package.apkver,
	u"packagepath" : package.packagepath,
	u"hostver" : package.hostver,
	u"packagemd5" : package.packagemd5,
	u"packagesize": package.packagesize,
	u"channel" : package.channel,
	u"publishtime" : package.publishtime,
	u"iidcode" : package.iid_code,
	u"flag" : package.flag,
	u"remarks" : package.remarks,
	u"issync" : package.issync
	}

	ret_json = myjson.generateitemjson(msg, errorcode, version, "packageinfo", item)
	return ret_json

def API_SaveRecordById(jsondata, user):
	msg = 'ok'
	version = "1.0"
	errorcode = 0

	pid =jsondata.get("id")
	hostver = jsondata.get("hostver")
	apkver = jsondata.get("apkver")
	packagepath = jsondata.get("packagepath")
	packagesize = jsondata.get("packagesize")
	packagemd5 = jsondata.get("packagemd5")
	channel = jsondata.get("channel")
	publishtime = jsondata.get("publishtime")
	iid_code = jsondata.get("iidcode")
	remarks = jsondata.get("remarks")
	flag = jsondata.get("flag")

	API_ModifyPackage(pid, apkver, packagepath, hostver, packagemd5, packagesize, channel, publishtime, iid_code, flag, remarks)
	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json

def API_DeleteRecordById(jsondata, user):
	msg = "ok"
	version = "1.0"
	errorcode = 0

	pid = jsondata.get("id")
	package = Package.objects.all().get(id=pid)
	package.delete()

	try:
		Plugin.objects.all().filter(publishid=pid).delete()
	except ObjectDoesNotExist:
		pass

	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json

def API_SearchText(jsondata):
	msg = 'ok'
	version = "1.0"
	errorcode = 0
	datalist = []
	publishidlist = set()

	text = jsondata.get("searchtext", None)
	logger.debug(text)
	pv = Plugin.objects.all().filter(pluginver=text)
	if pv:
		logger.debug("find some result from plugin...")
		plugins = Plugin.objects.all().filter(pluginver=text)
		for i in pv:
			logger.debug(i.pluginver)
			logger.debug(i.publishid)
			publishidlist.add(i.publishid)

		logger.debug(publishidlist)

		for i in publishidlist:
			try:
				p = Package.objects.all().get(id =i)
			except ObjectDoesNotExist:
				continue

			templist = {
				u"id" : p.id,
				u"apkver" : p.apkver,
				u"packagepath" : p.packagepath,
				u"hostver" : p.hostver,
				u"packagemd5" : p.packagemd5,
				u"packagesize": p.packagesize,
				u"channel" : p.channel,
				u"publishtime" : p.publishtime,
				u"iidcode" : p.iid_code,
				u"opuser" : p.opuser,
				u"flag" : p.flag,
				u"remarks" : p.remarks
			}
			datalist.append(templist)

		ret_json = myjson.generateitemjson(msg, errorcode, version, "datalist", datalist)
		return ret_json

	ic = Package.objects.all().filter(iid_code=text)
	if ic:
		logger.debug("find some result from iidcode...")

		for i in ic:
			templist = {
				u"id" : i.id,
				u"apkver" : i.apkver,
				u"packagepath" : i.packagepath,
				u"hostver" : i.hostver,
				u"packagemd5" : i.packagemd5,
				u"packagesize": i.packagesize,
				u"channel" : i.channel,
				u"publishtime" : i.publishtime,
				u"iidcode" : i.iid_code,
				u"opuser" : i.opuser,
				u"flag" : i.flag,
				u"remarks" : i.remarks
			}
			datalist.append(templist)

		ret_json = myjson.generateitemjson(msg, errorcode, version, "datalist", datalist)
		return ret_json

	msg = "no item match..."
	errorcode = -1
	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json

def API_SaveChannelById(jsondata, user, username):
	msg = 'ok'
	version = "1.0"
	errorcode = 0
	pid = jsondata.get("pid")
	channelnum = jsondata.get("channelnum")
	logger.debug(channelnum)
	description = jsondata.get("description")
	API_ModityChannel(pid, channelnum, username, description)
	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return ret_json
