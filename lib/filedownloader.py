#!/usr/bin/env python
# encoding=utf-8
# Date:    2017-09-06
# Author:  pangjian
# version: 1.0

import requests
import os,sys
from log import Log

logger = None

class FileDownLoader(object):
	"""docstring for FileDownLoader"""
	def __init__(self, url):
		super(FileDownLoader, self).__init__()
		self.url = url

	def downloadgitfile(self, folder):
		try:
			token = self.gettoken_gitfile()
		except Exception as e:
			logger.outError(str(e))

		filename = os.path.basename(self.url)
		cookies = dict(remember_user_token = token)
		# cookies = dict(_gitlab_session=token)
		r = requests.get(self.url, cookies=cookies)

		try:
			f = open("%s/%s"%(folder,filename), 'wb')
			f.write(r.content)
		except Exception as e:
			logger.outMsg("download file error...")
			logger.outError(str(e))
		finally:
			f.close()

	def gettoken_gitfile(self):
		tokenfile = os.path.join(os.getcwd(), 'token.txt')
		content = ''
		try:
			f = open(tokenfile, 'rb')
			content = f.read()
		except Exception as e:
			logger.outError(str(e))
		finally:
			f.close()

		return content


if __name__ == '__main__':
	logger = Log('filedownloader.txt')
	if len(sys.argv) == 3:
		f = FileDownLoader(sys.argv[1])
		# print f.gettoken_gitfile()
		f.downloadgitfile(sys.argv[2])
	else:
		logger.outError('call paramter wrong...')
		sys.exit()

