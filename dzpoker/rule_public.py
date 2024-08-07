#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-07-12
# Author:  pangjian
# version: 1.0
# gamer
#http://10.20.221.136/index.html?deskid=xxx观看比赛

from itertools import combinations
from cards import Cards
from rule import Rule

class RulePublic(object):
	"""docstring for CardsCombine"""
	def __init__(self, public_list):
		super(RulePublic, self).__init__()
		self.public_list = public_list
		temp = [x.point for x in public_list]
		print temp

	def getScore(self):
		card_list = self.public_list

		card_list_point = [x.point for x in card_list]
		card_list_point = sorted(card_list_point)

		if self.isStraightFlush(card_list) == True:
			return self.getextrascore(200)

		elif self.isFourofaKind(card_list) == True:
			return self.getextrascore(200)

		elif self.isFullhouse(card_list) == True:
			return self.getextrascore(200)

		elif self.isFlush(card_list) == True:
			return self.getextrascore(140)

		elif self.isStraight(card_list) == True:
			return self.getextrascore(120)

		elif self.isThreeofakind(card_list) == True:
			return self.getextrascore(100)

		elif self.isTwoPairs(card_list) == True:
			return self.getextrascore(80)

		elif self.isPairs(card_list) == True:
			return self.getextrascore(60)

		#gaopai
		else:
			return self.getextrascore(40)

	def getextrascore(self, basescore):
		return basescore


	def isStraightFlush(self, m_list):
		if len(m_list) <5 :
			return False

		tempcolor = m_list[0].color
		for i in m_list:
			if tempcolor == i.color:
				continue
			else:
				return False

		cardlist = [x.point for x in m_list]
		cardlist = sorted(cardlist)
		# print cardlist
		if cardlist[-1] - cardlist[0] == 4:
			return True
		elif cardlist[0] == 1:
			cardlist[0] = 14
			cardlist = sorted(cardlist)
			if cardlist[-1] - cardlist[0] == 4:
				return True
			else:
				return False
		else:
			return False

	def isFourofaKind(self, m_list):
		if len(m_list) < 4:
			return False

		count = 0
		temppoint = m_list[0].point

		for i in m_list:
			if i.point == temppoint:
				count = count + 1

		if count == 4:
			return True
		else:
			count = 0
			temppoint = m_list[1].point
			for i in m_list:
				if i.point == temppoint:
					count = count + 1

			if count == 4:
				return True
			else:
				return False


	def countsamecardinlist(self, x, cardlist):
		count = 0
		for i in cardlist:
			if i == x:
				count = count + 1
		return count

	def isFullhouse(self, m_list):

		if len(m_list) < 5:
			return False

		count = 0
		cardlist = [x.point for x in m_list]
		cardlist = sorted(cardlist)
		# print cardlist
		temppoint = cardlist[0]

		count = self.countsamecardinlist(temppoint, cardlist)

		if count != 3 and count !=2:
			return False
		else:
			if count == 3:
				if cardlist[4] == cardlist[3]:
					return True
				else:
					return False
			else:
				count = self.countsamecardinlist(cardlist[2], cardlist)
				if count == 3:
					return True
				else:
					return False

	def isFlush(self, m_list):
		if len(m_list) < 5:
			return False

		tempcolor = m_list[0].color
		for i in m_list:
			if tempcolor == i.color:
				continue
			else:
				return False

		return True

	def isStraight(self, m_list):
		if len(m_list) < 5:
			return False

		cardlist = [x.point for x in m_list]
		cardlist = sorted(cardlist)
		# print cardlist
		istrue = False

		if cardlist[0] != 1:
			for i in range(0, 4):
				if cardlist[i] + 1 != cardlist[i+1]:
					return False

			return True
		else:
			cardlist[0] = 14
			cardlist = sorted(cardlist)
			for i in range(0, 4):
				if cardlist[i] + 1 != cardlist[i+1]:
					return False

			return True


	def isThreeofakind(self, m_list):
		count = 0
		cardlist = [x.point for x in m_list]
		cardlist = sorted(cardlist)

		count = self.countsamecardinlist(cardlist[0], cardlist)
		if count !=3:
			count = self.countsamecardinlist(cardlist[1], cardlist)
			if count !=3:
				count = self.countsamecardinlist(cardlist[2], cardlist)
				if count == 3:
					return True
				else:
					return False
			else:
				return True

		else:
			return True

	def isTwoPairs(self, m_list):
		if len(m_list) < 4:
			return False

		count = 0
		cardlist = [x.point for x in m_list]
		cardlist = sorted(cardlist)
		# print cardlist
		temppoint = cardlist[0]

		if cardlist[0] == cardlist[1]:
			if cardlist[2] == cardlist[3]:
				return True
			elif len(m_list) == 5:
				if cardlist[3] == cardlist[4]:
					return True
			else:
				return False
		elif len(m_list) == 5:
			if cardlist[1] == cardlist[2] and cardlist[3] == cardlist[4]:
				return True
			else:
				return False

	def isPairs(self, m_list):

		cardlist = [x.point for x in m_list]
		for i in cardlist:
			count = self.countsamecardinlist(i, cardlist)
			if count == 2:
				return True
			else:
				continue

		return False


if  __name__ == '__main__':
	pass