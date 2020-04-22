#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-04-18
# Author:  pangjian
# version: 1.0

from django.http import HttpResponse

def json_response(jsondata, noarea=False):
	response = HttpResponse(jsondata, content_type='application/json')
	if noarea == True:
		response["Access-Control-Allow-Origin"] = "*"
	return response