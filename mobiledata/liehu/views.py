#!/usr/bin/env python
#encoding=utf-8
# Date:    2018-03-20
# Author:  pangjian
# version: 1.0
from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger('liehu')
from common import myhttpresponse,myjson
# Create your views here.

RET_TEXT = '''
{
　　"comrp":"IA_qPynYPj-bnH79nyuBPWF-riuGTv7b5HDhUyNbpy7xpyfqnHn4FhPEIy4YTMbqmv3hmLfqmv4xgzuWIA4E5H0hTAsqPzu-XZKGujYhmMFEI1YkPauETvFGIjYzFhkY5HDdnWDdnW63P1RhTZNGIjYkQjc_nzsdQjm_Pzs3Qjb_nHD_nHchmLFW5HfYPWR&ac=50",
　　"list":[
　　　　{
　　　　　　"ads":[
　　　　　　　　{
　　　　　　　　　　"adid":60001087,
　　　　　　　　　　"bgcolor":"",
　　　　　　　　　　"click_tracking":[
　　　　　　　　　　　　"http://10.60.81.185:1612/rp/?IA_qPynYPj-bnH79nyuBPWF-riuGTv7b5HDhUyNbpy7xpyfqnHn4FhPEIy4YTMbqmv3hmLfqmv4xgzuWIA4E5H0hTAsqPzu-XZKGujYhmMFEI1YkPauETvFGIjYzFhkY5HDdnWDdnW63P1RhTZNGIjYkQjc_nzsdQjm_Pzs3Qjb_nHD_nHchTAq1pyfqnHn4nHnsFhPETLfqnHcsnj0snauWTjY1FMNGujYdnj0snj0hTAk9U-qGujYvnj0snH03nzu9uv-b5Hmsnj0knj6dFMF-TdqYXgK-5H6sFMKoudq8myd-5HRsnj0sna3vnj0snH03nzu9TZKxTv9EIdqYXgK-5HRsnjnkFhFGujYkQWcsFhdYgv-b5Hmsnj0knj6LFhPzm1YYPHmzPf&ac=60",
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=2222&mid=139&placeid=139138&adcount=5",
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=2233&mid=139&placeid=139138&adcount=5"
　　　　　　　　　　],
　　　　　　　　　　"click_url":"http://dev.liehu.duba.com/v3/#/ads/list/manage/set?context=create&entryId=2&from=step#audience",
　　　　　　　　　　"desc":"",
　　　　　　　　　　"icon_url":"",
　　　　　　　　　　"imp_tracking":[
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=1111&mid=139&placeid=139138&adcount=5",
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=1122&mid=139&placeid=139138&adcount=5"
　　　　　　　　　　],
　　　　　　　　　　"imprp":"FMKETv-b5HD1rHD1nauWULPY5HDznj0snj0hmL0qnzudpyfqPH0snj0sFMK_my4xpyfqPW0snjDsrjnhmyIGujYvnj0snH03PiuzugPxIZ-suHY3nauspvIxUh7VuHYdnj0snj08PW0snjDsrjnhmgKsgLPCULIxIZ-suHYdnj01niuBpyfqni3znauVI7qGujYvnj0snH03PzuWThnqrj0Lrf&enc=1",
　　　　　　　　　　"material":[
　　　　　　　　　　　　{
　　　　　　　　　　　　　　"click_url":"http://dev.liehu.duba.com/v3/#/ads/list/manage/ad?context=create&entryId=2&from=step#format",
　　　　　　　　　　　　　　"desc":"",
　　　　　　　　　　　　　　"icon_url":"",
　　　　　　　　　　　　　　"pic_url":"http://10.60.81.184/150150.gif",
　　　　　　　　　　　　　　"title":"",
　　　　　　　　　　　　　　"title_color":"#000000"
　　　　　　　　　　　　}
　　　　　　　　　　],
　　　　　　　　　　"pic_url":"http://10.60.81.184/150150.gif",
　　　　　　　　　　"show_type":50031,
　　　　　　　　　　"title":"",
　　　　　　　　　　"title_color":"#000000"
　　　　　　　　},
　　　　　　　　{
　　　　　　　　　　"adid":60001086,
　　　　　　　　　　"bgcolor":"",
　　　　　　　　　　"click_tracking":[
　　　　　　　　　　　　"http://10.60.81.185:1612/rp/?IA_qPynYPj-bnH79nyuBPWF-riuGTv7b5HDhUyNbpy7xpyfqnHn4FhPEIy4YTMbqmv3hmLfqmv4xgzuWIA4E5H0hTAsqPzu-XZKGujYhmMFEI1YkPauETvFGIjYzFhkY5HDdnWDdnW63P1RhTZNGIjYkQjc_nzsdQjm_Pzs3Qjb_nHD_nHchTAq1pyfqnHn4nHnsFhPETLfqnHcsnj0snauWTjY1FMNGujYdnj0snj0hTAk9U-qGujYvnj0snH03nzu9uv-b5Hmsnj0knj6dFMF-TdqYXgK-5H6sFMKoudq8myd-5HRsnj0sna3vnj0snH03nzu9TZKxTv9EIdqYXgK-5HRsnjnkFhFGujYkQWcsFhdYgv-b5Hmsnj0knj6vFhPzm1YvnW63r0&ac=60",
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=2222&mid=139&placeid=139138&adcount=5",
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=2233&mid=139&placeid=139138&adcount=5"
　　　　　　　　　　],
　　　　　　　　　　"click_url":"http://dev.liehu.duba.com/v3/#/ads/list/manage/set?context=create&entryId=2&from=step#audience",
　　　　　　　　　　"desc":"",
　　　　　　　　　　"icon_url":"",
　　　　　　　　　　"imp_tracking":[
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=1111&mid=139&placeid=139138&adcount=5",
　　　　　　　　　　　　"http://10.60.81.185:1612/pc/?sdkt=3&uuid=&sysn=7&syst=2&brow=14&uit=1122&mid=139&placeid=139138&adcount=5"
　　　　　　　　　　],
　　　　　　　　　　"imprp":"FMKETv-b5HD1rHD1nauWULPY5HDznj0snj0hmL0qnzudpyfqPH0snj0sFMK_my4xpyfqPW0snjDsrjnhmyIGujYvnj0snH03PiuzugPxIZ-suHY3nauspvIxUh7VuHYdnj0snj08PW0snjDsrjnhmgKsgLPCULIxIZ-suHYdnj01niuBpyfqni3znauVI7qGujYvnj0snH03PBuWThnqnWcdPH6&enc=1",
　　　　　　　　　　"material":[
　　　　　　　　　　　　{
　　　　　　　　　　　　　　"click_url":"http://dev.liehu.duba.com/v3/#/ads/list/manage/ad?context=create&entryId=2&from=step#format",
　　　　　　　　　　　　　　"desc":"",
　　　　　　　　　　　　　　"icon_url":"",
　　　　　　　　　　　　　　"pic_url":"http://10.60.81.184/150150.png",
　　　　　　　　　　　　　　"title":"",
　　　　　　　　　　　　　　"title_color":"#000000"
　　　　　　　　　　　　}
　　　　　　　　　　],
　　　　　　　　　　"pic_url":"http://10.60.81.184/150150.png",
　　　　　　　　　　"show_type":50031,
　　　　　　　　　　"title":"",
　　　　　　　　　　"title_color":"#000000"
　　　　　　　　}
　　　　　　],
　　　　　　"placeid":139130
　　　　},
　　　　{
　　　　　　"ads":[
　　　　　　　　{
　　　　　　　　　　"adid":60001096,
　　　　　　　　　　"bgcolor":"",
　　　　　　　　　　"click_tracking":[
　　　　　　　　　　　　"http://10.60.81.185:1612/rp/?IA_qPynYPj-bnH79nyuBPWF-riuGTv7b5HDhUyNbpy7xpyfqnHn4FhPEIy4YTMbqmv3hmLfqmv4xgzuWIA4E5H0hTAsqPzu-XZKGujYhmMFEI1YkPauETvFGIjYzFhkY5HDdnWDdnW63P1RhTZNGIjYkQjc_nzsdQjm_Pzs3Qjb_nHD_nHchTAq1pyfqnHn4nHfsFhPETLfqnH0snj0sFhPs5HnhIy-b5HThTAk9U-qGujYvnj0snH04nzu9uv-b5Hmsnj0knjbdFMF-TdqYXgK-5H6sFMKoudq8myd-5HT8PW0snjDsrHnhmgKsgLPCULIxIZ-suHYdnj01nBuBpyfqna3knauVI7qGujYvnj0snH04PBuWThnqPHDsnjf&ac=60"
　　　　　　　　　　],
　　　　　　　　　　"click_url":"",
　　　　　　　　　　"desc":"",
　　　　　　　　　　"icon_url":"",
　　　　　　　　　　"imp_tracking":[

　　　　　　　　　　],
　　　　　　　　　　"imprp":"FMKETv-b5HD1rHDYnauWULPY5HDsnj0snauWTjY1FMNGujYLFMK_my4xpyfqPW0snjDsrHnhmyIGujYvnj0snH04PiuzugPxIZ-suHY3nauspvIxUh7VuHYLQWmsnj0knjb1Fh7sT7q1pAqLgLw4TARqPH0sn1chmh-b5H08nH0hUgwxpyfqPW0snjDsrHmhmLFW5HbsPjc&enc=1",
　　　　　　　　　　"material":[
　　　　　　　　　　　　{
　　　　　　　　　　　　　　"click_url":"",
　　　　　　　　　　　　　　"desc":"",
　　　　　　　　　　　　　　"icon_url":"",
　　　　　　　　　　　　　　"pic_url":"http://dev.liehu.duba.com/liehu/20180319/1521447643zxkx5.jpg",
　　　　　　　　　　　　　　"title":"",
　　　　　　　　　　　　　　"title_color":"#000000"
　　　　　　　　　　　　}
　　　　　　　　　　],
　　　　　　　　　　"pic_url":"http://dev.liehu.duba.com/liehu/20180319/1521447643zxkx5.jpg",
　　　　　　　　　　"show_type":50032,
　　　　　　　　　　"title":"",
　　　　　　　　　　"title_color":"#000000"
　　　　　　　　},
　　　　　　　　{
　　　　　　　　　　"adid":60001097,
　　　　　　　　　　"bgcolor":"",
　　　　　　　　　　"click_tracking":[
　　　　　　　　　　　　"http://t.duba.com"
　　　　　　　　　　],
　　　　　　　　　　"click_url":"",
　　　　　　　　　　"desc":"",
　　　　　　　　　　"icon_url":"",
　　　　　　　　　　"imp_tracking":[

　　　　　　　　　　],
　　　　　　　　　　"imprp":"FMKETv-b5HD1rHDYnauWULPY5HDsnj0snauWTjY1FMNGujYLFMK_my4xpyfqPW0snjDsrHnhmyIGujYvnj0snH04PiuzugPxIZ-suHY3nauspvIxUh7VuHYLQWmsnj0knjb1Fh7sT7q1pAqLgLw4TARqPH0sn1chmh-b5H08nH0hUgwxpyfqPW0snjDsrHmhmLFW5HbsPjc&enc=1",
　　　　　　　　　　"material":[
　　　　　　　　　　　　{
　　　　　　　　　　　　　　"click_url":"",
　　　　　　　　　　　　　　"desc":"",
　　　　　　　　　　　　　　"icon_url":"",
　　　　　　　　　　　　　　"pic_url":"http://dev.liehu.duba.com/liehu/20180319/2.jpg",
　　　　　　　　　　　　　　"title":"",
　　　　　　　　　　　　　　"title_color":"#000000"
　　　　　　　　　　　　}
　　　　　　　　　　],
　　　　　　　　　　"pic_url":"http://dev.liehu.duba.com/liehu/20180319/2.jpg",
　　　　　　　　　　"show_type":50032,
　　　　　　　　　　"title":"",
　　　　　　　　　　"title_color":"#000000"
　　　　　　　　}
　　　　　　],
　　　　　　"placeid":139140
　　　　}
　　],
　　"rpurl":"http://10.60.81.185:1612/rp/?"
}
'''



def pc(request):
    logger.debug('ttt')
    logger.debug(request.path)
    logger.debug(request.body)
    logger.debug(request.GET)
    logger.debug(request.GET['cb'])
    logger.debug(request.GET['cb'] + '(' + RET_TEXT + ')')
    return HttpResponse(request.GET['cb'] + '(' + RET_TEXT + ')')
