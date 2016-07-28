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
    
    str = str.lstrip(r"ftp://" + substr)
    print str
    print os.path.dirname(str)
    
### 输出 ### 
# hello 
