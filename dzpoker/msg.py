#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-07-13
# Author:  pangjian
# version: 1.0
# gamer
#http://10.20.221.136/index.html?deskid=xxx观看比赛
class MsgQueue(object):
	"""docstring for MsgQueue"""
	def __init__(self, game_status):
		super(MsgQueue, self).__init__()
		self.game_status = game_status
		self.msglist = []
		self.totalmoney = 100000

	def addmsg(self, msg):
		self.msglist.append(msg)

	def clearmsgqueue(self):
		self.msglist = []

	def printmsg(self):
		print "game_status: " + str(self.game_status)
		for i in self.msglist:
			print i


	def isneedxiazhu(self):
		if self.game_status == 4 or self.game_status == 5 or self.game_status ==6:
			if len(self.msglist) == 0:
				return True

			elif self.msglist[0]['wager_type'] == 7 or self.msglist[0]['wager_type'] == 8:
				return True

		return False

	def getbigestwtype(self):
		temp = [x['money'] for x in self.msglist]
		temp = sorted(temp)
		print(temp)
		if len(temp) > 0:
			return temp[-1]
		else:
			return 0