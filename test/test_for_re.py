# encoding: UTF-8 
import re,os
import urllib

str = r"d.d.cxv.ewwe/vjisjvij"

pattern = re.compile('\w+.\w+.\w+.\w+') 
  
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None 
#match = pattern.match(str) 
match = pattern.search(str) 
  
if match: 
    # 使用Match获得分组信息 
    substr = match.group()
    print match.group() 
    print match
    
    print "-" *10
    str = str.lstrip(r"ftp://" + substr)
    print str
    print os.path.dirname(str)
    
### 输出 ### 
# hello 


str2 = r""
str3 = r""

print "-" *20
pattern = re.compile('\d{14}')
match = pattern.search(str3)
if match:
	substr = match.group()
	print match.group()

print "-" *20
pattern = re.compile('cms*_plugin_[abcdefghijklmnopqrstuvwxyz]+')
match = pattern.search(str3)
if match:
    substr = match.group()
    print match.group()


def getplugintype(pluginpath):
    pattern = re.compile('cms*_plugin_[abcdefghijklmnopqrstuvwxyz]+')
    match = pattern.search(pluginpath)
    if match:
        substr = match.group()
        return substr.split('_')[2]
    else:
        return ""

print getplugintype(str3)


print "-"*100


import re
# m = re.match(r'(\w+) (\w+)(?P<sign>.*)', 'hello world!')
 
# print "m.string:", m.string
# print "m.re:", m.re
# print "m.pos:", m.pos
# print "m.endpos:", m.endpos
# print "m.lastindex:", m.lastindex
# print "m.lastgroup:", m.lastgroup
 
# print "m.group(1,2):", m.group(1, 2)
# print "m.groups():", m.groups()
# print "m.groupdict():", m.groupdict()
# print "m.start(2):", m.start(2)
# print "m.end(2):", m.end(2)
# print "m.span(2):", m.span(2)
# print r"m.expand(r'\2 \1\3'):", m.expand(r'\2 \1\3')


channel = "2010003660(qq浏览器)"
m = re.match('(\d+)(.)', channel)
print m.group(1,2)


print "-" * 50

u = r'http://www.gaojiqing.com'
print 'tt'
proto, rest = urllib.splittype(u)
host, rest = urllib.splithost(rest)
print host
# u = r'http://www.gaojiqing.com/'
pattern = '(http|https)://([\S]+/)'
m = re.match(pattern, u)
# print m.group(0,1,2)


u = r'lb2345.com/dfe'
pattern = '([\S]+.[\S]+/)'
m = re.match(pattern, u)
print m.group(1)