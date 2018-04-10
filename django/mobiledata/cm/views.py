# !/usr/bin/env python
# encoding=utf-8
# Date:    2016-10-20
# Author:  pangjian
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from models import SideBar, SideBarGroup, PublishRecord, Package
# from rest_framework import viewsets
# from serializer import SideBarSerializer, SideBarGroupSerializer, PublishRecordSerializer
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponseRedirect
import logging
import json
import traceback

from .import apifuncs
from common import myjson, myhttpresponse

logger = logging.getLogger('mobiledata_cm')

# Create your views here.

def verifylogin(func):
	def wrapfunc(*args):
		if not args[0].user.is_authenticated():
			msg = "请先登录，谢谢"
			errorcode = "403"
			version = "1.0"
			logger.debug("user is not login...")
			return myhttpresponse.json_response(myjson.generatecommonjson(msg, errorcode, version))
		return func(*args)
	return wrapfunc


def index(request):
	test = 'ok'
	template = loader.get_template('templates\index.html')
	context = {
		'ret': test,
	}
	return HttpResponse(template.render(context, request))

# sidebar接口定义：返回侧边栏信息
# {
# "grouplist":[
# 	{
#     "groupname":"查询",
#     "sidebars":[
#     {"name": "宿主查询", "url":"http://127.0.0.1:8080/cm/host/"},
#     {"name": "apk包查询","url":"http://127.0.0.1:8080/cm/package/"},
#     {"name": "插件查询", "url":"http://127.0.0.1:8080/cm/plugin/"}]
# 	},

#     {
#     "groupname":"工具",
#     "sidebars":	[{"name": "apk包解析", "url":"http://127.0.0.1:8080/cm/tool/packagedetail/"}]
#     },

#     {
#      "groupname":"外链",
#      "sidebars":	[
# 	{"name": "提测合格率", "url":"http://update.rdev.kingsoft.net:8089/addstats/"},
# 	{"name": "手机资产", "url":"http://update.rdev.kingsoft.net:8089/phonemanager/"}]
# 	}
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def sidebar(request):
	logger.error("svdfdfe")
	jsondata = apifuncs.API_GetSideBarInfo()
	return HttpResponse(jsondata, content_type='application/json')


@csrf_exempt
def sidebargroup(request):
	test_data = {}
	test_data['msg'] = 'ok'
	test_data['group'] = ['sdf', 'sfe', 'fee']
	return HttpResponse(json.dumps(test_data), content_type='application/json')


# class JSONResponse(HttpResponse):
# 	"""docstring for JSONResponse"""
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)


# regist接口定义：返回注册是否成功信息
# {
# "version":"1.0",
# "errorcode":"-1",
# "msg":"the mail has been regist by other user!!"
# }
# {
# "version":"1.0",
# "errorcode":"0",
# "msg":"regist success"
# }
@csrf_exempt
def regist(request):
	msg = ""
	errorcode = ""
	if request.method == 'POST':
		email = request.POST.get("email")
		password = request.POST.get("password")
		if email == None or password == None:
			logger.debug("get from json data...")
			jsondata = json.loads(request.body)
			email = jsondata.get("email", None)
			password = jsondata.get("password", None)
		firstname = ""
		maillist = ['kingsoft.com', 'conew.com', 'cmcm.com', 'ijinshan.com']

		try:
			str = email.split("@")
			firstname = str[0]
			if str[1] not in maillist:
				msg = "请使用公司邮箱注册"
				errorcode = "-2"
				ret = myjson.generatecommonjson(msg, errorcode, "1.0")
				return HttpResponse(ret, content_type= 'application/json')
		except:
			msg = "error email format!"
			errorcode = "-3"
			ret = myjson.generatecommonjson(msg, errorcode, "1.0")
			return	HttpResponse(ret, content_type='application/json')

		try:
			user = User.objects.get(username = email)
			msg = "the mail has been regist by other user!!"
			errorcode = "-1"
		except ObjectDoesNotExist:
			user = User.objects.create_user(username = email, password = password, first_name = firstname, email= email)
			msg = "regist success"
			errorcode = "0"

		ret = myjson.generatecommonjson(msg, errorcode, "1.0")
		return HttpResponse(ret, content_type='application/json')

