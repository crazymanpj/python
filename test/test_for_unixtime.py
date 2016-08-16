#coding=utf-8
import time

def timestamp_datatime(value):
	format = '%Y-%m-%d %H:%M:%S'
	#value为传入值的时间错，如：133288820
	time_convert = time.localtime(float(value))
	dt = time.strftime(format, time_convert)
	return dt

def datatime_timestamp(dt):
	time.strptime(dt, '%Y-%m-%d %H:%M:%S')
	s=time.mktime(time.strptime(dt, '%Y-%m-%d %H:%M:%S'))
	return int(s)


print "input the unix time:"
value = raw_input()
print value
s = timestamp_datatime(value)
print s