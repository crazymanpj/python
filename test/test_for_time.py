#encoding=utf-8
import time
import datetime
print time.time()

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print time.strftime("%Y-%m-%d", time.localtime(time.time()))

t_str = '2015-04-07'
print datetime.datetime.strptime(t_str, '%Y-%m-%d')


str = "Wed, 3 Aug 2016 15:30:39 +0800"
t = datetime.datetime.strptime(str, "%a, %d %b %Y %H:%M:%S +0800")
t.strftime('%Y-%m-%d %H:%M:%S')
print t

#算最近几天
now = datetime.datetime.now()
print "now"
print now
delta = datetime.timedelta(days=3)
n_days = now - delta
print n_days.strftime('%Y-%m-%d %H:%M:%S')  
time.sleep(1)
then = datetime.datetime.now()
print (then - now).seconds


def datetime_to_strtime(datetime_obj):
    """将 datetime 格式的时间 (含毫秒) 转为字符串格式
    :param datetime_obj: {datetime}2016-02-25 20:21:04.242000
    :return: {str}'2016-02-25 20:21:04.242'
    """
    local_str_time = datetime_obj.strftime("%Y-%m-%d %H:%M:%S.%f")
    return local_str_time

print time.ctime(1490860211)
# print time.ctime(1490860211.606)
timetuple = time.localtime(1490860211.606)
dt =  datetime.datetime.now()
print type(dt)
print   '时间：(%Y-%m-%d %H:%M:%S %f): ' , dt.strftime( '%Y-%m-%d %H:%M:%S %f')
# print time.strftime('%Y-%m-%d %H:%M:%S %f',timetuple)
dt2 = datetime.datetime.fromtimestamp(1490860211606/1000.0)
print   '时间2：(%Y-%m-%d %H:%M:%S %f): ' , dt2.strftime( '%Y-%m-%d %H:%M:%S.%f')
print datetime.datetime.fromtimestamp(1490860212056/1000)
print datetime_to_strtime(dt2)
print datetime.datetime.fromtimestamp(1490860211606/1000.0).strftime('%Y-%m-%d %H:%M:%S.%f')

dayOfWeek = datetime.datetime.today()
temp = '2017-12-02'
print datetime.datetime.strptime(temp, '%Y-%m-%d').weekday()
print type(dayOfWeek)
print(dayOfWeek)
