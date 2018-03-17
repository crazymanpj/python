# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-01-09
# Author:  pangjian
# version: 1.0
from dbpackage.models import DBproductlist, DBtrynolist, DBpackageret, DBpackageinfo, DBPartnerlist
from lib import myjson, singletonexecute,myconfig
import os,time
from dbmakepack.settings import PROJECT_PATH
from django.core.exceptions import ObjectDoesNotExist
from dbmakepack.settings import MYCONFIG_FILE_PATH, MYCONFIG_FILE_PATH
import logging
from lib import winhelper
import subprocess
import database
logger = logging.getLogger('dbpackage')


def API_MakePackage(jsondata):
    msg = "ok"
    version = "1.0"
    errorcode = "0"
    ret_json = {}
    packageinfo = {}

    packageinfo['product'] = jsondata.get('product', None)
    # packageinfo['isnewitem'] = jsondata.get('isnewitem', None)
    packageinfo['itemname'] = jsondata.get('itemname', None)
    packageinfo['tryno'] = jsondata.get('tryno', None)
    packageinfo['packagetype'] = jsondata.get('packettype', None)
    packageinfo['packagemodel'] = jsondata.get('packetmodel', None)
    packageinfo['tid1'] = jsondata.get('tid1', None)
    packageinfo['tid2'] = jsondata.get('tid2', None)
    packageinfo['tod1'] = jsondata.get('tod1', None)
    packageinfo['tod2'] = jsondata.get('tod2', None)
    packageinfo['fixuplive'] = jsondata.get('fixuplive', None)
    packageinfo['islokmp'] = jsondata.get('islokmp', None)
    packageinfo['specialfile'] = jsondata.get('specialfile', None)
    packageinfo['localname'] = jsondata.get('localname', None)
    packageinfo['isnewitem'] = database.isnewitem(packageinfo['itemname'], packageinfo['packagetype'])
    logger.debug(packageinfo['localname'])

    database.createpackageinfo(**packageinfo)
    gettaskid = DBpackageinfo.objects.all().order_by('-taskid')
    taskid = gettaskid[0].taskid

    logger.debug(taskid)
    logger.debug('API_UpdateSvn')
    API_UpdateSvn()

    # isnewitem = API_IsNewItem(packageinfo['itemname'], packageinfo['packagetype'])
    argvs = '-product=%s -isnewitem=%s -itemname=%s -tryno=%s -packettype=%s -packetmodel=%s -tid1=%s -tid2=%s -tod1=%s -tod2=%s -fixuplive=%s -islokmp=%s -specialfile=%s -localname=%s -taskid=%s'%(\
            packageinfo['product'], packageinfo['isnewitem'], packageinfo['itemname'], packageinfo['tryno'], packageinfo['packagetype']\
            , packageinfo['packagemodel'], packageinfo['tid1'], packageinfo['tid2'], packageinfo['tod1'], packageinfo['tod2']\
            , packageinfo['fixuplive'], packageinfo['islokmp'], packageinfo['specialfile'], packageinfo['localname'], taskid)
    logger.debug(argvs)
    # os.chdir('D:\makepacketToosls')
    s = singletonexecute.Singleton(MYCONFIG_FILE_PATH, argvs)
    ret = s.makepackage_thread()

    if ret:
        ret_json = myjson.generatecommonjson('ok', '0', '1.0')
    else:
        ret_json = myjson.generatecommonjson('有人正在打包，请稍后再打', -1, '1.0')
        logger.debug('someone is making package, delete unuse record')
        deletepackageinfo(taskid)
    return ret_json

def API_AddParnerlist(jsondata):
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    d_parner = {}

    logger.debug('addparner start...')
    d_parner['partner'] = jsondata.get('parner', None)
    if d_parner['partner'] != None:
        database.createparner(**d_parner)

    ret_json = myjson.generatecommonjson(msg, errorcode, version)
    logger.debug('addparner end...')
    return ret_json

def API_GetProductList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    pl = DBproductlist.objects.all().filter(status=1)
    for i in pl:
        itemlist.append(i.name)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'productlist', itemlist)
    return ret_json


def API_GetTrynoList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    tl = DBtrynolist.objects.all().filter(status=1)
    for i in tl:
        itemlist.append(i.tryno)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'trynolist', itemlist)
    return ret_json


def API_GetAllMakePacketInfo():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []
    localpath = ''

    pi = DBpackageinfo.objects.all().order_by('-makepackagetime')
    for i in pi:
        try:
            pr = DBpackageret.objects.all().get(taskid=i.taskid)
            localpath = pr.localpath
        except ObjectDoesNotExist as e:
            localpath = ''

        ret = {
        u"taskid" : i.taskid,
        u"datetime" : i.makepackagetime,
        u"tryno" : i.tryno,
        u"product" : i.product,
        u"user" : i.user,
        u"sharepath" : localpath,
        u"result" : i.result,
        u"isnewitem" : i.isnewitem,
        u"itemname" : i.itemname,
        u"packagetype" : i.packagetype,
        u"packagemodel" : i.packagemodel,
        u"tid1" : i.tid1,
        u"tid2" : i.tid2,
        u"tod1" : i.tod1,
        u"tod2" : i.tod2,
        u"islokmp" : i.islokmp,
        u"user" : i.user
        }
        itemlist.append(ret)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'data', itemlist)
    return ret_json

def API_GetTaskResult(taskid):
    msg = 'ok'
    version = '1.0'
    errorcode = 0

    logger.debug(taskid)
    pl = DBpackageinfo.objects.all().get(taskid=taskid)
    result = pl.result

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'result', result)
    return ret_json

def API_StopMakePackage(jsondata):
    msg = 'ok'
    version = '1.0'
    result = 1
    logger.debug(MYCONFIG_FILE_PATH)
    processlist = myconfig.getconfigvalue(MYCONFIG_FILE_PATH, 'taskkill', 'processlist')
    logger.debug(processlist)
    processlist = processlist.split('|')
    for i in processlist:
        cmd = "taskkill /F /IM " + i
        ret = os.system(cmd)
        if ret is not False:
            result = 0

    taskid = jsondata.get('Taskid', None)
    logger.debug(taskid)
    pi = DBpackageinfo.objects.all().get(taskid=taskid)
    pi.result = -1
    pi.save()

    configfile = os.path.join(PROJECT_PATH, 'stconfig.ini')
    s = singletonexecute.Singleton(configfile, '')
    s.resetworking_bymanu()

    return myjson.generatecommonjson(msg, 0, version)

def API_GetPartnerList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    pl = DBPartnerlist.objects.all().filter(status=1)
    for i in pl:
        itemlist.append(i.partner)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'partnerlist', itemlist)
    return ret_json

def API_UpdateSvn():
    msg = 'ok'
    version = '1.0'
    errorcode = 0

    binpath = myconfig.getconfigvalue(MYCONFIG_FILE_PATH, 'svnupdate', 'binpath')
    # downloadir = myconfig.getconfigvalue(MYCONFIG_FILE_PATH, 'svnupdate', 'downloadir')
    # testpath = myconfig.getconfigvalue(MYCONFIG_FILE_PATH, 'svnupdate', 'testpath')
    logger.debug(binpath)
    # winhelper.removeFileInFirstDir('D:\makepacketTools\PacketInfo\duba')
    # cmd = "runas /savecred /user:makepackage " + binpath
    # logger.debug(cmd)
    subprocess.Popen(binpath)
    logger.debug('API_UpdateSvn end...')
    # print 'API_UpdateSvn end...'
    return myjson.generatecommonjson(msg, errorcode, version)
