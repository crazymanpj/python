#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-04-28
# Author:  pangjian
# version: 1.0
from hashlib import md5

def md5_file(filepath):
	m = md5()
	a_file = open(filepath, 'rb')
	m.update(a_file.read())
	a_file.close()
	return m.hexdigest()