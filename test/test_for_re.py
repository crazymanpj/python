# encoding: UTF-8 
import re,os

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