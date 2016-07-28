# encoding: UTF-8 
import re,os

str = r"测试结果"

pattern = re.compile('测试结果') 
  
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None 
#match = pattern.match(str) 
match = pattern.search(str) 
  
if match: 
    # 使用Match获得分组信息 
    substr = match.group()
    print match.group() 
    print match
    
### 输出 ### 
# hello 
