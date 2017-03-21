#encoding=utf-8
import time
import datetime
print time.time()

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
print time.strftime("%Y-%m-%d", time.localtime(time.time()))

#×Ö·û´®×ªtime
str = "Wed, 3 Aug 2016 15:30:39 +0800"
t = datetime.datetime.strptime(str, "%a, %d %b %Y %H:%M:%S +0800")
t.strftime('%Y-%m-%d %H:%M:%S')
print t

#算最近几天
now = datetime.datetime.now()
print now
delta = datetime.timedelta(days=3)
n_days = now - delta
print n_days.strftime('%Y-%m-%d %H:%M:%S')  
time.sleep(1)
then = datetime.datetime.now()
print (then - now).seconds
