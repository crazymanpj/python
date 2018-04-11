# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-02-06
# Author:  pangjian
# version: 1.0
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from lib import myhttpresponse
from . import apifuncs
import json
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
import logging
import traceback
# from django.views.decorators.cache import cache_page

logger = logging.getLogger('dbpackage')
# from dbpackage.task import add


def index(request):
    return HttpResponseRedirect('/dbmakepack/')

@csrf_exempt
def makepackage(request):
    if request.method == 'POST':
        print('test')
        try:
            jsondata = json.loads(request.body.decode('utf-8'))
            ret_json = apifuncs.API_MakePackage(jsondata)
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not post...')


def getproductlist(request):
    print('getproductlist')
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_GetProductList()
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

# @cache_page(60 * 15)
def gettrynolist(request):
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_GetTrynoList()
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')


def getallmakepacketinfo(request):
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_GetAllMakePacketInfo()
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')


def testcelery(request):
    # add.delay(4, 8)
    return HttpResponse('Celery testing666')

@csrf_exempt
def getresultbytaskid(request):
    logger.debug('getresultbytaskid')
    if request.method == 'GET':
        try:
            taskid = request.GET.get('Taskid', '')
            logger.debug(taskid)
            ret_json = apifuncs.API_GetTaskResult(taskid)
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not post...')

@csrf_exempt
def stopmakepackage(request):
    if request.method == 'POST':
        try:
            jsondata = json.loads(request.body)
            ret_json = apifuncs.API_StopMakePackage(jsondata)
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not post...')

def getpartnerlist(request):
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_GetPartnerList()
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

def test_updatesvn(request):
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_UpdateSvn()
            # ret_json = {}
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

def test_method(request):
    logger.debug('test_method')
    if request.method == 'GET':
        try:
            # ret_json = apifuncs.API_IsNewItem(itemname, packagetype)
            ret_json = {}
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not post...')

@csrf_exempt
def addpartner(request):
    if request.method == 'POST':
        try:
            jsondata = json.loads(request.body)
            ret_json = apifuncs.API_AddParnerlist(jsondata)
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

def getinstallxml(request):
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_GetInstallXmlList()
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

def getpacketxml(request):
    if request.method == 'GET':
        try:
            ret_json = apifuncs.API_GetPacketXmlList()
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            logger.debug(str(e))
            traceback.print_exc()
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

@csrf_exempt
def getlastpackageinfobyitemname(request):
    if request.method == 'POST':
        try:
            jsondata = json.loads(request.body)
            ret_json = apifuncs.API_GetLastPackageInfoByItemname(jsondata)
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            traceback.print_exc()
            logger.debug(str(e))
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')

@csrf_exempt
def getautotidtod(request):
    if request.method == 'POST':
        try:
            jsondata = json.loads(request.body)
            logger.debug('test')
            ret_json = apifuncs.API_GetPackageInfoGroupByTidTod(jsondata)
            return myhttpresponse.json_response(ret_json, True)
        except Exception as e:
            traceback.print_exc()
            logger.debug(str(e))
            return myhttpresponse.mycommonerror_response(str(e))
    else:
        return myhttpresponse.mycommonerror_response('method is not get...')
