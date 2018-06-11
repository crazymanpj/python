# !/usr/bin/env python
# encoding=utf-8
# Date:    2018-05-28
# Author:  pangjian
from aip import AipOcr

APP_ID = '11312548'
API_KEY = 'F8VHIMmovwN8oaINsLHTYNXk'
SECRET_KEY = 'DVvrhcOjTAhRLphpgXjV9AuGRGinp1HQ'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    try:
        file = open(filePath, 'r')
        ret = file.read()
        return ret
    except:
        print 'read file error'
    finally:
        file.close()

""" 如果有可选参数 """
options = {}
options["language_type"] = "ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["probability"] = "true"

image = get_file_content('image2.jpg')
client.basicGeneral(image, options)
