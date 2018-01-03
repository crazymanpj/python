#encoding=utf-8
# Date:    2017-10-17
# Author:  pangjian
# version: 1.0
import time,datetime

def get_time_today():
	# return '2017-09-07'
	return time.strftime("%Y-%m-%d", time.localtime(time.time()))

def get_time_yesterday():
	# return '2017-09-07'
	now = datetime.datetime.now()
	delta = datetime.timedelta(days=1)
	n_days = now - delta
	return n_days.strftime('%Y-%m-%d')

def get_time_weekago_today():
	# return '2017-09-01'
	now = datetime.datetime.now()
	delta = datetime.timedelta(days=7)
	n_days = now - delta
	return n_days.strftime('%Y-%m-%d')

def get_time_weekago_yesterday():
	# return '2017-09-01'
	now = datetime.datetime.now()
	delta = datetime.timedelta(days=8)
	n_days = now - delta
	return n_days.strftime('%Y-%m-%d')

def get_recent_hour():
	recent_hour = time.strftime("%H", time.localtime(time.time()))
	if int(recent_hour) - 2 > 1:
		return int(recent_hour) - 2
	else:
		return 23

def get_time_today_f():
	return time.strftime("%m.%d", time.localtime(time.time()))

def get_time_yesterday_f():
	now = datetime.datetime.now()
	delta = datetime.timedelta(days=1)
	n_days = now - delta
	return n_days.strftime('%m.%d')

def get_time_bydiff(date, diff):
	orginal = datetime.datetime.strptime(date, '%Y-%m-%d')
	delta = datetime.timedelta(days=diff)
	n_days = orginal - delta
	return n_days.strftime('%Y-%m-%d')

def get_time_f_bydiff(date, diff):
	orginal = datetime.datetime.strptime(date, '%Y-%m-%d')
	delta = datetime.timedelta(days=diff)
	n_days = orginal - delta
	return n_days.strftime('%m.%d')


def get_weekday(date):
	#where Monday is 0 and Sunday is 6
	weekdecription = {'0':'星期一', '1':'星期二', '2':'星期三', '3':'星期四', '4':'星期五', '5':'星期六', '6':'星期日',}
	num = datetime.datetime.strptime(date, '%Y-%m-%d').weekday()
	return weekdecription[str(num)]

def sortdictbyvalue(dict_temp):
	items = dict_temp.items()
	backitems = [[v[1], v[0]] for v in items ]
	backitems.sort(reverse=True)
	return  [ backitems[i][1] for i in range(0,len(backitems))]

def get_dict_keybyvalue(dict_temp, value):
	for k,v in dict_temp.items():
		if v == value:
			return k



if __name__=='__main__':
	print 'test'
	# print get_time_yesterday()
	# print get_time_today_f()
	# print get_time_yesterday_f()
	print get_weekday('2017-12-02')
	print '-'
	print get_time_f_bydiff('2017-12-02', 7)
	print get_time_bydiff('2017-12-02', 1)
	print len('p_duba_uppop')
	print len('﻿p_duba_uppop')
	t = u'p_duba_uppop'
	p = u'﻿p_duba_uppop'
	print len(t), len(p)
	for i in t:
		print i 

	for i in p:
		print i
