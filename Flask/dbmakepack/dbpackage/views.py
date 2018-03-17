#encoding=utf-8
# Date:    2018-02-01
# Author:  pangjian
# version: 1.0
from dbpackage import ins_dbpackage
from flask import request
import apifuncs
from lib import myjson

@ins_dbpackage.route('/')
def index():
    return 'Hello World'

@ins_dbpackage.route('/dbpackage/getproductlist/', methods=['GET', 'POST'])
def getproductlist():
    if request.method == 'GET':
        try:
            return apifuncs.API_GetProductList()
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')
    else:
        return 'method is not get...'


@ins_dbpackage.route('/dbpackage/gettrynolist/', methods=['GET', 'POST'])
def gettrynolist():
    if request.method == 'GET':
        try:
            return apifuncs.API_GetTrynoList()
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')

    else:
        return 'method is no get...'


@ins_dbpackage.route('/dbpackage/getallmakepacketinfo/', methods=['GET', 'POST'])
def getallmakepacketinfo():
    if request.method == 'GET':
        try:
            return apifuncs.API_GetAllMakePacketInfo()
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')
    else:
        return 'method is no get...'

@ins_dbpackage.route('/dbpackage/getresultbytaskid/', methods=['GET', 'POST'])
def getresultbytaskid():
    if request.method == 'GET':
        try:
            taskid = request.args.get('Taskid', '')
            return apifuncs.API_GetTaskResult(taskid)
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')
    else:
        return 'method is not get...'

@ins_dbpackage.route('/dbpackage/getpartnerlist/', methods=['GET', 'POST'])
def getpartnerlist():
    if request.method == 'GET':
        try:
            return apifuncs.API_GetPartnerList()
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')
    else:
        return 'method is no get...'

@ins_dbpackage.route('/dbpackage/makepackage/', methods=['GET', 'POST'])
def makepackage():
    if request.method == 'POST':
        try:
            jsondata = request.get_json()
            return apifuncs.API_MakePackage(jsondata)
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')
    else:
        return 'method is not post...'

@ins_dbpackage.route('/dbpackage/stopmakepackage/', methods=['GET', 'POST'])
def stopmakepackage():
    if request.method == 'POST':
        try:
            return apifuncs.API_StopMakePackage()
        except Exception as e:
            return myjson.generatecommonjson(str(e), -1, '1.0')
    else:
        return 'method is not post'
