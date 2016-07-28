import os
import stat
import time

fileStats = os.stat('e:\index_makedata\index.sqlite')
fileinfo = {
    'Size' : fileStats[stat.ST_SIZE],
    'LastModified' : fileStats[stat.ST_MTIME],
    'LastAccessed' : time.ctime(fileStats[stat.ST_ATIME]),
    'CreateTime' : time.ctime(fileStats[stat.ST_CTIME]),
    'Mode' : fileStats[stat.ST_MODE]
    }
for infoField in fileinfo:
    print infoField, ':' + str(fileinfo[infoField])

if stat.S_ISDIR(fileStats[stat.ST_MODE]):
    print 'Directory'
else:
    print 'Non-directory'

test = fileinfo["LastModified"]
temp = time.localtime(test)
print temp
temp2 = time.strftime("%Y-%m-%d %H:%M:%S", temp)
print temp2