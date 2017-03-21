import json
import requests

url = r""

def postjson():
	body_value = {u"email": "", "password": ""}

def post():
	body_value = {u"email": "", u"": ""}
	r = requests.post("", data=body_value)
	print r.text

post()