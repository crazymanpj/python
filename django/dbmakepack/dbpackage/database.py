# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-03-14
# Author:  pangjian
# version: 1.0
from dbpackage.models import DBproductlist, DBtrynolist, DBpackageret, DBpackageinfo, DBPartnerlist
from django.core.exceptions import ObjectDoesNotExist
import logging
import time
logger = logging.getLogger('dbpackage')


def createpackageinfo(**packageinfo):
    m_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    logger.debug(m_time)
    packageinfo['makepackagetime'] = m_time
    packageinfo['result'] = 0
    DBpackageinfo.objects.create(**packageinfo)

def deletepackageinfo(taskid):
    DBpackageinfo.objects.get(taskid=taskid).delete()

def createparner(**parner):
    m_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
    parner['status'] = 1
    parner['addtime'] = m_time
    DBPartnerlist.objects.create(**parner)

def isnewitem(itemname, packagetype):
    pi = DBpackageinfo.objects.filter(itemname=itemname, packagetype=packagetype, result=1)
    if len(pi) > 0:
        logger.debug('is not newitem...')
        return 0
    else:
        logger.debug('newitem...')
        return 1
        
if __name__=='__main__':
    pass
