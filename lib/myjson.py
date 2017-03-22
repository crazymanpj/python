import json
from datetime import date,datetime

def __default(obj):
	if isinstance(object, datetime):
		return obj.strftime('%Y-%m-%dT%H:%M:%S')
	elif isinstance(obj, date): 
		return obj.strftime('%Y-%m-%d') 
	else: 
		raise TypeError('%r is not JSON serializable' % obj) 



def generatecommonjson(msg, errorcode, version):
	ret_json= {}
	ret_json['msg'] = msg
	ret_json['errorcode'] = errorcode
	ret_json['version'] = version

	ret = json.dumps(ret_json)

	return ret

def generateitemjson(msg, errorcode, version, itemlistname, itemlist):
	ret_json={}
	ret_json['msg'] = msg
	ret_json['errorcode'] = errorcode
	ret_json['version'] = version
	ret_json[itemlistname] = itemlist

	ret = json.dumps(ret_json, default=__default)
	return ret

def generaetmultijson(msg, errorcode, version, itemlistnames, itemlists):
	ret_json={}
	ret_json['msg'] = msg
	ret_json['errorcode'] = errorcode
	ret_json['version'] = version
	for i in range(len(itemlistnames)):
		ret_json[itemlistnames[i]] = itemlists[i]

	ret = json.dumps(ret_json, default=__default)
	return ret