# userlogin接口定义：返回登录是否成功信息
# {
# "version":"1.0",
# "errorcode":"-1",
# "msg":"username/email or password wrong!!"
# }
# {
# "version":"1.0",
# "errorcode":"0",
# "msg":"login success"
# }
@csrf_exempt
def userlogin(request):
	msg = ""
	errorcode = ""
	if request.method == 'POST':
		try:
			email = request.POST.get("email")
			password = request.POST.get("password")
			if email == None or password == None:
				logger.debug("get from json data...")
				jsondata = json.loads(request.body)
				email = jsondata.get("email", None)
				password = jsondata.get("password", None)

			user = authenticate(username=email, password = password)
			if user is not None:
				logger.debug("login success")
				login(request, user)
				msg = "login success"
				errorcode = "0"
				ret = myjson.generatecommonjson(msg, errorcode, "1.0")
				response = HttpResponse(ret, content_type='application/json')
				response.set_cookie(u"email", user.first_name, max_age=259200)
				return response
			else:
				logger.debug("login failed")
				msg = "username/email or password wrong!!"
				errorcode = "-1"
				ret = myjson.generatecommonjson(msg, errorcode, "1.0")
				response = HttpResponse(ret, content_type='application/json')
				return response
		except Exception,e:
			traceback.print_exc()
			msg = str(e)
			errorcode = "-1"
			ret = myjson.generatecommonjson(msg, errorcode, "1.0")
			return myhttpresponse.json_response(ret)


# logout接口定义：无返回数据
@csrf_exempt
def userlogout(request):
	response = HttpResponseRedirect('/mobiledata/')
	response.delete_cookie(u"email")
	logout(request)
	return response

# productlist接口定义
# {
# "selectlist":[
# 	{
#     "name":"product",
#     "itemlist":[
#     {"itemname": "cm", "description":"猎豹清理大师"}]
# 	},

#     {
#     "name":"filetype",
#     "itemlist":	[{"itemname": "apk包解析", "description":"安装包"},
# {"itemname": "plugin", "description":"插件"}
# ]
#     },

#     {
#      "name":"channel",
#      "itemlist":	[
# 	{"itemname": "cms推cm", "channel":"100039"},
# 	{"itemname": "电池医生渠道", "channel":"100005"},
#         {"itemname": "手助全渠道", "channel":"100003"}
# ]
# 	}
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def selectlist(request):
	retjson = apifuncs.API_GetSelectList()
	return HttpResponse(retjson, content_type='application/json')

# submitpublishdata接口定义：返回提交数据是否成功信息
# {
# "version":"1.0",
# "errorcode":"-1",
# "msg":"xxx!"
# }
# {
# "version":"1.0",
# "errorcode":"0",
# "msg":"submit success!"
# }
@csrf_exempt
def submitpublishdata(request):
	return HttpResponse('forbit')
	msg = ""
	errorcode = ""
	if request.method == "POST":
		try:
			received_json_data =json.loads(request.body)
		except:
			msg = "get data error!"
			errorcode = "-1"
			ret_json = myjson.generatecommonjson(msg, errorcode, "1.0")
			response = HttpResponse(ret_json, content_type='application/json')
			return response

		username = request.COOKIES.get("email", '')
		logger.debug(username)
		user = request.user

		ret_json = apifuncs.API_AddPublishRecord(received_json_data, user, username)
		# ret = myjson.generatecommonjson(msg, errorcode, "1.0")
		response = HttpResponse(ret_json, content_type='application/json')
		return response

# getpublishdata接口定义
# {
# "datalist":[
# 	{
#     "id":1,
#     "filetype":"安装包",
#     "channel":"电池医生渠道",
#     "publishtime":"2016-10-25",
#     "文件地址":"",
#     "details":"测试"
# 	}
# ],
# "pagecount":"20",
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def getpublishdata(request):
	if request.method == "POST":
		try:
			received_json_data =json.loads(request.body)
			retjson =apifuncs.API_GetPublishData(received_json_data)
			return HttpResponse(retjson, content_type='application/json')
		except Exception,e:
			traceback.print_exc()
			return HttpResponse('can not get data from post')


