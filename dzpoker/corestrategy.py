#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-07-04
# Author:  pangjian
# version: 1.0
# gamer
#http://10.20.221.136/index.html?deskid=xxx观看比赛

from cards import Cards
import rule
from itertools import combinations
from rule_public import RulePublic

#同花顺
LEVEL_1 = 1
#四条    
LEVEL_2 = 10
#满堂红
LEVEL_3 = 50
#同花
LEVEL_4 = 100
#顺子
LEVEL_5 = 150
#三条
LEVEL_6 = 200
#两对
LEVEL_7 = 250
#一对
LEVEL_8 = 300
#高牌
LEVEL_9 = 350


def decideaction(level):
	pass

def makedecision_dipai(m_list):
	level = 9999
	m_list_point = sorted([x.point for x in m_list])
	m_list_color = sorted([x.color for x in m_list])
	if m_list_point[0]  == m_list_point[1]:

		if m_list_point[0] == 1:
			level = LEVEL_2

		elif m_list_point[0] >= 11:
			level = LEVEL_2 + 10

		else:
			level = LEVEL_2 + 40

	elif m_list_color[0] == m_list_color[1]:
		level = LEVEL_4

	else:
		if m_list_point[0] == 1:
			level = LEVEL_8

		elif m_list_point[1] >11:
			level = LEVEL_8 + 20

		else:
			level = LEVEL_9


	print level
	if (level < LEVEL_3):
		#加注跟住
		ret = 0
	elif(level <=LEVEL_8 + 20):
		#跟中
		ret = 2
	elif(level <=LEVEL_9):
		#跟小和盲注
		ret = 2
	else:
		#弃牌
		ret =3

	return ret

def makedecision_fanpai(public_list, m_list):
	# print m_list
	card_list = public_list + m_list
	# print card_list
	pr = RulePublic(public_list)

	ret_isFullhouse = rule.isFullhouse(card_list)
	ret_isThreeofakind = rule.isThreeofakind(card_list)
	ret_isTwoPair = rule.isTwoPairs(card_list)
	ret_isPair = rule.isPairs(card_list)
	if rule.isStraightFlush(card_list) == True and pr.isStraightFlush(public_list) != True:
		level = LEVEL_1

	elif rule.isFourofaKind(card_list) == True and pr.isFourofaKind(public_list) !=True:
		level = LEVEL_2

	elif ret_isFullhouse != False and pr.isFullhouse(public_list) != True:
		level = LEVEL_3

	elif rule.isFlush(card_list) == True and pr.isFlush(public_list) != True:
		level = LEVEL_4

	elif rule.isStraight(card_list) == True and pr.isStraight(public_list) != True:
		level = LEVEL_5

	elif ret_isThreeofakind != False and pr.isThreeofakind(public_list) != True:
		level = LEVEL_6

	elif ret_isTwoPair != False and pr.isTwoPairs(public_list) != True:
		level = LEVEL_7

	#对A
	elif ret_isPair != False and pr.isPairs(public_list) != True:
		if ret_isPair[0] == 1 or ret_isPair[1] >= 11:
			level = LEVEL_8
		else:
			level = LEVEL_8 + 30

	# gaopai
	else:
		level = LEVEL_9

	print 'level: ' + str(level)
	if (level <= LEVEL_6):
		# 加注跟住
		ret = 0
	elif (level == LEVEL_7):
		# 跟中
		ret = 1
	elif (level == LEVEL_8):
		ret = 1
	elif (level > LEVEL_8 and level <LEVEL_9):
		# 跟小
		ret = 2
	else:
		# 弃牌
		ret = 3

	return ret

def makedecision_hepai(public_list, m_list):
	r = rule.Rule(public_list, m_list)
	pr = RulePublic(public_list)
	combins = [c for c in combinations(public_list, 3)]
	bestscore = 0.0
	temp = []
	for i in combins:
		cardscom = list(i) + m_list
		# cardscom = sorted(cardscom)
		temp1 = [x.point for x in cardscom]
		print sorted(temp1)
		score = r.getScore(cardscom)

		if (score > bestscore):
			bestscore = score
			bestcardscom = i
			temp = [y.point for y in m_list] + [x.point for x in bestcardscom]
		else:
			continue

	print 'bestscore: ' + str(bestscore)
	print sorted(temp)
	prscore = pr.getScore()
	print 'prscore: ' + str(prscore)
	# temp1 = [x.point for x in bestcardscom]
	# temp2 = [y.point for y in self.m_list]
	# print temp1 + temp2

	if bestscore - prscore >= 40:
		ret = 0
	elif bestscore - prscore >= 20:
		ret = 1
	else:
		ret = 2

	# if (bestscore >= 100):
	# 	# 加注跟住
	# 	ret = 0
	# elif (bestscore >= 80 and bestscore <100):
	# 	# 跟中
	# 	ret = 1
	# elif (bestscore > 70 and bestscore <80):
	# 	ret =2
	# elif (bestscore > 60 and bestscore <=70):
	# 	# 跟小
	# 	ret = 2
	# else:
	# 	# 弃牌
	# 	ret = 3


	print ret
	return ret
	

if __name__ == '__main__':
	m_list = [Cards(40), Cards(36)]
	r = makedecision_dipai(m_list)
	print r

	public_list = [Cards(33), Cards(32), Cards(27), Cards(47), Cards(22)]
	pr = RulePublic(public_list)
	# print pr.getScore()
	m_list = [Cards(38), Cards(36)]
	print '-' *100
	print makedecision_hepai(public_list, m_list)
