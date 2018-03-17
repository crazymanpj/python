#encoding=utf-8
# Date:    2018-02-01
# Author:  pangjian
# version: 1.0
from models import ProductList, TrynoList, PackageInfo, PackageRet,ParnerList
from lib import myjson, singletonexecute,myconfig
import time,os
from dbpackage import db,ins_dbpackage


def API_GetProductList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    pl = ProductList.query.filter_by(status='1')
    for i in pl:
        itemlist.append(i.name)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'productlist', itemlist)
    return ret_json


def API_GetTrynoList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    tl = TrynoList.query.filter_by(status='1')
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

    #按时间排序还没弄好
    pi = PackageInfo.query.order_by(PackageInfo.makepackagetime)
    for i in pi:
        print i.taskid
        pr = PackageRet.query.filter_by(taskid=i.taskid).first()
        print(type(pr))
        print(pr)
        if pr == None:
            print 'object is none'
            localpath = ''
        else:
            localpath = pr.localpath

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

    pl = PackageInfo.query.get(taskid)
    result = pl.result

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'result',result)
    return ret_json

def API_GetPartnerList():
    msg = 'ok'
    version = '1.0'
    errorcode = 0
    itemlist = []

    pl = ParnerList.query.filter_by(status=1)
    for i in pl:
        itemlist.append(i.partner)

    ret_json = myjson.generateitemjson(msg, errorcode, version, 'partnerlist', itemlist)
    return ret_json

def API_MakePackage(jsondata):
    msg = 'ok'
    version = '1.0'
    errorcode = '0'
    ret_json = {}

    product = jsondata['product']
    isnewitem = jsondata['isnewitem']
    itemname = jsondata['itemname']
    tryno = jsondata['tryno']
    packettype = jsondata['packettype']
    packetmodel = jsondata['packetmodel']
    tid1 = jsondata['tid1']
    tid2 = jsondata['tid2']
    tod1 = jsondata['tod1']
    tod2 = jsondata['tod2']
    fixuplive = jsondata['fixuplive']
    islokmp = jsondata['islokmp']
    specialfile = jsondata['specialfile']
    localname = jsondata['localname']

    API_CREATPackageInfo(product, isnewitem,itemname,tryno,packettype,packetmodel,tid1,tid2,tod1,tod2,fixuplive,islokmp,specialfile,localname)
    gettaskid = PackageInfo.query.order_by('-taskid')
    taskid = gettaskid[0].taskid
    print taskid
    argvs = '-product=%s -isnewitem=%s -itemname=%s -tryno=%s -packettype=%s -packetmodel=%s -tid1=%s -tid2=%s -tod1=%s -tod2=%s -fixuplive=%s -islokmp=%s -specialfile=%s -localname=%s -taskid=%s'%(\
            product, isnewitem, itemname, tryno, packettype, packetmodel, tid1, tid2, tod1, tod2, fixuplive\
            , islokmp, specialfile, localname, taskid)
    print(argvs)
    s = singletonexecute.Singleton(os.path.join(ins_dbpackage.config['PROJECT_PATH'], 'stconfig.ini'), argvs)
    s.makepackage_thread()
    ret_json = myjson.generatecommonjson('ok', '0', '1.0')
    return ret_json

def API_CREATPackageInfo(product, isnewitem,itemname,tryno,packettype,packetmodel,tid1,tid2,tod1,tod2,fixuplive,islokmp,specialfile,localname):
    m_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    packageinfo = PackageInfo(m_time,product, isnewitem,itemname,tryno,packettype,packetmodel,tid1,tid2,tod1,tod2,fixuplive,islokmp,specialfile,localname)
    db.session.add(packageinfo)
    db.session.commit()
    return True

def API_StopMakePackage():
    configfilepath = os.path.join(ins_dbpackage.config['PROJECT_PATH'], 'stconfig.ini')
    print configfilepath
    processlist = myconfig.getconfigvalue(configfilepath, 'taskkill', 'processlist')
    processlist = processlist.split('|')
    for i in processlist:
        cmd = "taskkill /IM " + i
        ret = os.system(cmd)
        if ret is not False:
            result = 0
    return result