# gethostverdata接口定义
# {
# {
# "datalist": [
# {"id" : "1", "hostver":"10100036"},
# {"id" : "2", "hostver":"2323232423"},
# {"id" : "3", "hostver":"454546466"}
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
# }
@csrf_exempt
def gethostverdata(request):
	if request.method == "GET":
		retjson = apifuncs.API_GetHostVer()
		return HttpResponse(retjson, content_type='application/json')

# getsearchchanneldata接口定义
# {
# "channellist": [
# "手助渠道",
# "应用宝渠道",
# "电池医生渠道"
# ],
# "filetypelist":[
# "安装包",
# "插件"
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def getsearchchanneldata(request):
	if request.method == "GET":
		retjson = apifuncs.API_GetSearchChannelData()
		return HttpResponse(retjson, content_type='application/json')
	return True

# getsearchplugindata接口定义
# {
# "channellist": [
# "手助渠道",
# "应用宝渠道",
# "电池医生渠道"
# ],
# "pluginverlist":[
# "1232324",
# "565775634"
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def getsearchplugindata(request):
	if request.method == "GET":
		retjson = apifuncs.API_GetSearchPluginData()
		return HttpResponse(retjson, content_type='application/json')
	return False

# getsearchpackagedata接口定义
# {
# "channellist": [
# "手助渠道",
# "应用宝渠道",
# "电池医生渠道"
# ],
# "apkverlist":[
# "123232455",
# "565775634"
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def getsearchpackagedata(request):
	if request.method == "GET":
		retjson = apifuncs.API_GetSearchPackageData()
		return HttpResponse(retjson, content_type='application/json')
	return False

# getsearchhostdata接口定义
# {
# "channellist": [
# "手助渠道",
# "应用宝渠道",
# "电池医生渠道"
# ],
# "hostverlist":[
# "123232455",
# "565775634"
# ],
# "filetypelist":[
# "安装包",
# "插件"
# ],
# "version":"1.0",
# "errorcode":"null",
# "msg":"ok"
# }
@csrf_exempt
def getsearchhostdata(request):
	if request.method == "GET":
		retjson = apifuncs.API_GetSearchHostData()
		return HttpResponse(retjson, content_type='appliacation/json')
	return False

# searchchannel接口定义
# {
#     "msg":"ok",
#     "errorcode":"null",
#     "datalist":[
#         {
#             "filepath":"",
#             "filetype":"安装包",
#             "publishtime":"2016-10-18",
#             "details":"xcvxcv",
#             "id":19,
#             "channel":"手助全渠道",
#             "user":null
#         },
#         {
#             "filepath":"",
#             "filetype":"安装包",
#             "publishtime":"2016-10-03",
#             "details":"sdfe",
#             "id":25,
#             "channel":"手助全渠道",
#             "user":null
#         }
#     ],
#     "version":"1.0"
# }
@csrf_exempt
def searchchannel(request):
	if request.method == 'POST':
		try:
			received_json_data = json.loads(request.body)
			ret_json = apifuncs.API_SearchChannel(received_json_data)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			traceback.print_exc()
			return HttpResponse('get data error')

# searchplugin接口定义
# {
#     "msg":"ok",
#     "errorcode":"null",
#     "datalist":[
#         {
#             "plugintype":"uniform",
#             "pluginmd5":"51d5100c0c7bc9e0db538275ee1bb7",
#             "pluginver":"10010216100121",
#             "pluginpath":"",
#             "channel":"100005",
#             "publishid":37,
#             "pluginsize":"4255819",
#             "hostver":"10100036 "
#         }
#     ],
#     "version":"1.0"
# }
@csrf_exempt
def searchplugin(request):
	if request.method == 'POST':
		try:
			received_json_data = json.loads(request.body)
			ret_json = apifuncs.API_SearchPlugin(received_json_data)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			traceback.print_exc()
			return HttpResponse('get data error')

# searchpackage接口定义
# {
#     "msg":"ok",
#     "errorcode":"null",
#     "datalist":[
#         {
#             "channel":"100005",
#             "publishid":20,
#             "hostver":"False",
#             "apkver":"51481004",
#             "packagepath":""
#         }
#     ],
#     "version":"1.0"
# }
@csrf_exempt
def searchpackage(request):
	if request.method == 'POST':
		try:
			received_json_data = json.loads(request.body)
			ret_json = apifuncs.API_SearchPackage(received_json_data)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			traceback.print_exc()
			return HttpResponse('get data error')

