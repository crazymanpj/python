# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-01-09
# Author:  pangjian
# version: 1.0
from dbpackage.models import DBproductlist, DBtrynolist, DBpackageret, DBpackageinfo, DBPartnerlist, DBPacketXml, DBInstallXml
from lib import myjson, singletonexecute,myconfig
import os,time
from dbmakepack.settings import PROJECT_PATH
from django.core.exceptions import ObjectDoesNotExist
from dbmakepack.settings import MYCONFIG_FILE_PATH, PRODUCT_DUBA
import logging
from lib import winhelper
import subprocess
import database
import datetime
from lib import singletonexecute
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
    packageinfo['installxml'] = database.getargv_by_description(DBInstallXml, jsondata.get('installxml', None))
    packageinfo['packetxml'] = database.getargv_by_description(DBPacketXml, jsondata.get('packetxml', None))
    logger.debug(packageinfo['installxml'])
    logger.debug(packageinfo['packetxml'])

    tid1 = packageinfo['tid1']
    numlist = myconfig.getconfigvalue(MYCONFIG_FILE_PATH, 'islockmp', 'tid1')
    for i in numlist.split(','):
        if tid1 == i:
            packageinfo['islokmp'] = 1


    database.createpackageinfo(**packageinfo)
    gettaskid = DBpackageinfo.objects.all().order_by('-taskid')
    taskid = gettaskid[0].taskid

    logger.debug(taskid)
    logger.debug('API_UpdateSvn start...')
    API_UpdateSvn()
    logger.debug('API_UpdateSvn end...')
    time.sleep(3)

    # isnewitem = API_IsNewItem(packageinfo['itemname'], packageinfo['packagetype'])
    argvs = '-product=%s -isnewitem=%s -itemname=%s -tryno=%s -packettype=%s -packetmodel=%s -tid1=%s -tid2=%s -tod1=%s -tod2=%s -fixuplive=%s -islokmp=%s -specialfile=%s -localname=%s -taskid=%s -installxmlitem=%s -packetxmlitem=%s'%(\
            packageinfo['product'], packageinfo['isnewitem'], packageinfo['itemname'], packageinfo['tryno'], packageinfo['packagetype']\
            , packageinfo['packagemodel'], packageinfo['tid1'], packageinfo['tid2'], packageinfo['tod1'], packageinfo['tod2']\
            , packageinfo['fixuplive'], packageinfo['islokmp'], packageinfo['specialfile'], packageinfo['localname'], taskid, packageinfo['installxml'], packageinfo['packetxml'])
    logger.debug(argvs)
    # os.chdir('D:\makepacketToosls')
    s = singletonexecute.Singleton(MYCONFIG_FILE_PATH, argvs)
    ret = s.makepackage_thread()

    if ret:
        ret_json = myjson.generatecommonjson('ok', '0', '1.0')
    else:
        ret_json = myjson.generatecommonjson('有人正在打包，请稍后再打', -1, '1.0')
        logger.debug('someone is making package, delete unuse record')
        database.deletepackageinfo(taskid)
    return ret_json

def API_AddParnerlist(jsondata):
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    d_parner = {}

    logger.debug('addparner start...')
    d_parner['partner'] = jsondata.get('parner', None)
    pl = DBPartnerlist.objects.filter(partner=d_parner['partner'])

    if d_parner['partner'] != None and len(pl) == 0:
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

    pi = DBpackageinfo.objects.filter(product=PRODUCT_DUBA).order_by('-makepackagetime')
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
        u"localname" : i.localname,
        u"installxml" : database.getdescription_by_argv(DBInstallXml, i.installxml),
        u"packetxml" : database.getdescription_by_argv(DBPacketXml, i.packetxml)
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

    pl = DBPartnerlist.objects.all().filter(status=1).order_by('partner')
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
    # subprocess.Popen(binpath)
    s = singletonexecute.Singleton(argvs=binpath)
    s.winwaitcallexe(waitingsecond=120, breaksecond=1)
    logger.debug('API_UpdateSvn end...')
    # print 'API_UpdateSvn end...'
    return myjson.generatecommonjson(msg, errorcode, version)

def API_GetInstallXmlList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    ixlist = DBInstallXml.objects.all().filter(status=1)
    for i in ixlist:
        itemlist.append(i.description)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'installxml', itemlist)
    return ret_json

def API_GetPacketXmlList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    pxlist = DBPacketXml.objects.all().filter(status=1)
    for i in pxlist:
        itemlist.append(i.description)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'packetxml', itemlist)
    return ret_json

def API_GetLastPackageInfoByItemname(jsondata):
    msg = 'ok'
    version = '1.0'
    errorcode = 0

    itemname = jsondata.get('itemname', None)
    logger.debug(itemname)
    pi = DBpackageinfo.objects.all().filter(itemname=itemname, product=PRODUCT_DUBA).order_by('-makepackagetime')
    logger.debug(len(pi))
    if len(pi) < 1:
        logger.debug('无记录')
        ret={}
    else:
        ret = {
        u"taskid" : pi[0].taskid,
        u"datetime" : pi[0].makepackagetime,
        u"tryno" : pi[0].tryno,
        u"product" : pi[0].product,
        u"user" : pi[0].user,
        u"result" : pi[0].result,
        u"isnewitem" : pi[0].isnewitem,
        u"itemname" : pi[0].itemname,
        u"packagetype" : pi[0].packagetype,
        u"packagemodel" : pi[0].packagemodel,
        u"tid1" : pi[0].tid1,
        u"tid2" : pi[0].tid2,
        u"tod1" : pi[0].tod1,
        u"tod2" : pi[0].tod2,
        u"islokmp" : pi[0].islokmp,
        u"localname" : pi[0].localname,
        u"installxml" : database.getdescription_by_argv(DBInstallXml, pi[0].installxml),
        u"packetxml" : database.getdescription_by_argv(DBPacketXml, pi[0].packetxml)
        }

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'data', ret)
    return ret_json

def API_GetPackageInfoGroupByTidTod(jsondata):
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    itemname = jsondata.get('itemname', None)
    logger.debug(itemname)
    sql = "select * from db_packageinfo where itemname='%s' and product='%s' group by tid1,tid2,tod1,tod2"%(itemname,PRODUCT_DUBA)
    ret = DBpackageinfo.objects.raw(sql)
    # for i in ret:
    #     logger.debug(i.taskid)
    for i in ret:
        temp = {
            u"taskid" : i.taskid,
            u"datetime" : i.makepackagetime,
            u"tryno" : i.tryno,
            u"product" : i.product,
            u"user" : i.user,
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
            u"localname" : i.localname,
            u"installxml" : database.getdescription_by_argv(DBInstallXml, i.installxml),
            u"packetxml" : database.getdescription_by_argv(DBPacketXml, i.packetxml)
        }
        itemlist.append(temp)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'data', itemlist)
    return ret_json
