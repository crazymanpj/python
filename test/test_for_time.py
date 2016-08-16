import time
import datetime
print time.time()

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

#×Ö·û´®×ªtime
str = "Wed, 3 Aug 2016 15:30:39 +0800"
t = datetime.datetime.strptime(str, "%a, %d %b %Y %H:%M:%S +0800")
t.strftime('%Y-%m-%d %H:%M:%S')
print t