# searchhostver接口定义
# {
#     "msg":"ok",
#     "errorcode":"null",
#     "datalist":[
#         {
#             "plugintype":"uniform",
#             "pluginmd5":"51d5100c0c7bc9e0db538275ee1bb7",
#             "pluginver":"10010216100121",
#             "pluginpath":"",
#             "channel":"100005",
#             "publishid":37,
#             "pluginsize":"4255819",
#             "hostver":"10100036 "
#         }
#     ],
#     "version":"1.0",
#     "filetype":"插件"
# }
@csrf_exempt
def searchhostver(request):
	if request.method == 'POST':
		try:
			received_json_data = json.loads(request.body)
			ret_json = apifuncs.API_SearchHostver(received_json_data)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			traceback.print_exc()
			return HttpResponse('get data error')

@csrf_exempt
def addchannel(request):
	if request.method == 'POST':
		try:
			received_json_data = json.loads(request.body)
			ret_json = apifuncs.API_AddChannel(received_json_data)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			msg = str(e)
			errorcode = -1
			version = "1.0"
			return myhttpresponse.json_response(myjson.generatecommonjson(msg, errorcode, version), True)

@csrf_exempt
def addhostver(request):
	if request.method == 'POST':
		try:
			received_json_data = json.loads(request.body)
			ret_json = apifuncs.API_AddHostver(received_json_data)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			traceback.print_exc()
			return HttpResponse(traceback.print_exc())

@csrf_exempt
def ps_channelchange(request):
	try:
		received_json_data =json.loads(request.body)
		ret_json = apifuncs.API_PSChannelChange(received_json_data)
		return HttpResponse(ret_json, content_type='application/json')
	except Exception,e:
		traceback.print_exc()
		return HttpResponse('ps_channelchange error')

@csrf_exempt
def apks_channelchange(request):
	try:
		received_json_data =json.loads(request.body)
		ret_json = apifuncs.API_APKSChannelChange(received_json_data)
		return HttpResponse(ret_json, content_type='application/json')
	except Exception,e:
		traceback.print_exc()
		return HttpResponse('apk_channelchange error')

@csrf_exempt
def hs_channelchange(request):
	try:
		received_json_data = json.loads(request.body)
		ret_json = apifuncs.API_HSChannelchange(received_json_data)
		return HttpResponse(ret_json, content_type='application/json')
	except Exception,e:
		traceback.print_exc()
		return HttpResponse('hs_channelchange error')

@csrf_exempt
def getpublishdetailbyid(request):
	try:
		received_json_data = json.loads(request.body)
		ret_json = apifuncs.API_GetPublishDetailById(received_json_data)
		return HttpResponse(ret_json, content_type='application/json')
	except Exception,e:
		msg = str(e)
		errorcode = -1
		version = "1.0"
		return myhttpresponse.json_response(myjson.generatecommonjson(msg, errorcode, version))

@csrf_exempt
@verifylogin
def synchannelrecord(request):
	if request.method == "POST":
		try:
			received_json_data = json.loads(request.body)
			user = request.user
			username = str(user).split('@')[0]
			ret_json = apifuncs.API_SynChannelRecord(received_json_data, user, username)
			return HttpResponse(ret_json, content_type='application/json')
		except Exception,e:
			msg = str(e)
			errorcode = -1
			version = "1.0"
			ret_json = myjson.generatecommonjson(msg, errorcode, version)
			return myhttpresponse.json_response(ret_json, True)
# 获取渠道号列表
# {
# "msg": "ok",
# "errorcode": "0",
# "data":[
# "500092",
# "500091",
# "500093",
# "500094",
# "500095",
# "500096",
# "全网渠道"
# ],
# "version": "1.0"
# }
@csrf_exempt
def getchannellist(request):
	if request.method == 'GET':
		try:
			ret_json = apifuncs.API_GetChannelList()
			return myhttpresponse.json_response(ret_json, True)
		except Exception as e:
			msg = str(e)
			# logger.debug(msg)
			errorcode = -1
			version = "1.0"
			ret_json = myjson.generatecommonjson(msg, errorcode, version)
			return myhttpresponse.json_response(ret_json, True)
	else:
		msg = 'http method is not GET, return...'
		errorcode = -1
		version = "1.0"
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return myhttpresponse.json_response(ret_json, True)

