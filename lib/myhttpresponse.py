# !/usr/bin/env python
# encoding=utf-8
# Date:    2017-04-18
# Author:  pangjian
# version: 1.0

from django.http import HttpResponse
from . import myjson


def json_response(jsondata, noarea=False):
	response = HttpResponse(jsondata, content_type='application/json')
	if noarea:
		response["Access-Control-Allow-Origin"] = "*"
	return response


def mycommonerror_response(msg):
	errorcode = -1
	version = "1.0"
	ret_json = myjson.generatecommonjson(msg, errorcode, version)
	return json_response(ret_json, True)
