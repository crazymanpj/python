#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-07-04
# Author:  pangjian
# version: 1.0
# gamer
#http://10.20.221.136/index.html?deskid=xxx观看比赛

from itertools import combinations
from cards import Cards

class Rule(object):
	"""docstring for CardsCombine"""
	def __init__(self, public_list, m_list):
		super(Rule, self).__init__()
		# self.public_list = [x.point for x in public_list]
		# self.m_list = [y.point for y in m_list]
		self.public_list = public_list
		self.m_list = m_list
		# print self.public_list
		# print self.m_list


	def getBestCardsCom(self):
		# print self.public_list
		# print self.m_list
		combins = [c for c in combinations(self.public_list, 3)]
		print '-' * 100
		bestcardscom = []
		bestscore = 0.0
		for i in combins:
			cardscom = list(i) + self.m_list
			# cardscom = sorted(cardscom)
			temp1 = [x.point for x in i]
			temp2 = [y.point for y in self.m_list]
			print temp1 + temp2
			score = self.getScore(cardscom)
			print 'score: ' + str(score)
			if (score > bestscore):
				bestscore = score
				bestcardscom = i
			else:
				continue

		print '*' * 100
		print bestcardscom
		temp1 = [x.point for x in bestcardscom]
		temp2 = [y.point for y in self.m_list]
		print temp1 + temp2
		return bestcardscom

	def getScore(self, card_list):
		ret_isFullhouse = isFullhouse(card_list)
		ret_isThreeofakind = isThreeofakind(card_list)
		ret_isTwoPair = isTwoPairs(card_list)
		ret_isPair = isPairs(card_list)

		card_list_point = [x.point for x in card_list]
		card_list_point = sorted(card_list_point)

		if isStraightFlush(card_list) == True:
			return self.getextrascore(200, card_list_point)

		elif isFourofaKind(card_list) == True:
			return self.getextrascore(200, card_list_point)

		elif ret_isFullhouse != False:
			return self.getextrascore_forFullhouse(200, card_list_point, ret_isFullhouse)

		elif isFlush(card_list) == True:
			return self.getextrascore(140, card_list_point)

		elif isStraight(card_list) == True:
			return self.getextrascore(120, card_list_point)

		elif ret_isThreeofakind != False:
			return self.getextrascore_forthree(100, card_list_point, ret_isThreeofakind)

		elif ret_isTwoPair != False:
			return self.getextrascore_fortwopair(80, card_list_point, ret_isTwoPair)

		elif ret_isPair != False:
			return self.getextrascore_pair(60, ret_isPair)

		#gaopai
		else:
			return self.getextrascore_bigcard(40, card_list_point)

	def getextrascore(self, basescore, card_list):
		extrascore = 0
		if card_list[0] == 1:
			extrascore = 14
		else:
			extrascore = card_list[-1]

		return basescore + extrascore

	def getextrascore_forFullhouse(self, basescore, card_list, point):
		extrascore = 0

		if point == 1:
			extrascore = 14
		else:
			extrascore = point

		return basescore +extrascore

	def getextrascore_forthree(self, basescore, card_list, point):
		extrascore = 0
		if point ==1:
			extrascore =14
		else:
			if card_list[0] == 1:
				card_list[-1] = 14
			extrascore = point

		return basescore + extrascore + card_list[-1]/10

	def getextrascore_fortwopair(self, basescore, card_list, retlist):
		extrascore = 0
		if retlist[0] ==1:
			extrascore = 14 + retlist[1]/10 + retlist[2]/100
		else:
			if retlist[2] ==1:
				retlist[2] = 14
			extrascore = retlist[1] + retlist[0]/10 +retlist[2]/100

		return basescore +extrascore

	def getextrascore_pair(self, basescore, retlist):
		extrascore = 0
		# print retlist
		if retlist[0] == 1:
			basescore = basescore + 14
		else:
			basescore = basescore + retlist[0]

		if retlist[1] == 1:
			extrascore = 14/10
		else:
			extrascore = retlist[1]/10

		return basescore + extrascore

	def getextrascore_bigcard(self, basescore, cardlist):
		extrascore = 0
		if cardlist[0] ==1:
			extrascore = 14
		else:
			extrascore = cardlist[-1]

		return basescore +extrascore



def isStraightFlush(m_list):
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

def isFourofaKind(m_list):
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


def countsamecardinlist(x, cardlist):
	count = 0
	for i in cardlist:
		if i == x:
			count = count + 1
	return count

def isFullhouse(m_list):
	count = 0
	cardlist = [x.point for x in m_list]
	cardlist = sorted(cardlist)
	# print cardlist
	temppoint = cardlist[0]

	count = countsamecardinlist(temppoint, cardlist)

	if count != 3 and count !=2:
		return False
	else:
		if count == 3:
			if cardlist[4] == cardlist[3]:
				return temppoint
			else:
				return False
		else:
			count = countsamecardinlist(cardlist[2], cardlist)
			if count == 3:
				return cardlist[2]
			else:
				return False

def isFlush(m_list):
	tempcolor = m_list[0].color
	for i in m_list:
		if tempcolor == i.color:
			continue
		else:
			return False

	return True

def isStraight(m_list):
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


def isThreeofakind(m_list):
	# print "isThreeofakind start..."
	count = 0
	cardlist = [x.point for x in m_list]
	cardlist = sorted(cardlist)
	# print cardlist
	# temppoint = cardlist[0]

	count = countsamecardinlist(cardlist[0], cardlist)
	if count !=3:
		count = countsamecardinlist(cardlist[1], cardlist)
		if count !=3:
			count = countsamecardinlist(cardlist[2], cardlist)
			if count == 3:
				return cardlist[2]
			else:
				return False
		else:
			return cardlist[1]

	else:
		return cardlist[0]

def isTwoPairs(m_list):
	count = 0
	cardlist = [x.point for x in m_list]
	cardlist = sorted(cardlist)
	# print cardlist
	temppoint = cardlist[0]

	if cardlist[0] == cardlist[1]:
		if cardlist[2] == cardlist[3]:
			return [cardlist[0], cardlist[2], cardlist[4]]
		elif cardlist[3] == cardlist[4]:
			return [cardlist[1],cardlist[3], cardlist[2]]
		else:
			return False
	elif cardlist[1] == cardlist[2] and cardlist[3] == cardlist[4]:
		return [cardlist[1], cardlist[3], cardlist[0]]
	else:
		return False


def getBigCard_Pairs(m_list, x):
	m_list = sorted(m_list)
	if m_list[0] == 1 and m_list[0] != x:
		return m_list[0]
	m_list = m_list[::-1]
	for i in m_list:
		if i == x:
			continue
		else:
			return i


def isPairs(m_list):
	cardlist = [x.point for x in m_list]
	# print cardlist
	for i in cardlist:
		count = countsamecardinlist(i, cardlist)
		if count == 2:
			bigcard = getBigCard_Pairs(cardlist, i)
			return [i,bigcard]
		else:
			continue

	return False


if  __name__ == '__main__':
	public_list = [Cards(4), Cards(2), Cards(27), Cards(40), Cards(14)]
	ret = isPairs(public_list)
	if ret != False:
		print ret
	m_list = [Cards(1), Cards(6)]
	r = Rule(public_list, m_list)
	r.getBestCardsCom()