@csrf_exempt
@verifylogin
def addrecord(request):
	if request.method == 'POST':
		try:
			jsondata = json.loads(request.body)
			user = request.user
			username = str(user).split('@')[0]
			ret_json = apifuncs.API_AddRecord(jsondata, user, username)
			return myhttpresponse.json_response(ret_json, True)
		except Exception as e:
			traceback.print_exc()
		 	msg = str(e)
		 	errorcode = -1
		 	version = "1.0"
		 	ret_json = myjson.generatecommonjson(msg, errorcode, version)
		 	return myhttpresponse.json_response(ret_json, True)
	else:
		msg = "http method is not POST, return..."
		errorcode = -1
		version = "1.0"
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return myhttpresponse.json_response(ret_json, True)

@csrf_exempt
def editrecordbyid(request):
	try:
		jsondata = json.loads(request.body)
		ret_json = apifuncs.API_GetPackageInfoByid(jsondata)
		return myhttpresponse.json_response(ret_json)
	except Exception as e:
		msg = str(e)
		errorcode = -1
		version = "1.0"
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return myhttpresponse.json_response(ret_json, True)

@csrf_exempt
@verifylogin
def saverecordbyid(request):
	try:
		jsondata = json.loads(request.body)
		user = request.user
		ret_json = apifuncs.API_SaveRecordById(jsondata, user)
		return myhttpresponse.json_response(ret_json)
	except Exception as e:
		msg = str(e)
		errorcode =-1
		version = "1.0"
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return myhttpresponse.json_response(ret_json, True)

@csrf_exempt
@verifylogin
def deleterecordbyid(request):
	try:
		jsondata = json.loads(request.body)
		user = request.user
		ret_json = apifuncs.API_DeleteRecordById(jsondata, user)
		return myhttpresponse.json_response(ret_json)
	except Exception as e:
		msg = str(e)
		errorcode = -1
		version = "1.0"
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return myhttpresponse.json_response(ret_json, True)

# class JSONResponse(HttpResponse):
# 	def __init__(self, data, **kwargs):
# 		content = JSONRenderer().render(data)
# 		kwargs['content_type'] = 'application/json'
# 		super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def searchtext(request):
	try:
		jsondata = json.loads(request.body)
		ret_json = apifuncs.API_SearchText(jsondata)
		return myhttpresponse.json_response(ret_json)
	except Exception as e:
		msg = str(e)
		errorcode = -1
		version = "1.0"
		ret_json = myjson.generatecommonjson(msg, errorcode, version)
		return myhttpresponse.json_response(ret_json, True)

@csrf_exempt
def islogin(request):
	if request.method == "GET":
		msg = 'ok'
		errorcode = 0
		version = "1.0"
		itemlists = []
		itemlistnames = []
		try:
			user = request.user
			if user.is_authenticated():
				islogin = 1
				username = str(user).split('@')[0]
				itemlistnames.extend(["islogin", "username", "user"])
				itemlists.extend([islogin, username, str(user)])
				ret_json = myjson.generaetmultijson(msg, errorcode, version, itemlistnames, itemlists)
				return myhttpresponse.json_response(ret_json)
			else:
				islogin = 0
				ret_json = myjson.generateitemjson(msg, errorcode, version, "islogin", islogin)
				return myhttpresponse.json_response(ret_json)
		except Exception as e:
			msg = str(e)
			errorcode = -1
			version = "1.0"
			return myhttpresponse.json_response(myjson.generatecommonjson(msg, errorcode, version))

@csrf_exempt
@verifylogin
def savechannelbyid(request):
	if request.method == 'POST':
		logger.debug("rrr")
		msg = 'ok'
		errorcode = 0
		version = "1.0"
		try:
			user = request.user
			username = str(user).split('@')[0]
			jsondata = json.loads(request.body)
			ret_json = apifuncs.API_SaveChannelById(jsondata, user, username)
			return myhttpresponse.json_response(ret_json)
		except Exception as e:
			msg = str(e)
			errorcode = -1
			version = "1.0"
			return myhttpresponse.json_response(myjson.generatecommonjson(msg, errorcode, version))
