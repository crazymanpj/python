#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-07-04
# Author:  pangjian
# version: 1.0
# gamer
#http://10.20.221.136/index.html?deskid=xxx观看比赛
import config

class Cards(object):
	"""docstring for Cards"""
	def __init__(self, num):
		super(Cards, self).__init__()
		self.num = num
		self.point = self.getcardspoint()
		self.color = self.getcardscolor()
		self.description =self.getdescription()

	def getcardspoint(self):
		if self.num >=0 and self.num <=13:
			return self.num
		elif self.num >=14 and self.num <=26:
			return self.num -13
		elif  self.num >=27 and self.num <=39:
			return self.num -26
		elif  self.num >=40 and self.num <=52:
			return self.num - 39
		
	def getcardscolor(self):
		if self.num >=0 and self.num <=13:
			return config.COLOR_FANGKUAI 
		elif self.num >=14 and self.num <=26:
			return config.COLOR_MEIHUA
		elif  self.num >=27 and self.num <=39:
			return config.COLOR_HONGTAO
		elif  self.num >=40 and self.num <=52:
			return config.COLOR_HEITAO

	def getdescription(self):
		text =""
		if self.num >=0 and self.num <=13:
			text = "方块" + str(self.point)
		elif self.num >=14 and self.num <=26:
			text = "梅花" + str(self.point)
		elif  self.num >=27 and self.num <=39:
			text = "红桃" + str(self.point) 
		elif  self.num >=40 and self.num <=52:
			text = "黑桃" + str(self.point)

		return text 


if __name__== '__main__':
	c =Cards(40)
	print c.getcardscolor()
	print c.getcardspoint()
	print c.getdescription()