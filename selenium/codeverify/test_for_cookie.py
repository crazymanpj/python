# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-06-25
# Author:  pangjian
from selenium import webdriver
import time,json

driver = webdriver.Chrome()
driver.get(r"")
time.sleep(50)

print 'end'
cookies = driver.get_cookies()
print (type(cookies))
# print ("".join(cookies))
f1 = open('cookie.txt', 'w')
f1.write(json.dumps(cookies))
f1.close

driver.close()

time.sleep(20)

# f1 = open('cookie.txt')
# cookie = f1.read()
# cookie =json.loads(cookie)
#
# for c in cookie:
#     print c
#     driver.add_cookie(c)
# # # 刷新页面
# driver.get(r'')
# driver.refresh()
