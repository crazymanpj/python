#!/usr/bin/env python
#encoding=utf-8
# Date:    2017-07-04
# Author:  pangjian
# version: 1.0
# gamer
#http://10.20.221.136/index.html?deskid=xxx


import requests
import json
import time
import commonlib
import corestrategy
from cards import Cards
import rule
from msg import MsgQueue
import sys


# 加注跟住
BET_ADD = 0
# 跟中
BET_FOLLOW = 1
# 跟小和盲注
BET_SMALL = 2
# 弃牌
BET_QUIT =3


def login(username, password, session, deskid):
	url = 'http://10.20.221.136/login?deskid=%s&user=%s&pass=%s&callback='%(deskid,username, password)
	# print url
	r = session.post(url)
	print r.text
	print r.cookies
	#失败处理
	return r

def getallgamerinfo(deskid, t, session):
	url = 'http://10.20.221.136/getuinfo?deskid=%s&type=%s&callback='%(deskid, t)
	# print url
	r = session.post(url)
	return r

def bet(deskid, token, session, m_type, money):
	print 'bet start...'
	url = 'http://10.20.221.136/action?deskid=%s&token=%s&type=%s&money=%s&callback='%(deskid, token, m_type, money)
	print url
	r = session.post(url).text
	bet_ret = json.loads(r)
	if bet_ret['ret'] == 0:
		print 'bet success...'
		return True
	else:
		print 'bet fail...'
		print bet_ret['ret']
		return False

def getmsg(deskid, token, msgid, session):
	url = 'http://10.20.221.136/getmsg?deskid=%s&token=%s&msgid=%s&count=1&callback='%(deskid, token, msgid)
	r = session.post(url)
	return r

def parsemsg(msgtext, msgtype):
	# print 'msgtext: ' + msgtext
	return commonlib.base64_decode(msgtext)

def showdown(deskid, token, session, owncards, publiccards):
	print "showdown start..."
	print "public cards: "
	for i in publiccards:
		print i.num
	r = rule.Rule(publiccards, owncards)
	ret = r.getBestCardsCom()
	url = r'http://10.20.221.136/cards?deskid=%s&token=%s&card1=%s&card2=%s&card3=%s&callback='%(deskid, token, ret[0].num,ret[1].num, ret[2].num)
	print url
	showdown_ret = session.post(url).text
	showdown_ret = json.loads(showdown_ret)
	if showdown_ret['ret'] == 0:
		print 'tan pai success...'
		return True
	else:
		print 'tan pai fail...'
		print showdown_ret['ret']
		return False

def xiazhucaozuo(deskid, token, session, strategyret, bigestbet, xiazhuret, mywager, totalmoney):
	wtype_add = 3
	if xiazhuret:
		wtype_add = 3
	else:
		wtype_add = 5

	if strategyret == BET_ADD:
		if mywager > 10000 or bigestbet >5000:
			print '策略：跟注'
			if xiazhuret:
				ret = bet(deskid, token, session, 3, 200)
			else:
				ret = bet(deskid, token, session, 4, 0)
		else:
			print '策略：加注'
			ret = bet(deskid, token, session, wtype_add, totalmoney/20)

	if strategyret == BET_FOLLOW:
		if bigestbet > 5000 or mywager >5000:
			print '策略：跟住'
			ret = bet(deskid, token, session, 8, 0)
		if bigestbet > 1500 or mywager > 3000:
			print '策略：跟住'
			if xiazhuret:
				ret = bet(deskid, token, session, 3, 200)
			else:
				ret = bet(deskid, token, session, 4, 0)
		else:
			print '策略：加zhong住'
			ret = bet(deskid, token, session, wtype_add, totalmoney/200)

	if strategyret == BET_SMALL:
		if bigestbet >800 or mywager >1200:
			print '策略：弃牌'
			ret = bet(deskid, token, session, 8, 0)
		else:
			print '策略：跟小注'
			if xiazhuret:
				ret = bet(deskid, token, session, 3, 200)
			else:
				ret = bet(deskid, token, session, 4, 0)

	if strategyret == BET_QUIT:
		if bigestbet >500  or mywager >500:
			print '策略：弃牌'
			ret = bet(deskid, token, session, 8, 0)
		else:
			print '策略：跟小小注'
			if xiazhuret:
				ret = bet(deskid, token, session, 3, 100)
			else:
				ret = bet(deskid, token, session, 4, 0)

	return ret



def startpokergame(deskid):
	s = requests.Session()
	ret = login('pangjian', '111111', s, deskid)
	jsondata = json.loads(ret.text)
	if jsondata['ret'] == 0:
		print "登录成功"
	token = jsondata['token']
	set_id = jsondata['set_id']
	game_status = jsondata['game_status']
	msgid = jsondata['msg_id']
	print 'msgid: ' + str(msgid)
	print 'game_status: ' + str(game_status)
	nextmsgid = msgid
	ret = json.loads(getmsg(deskid, token, nextmsgid, s).text)
	lastmsgid = ret['last_msg_id']
	print 'last_msg_id: ' + str(lastmsgid)
	nextmsgid = lastmsgid
	record_msgid= 0
	public_list = []
	m_list = []
	currentmsgid = 0
	dicret = 99
	betret = [0, 0]
	game_status = 0
	m = MsgQueue(0)

	while True:
		ret = json.loads(getmsg(deskid, token, nextmsgid, s).text)
		if ret['ret'] != 0:
			time.sleep(0.2)
			continue
		try:
			lastmsgid = ret['last_msg_id']
			msgid = ret['msgs'][0]['msg_id']
		except:
			print ret
			time.sleep(0.2)
			continue

		if nextmsgid <= lastmsgid and msgid != lastmsgid:
			nextmsgid = msgid + 1
		elif msgid < lastmsgid:
			nextmsgid = msgid + 1

		#过滤重复消息
		if currentmsgid == lastmsgid:
			continue
		else:
			currentmsgid = msgid

		for im in ret['msgs']:
			jsondata = parsemsg(im['msg'], im['msg_type'])
			print 'type: ' + str(im['msg_type'])
			print 'jsondata: ' + jsondata

			jsondata = json.loads(jsondata)

			if im['msg_type'] == 1:
				print '用户状态：'
				print 'jsondata: ' + str(jsondata)
				userinfo = jsondata['users_info'][0]
				if userinfo['user'] == 'pangjian' and userinfo['user_status'] == 2 and dicret != 99 and len(m_list) > 0:
					if betret[1] != msgid:
						print "下注..."
						print "-----------------------------打印信息-------------------------------"
						xiazhuret = m.isneedxiazhu()
						bigestbet = m.getbigestwtype()
						totalmoney = m.totalmoney
						print "xiazhuret: " + str(xiazhuret)
						print "bigestbet: " + str(bigestbet)
						print "totalmoney" + str(totalmoney)
						m.printmsg()
						betret[0] = xiazhucaozuo(deskid, token, s, dicret, bigestbet, xiazhuret, userinfo['wager'], totalmoney)
						betret[1] = msgid

			if im['msg_type'] == 2:
				print '牌局状态：'
				print 'jsondata: ' + str(jsondata)
				if jsondata['game_status'] == 1:
					print 'qingling'
					public_list = []
					m_list = []
					dicret = 99
					betret = [0, 0]

				elif jsondata['game_status'] == 7 and len(m_list) > 0 and len(public_list) > 0:
					print 'tanpai start...'
					showdown(deskid, token, s, m_list, public_list)

				else:
					if m.game_status != jsondata['game_status']:
						m.game_status = jsondata['game_status']
						m.clearmsgqueue()
					print 'jixu'
					continue

			if im['msg_type'] == 3:
				print '发底牌：'
				print 'jsondata: ' + str(jsondata)
				dipai = jsondata['cards']
				print '-' * 100
				print 'dipai:'
				print dipai
				m_list = [Cards(dipai[0]), Cards(dipai[1])]
				print '底牌: ' + m_list[0].description, m_list[1].description
				dicret = corestrategy.makedecision_dipai(m_list)
				print dicret
				print 'dipai end...'

			if im['msg_type'] == 4:
				print '下注状态：'
				m.addmsg(jsondata)

			if im['msg_type'] == 5 and len(m_list) > 0:
				print '发公共牌：'
				print 'jsondata: ' + str(jsondata)
				publiccards = jsondata['cards']
				print '-' * 100
				if jsondata['public_cards_type'] == 1:
					print 'fanpai:'
					# print publiccards
					# print m_list
					public_list = [Cards(publiccards[0]), Cards(publiccards[1]), Cards(publiccards[2])]
					dicret = corestrategy.makedecision_fanpai(public_list, m_list)
					print dicret
					print 'fanpai end...'

				if jsondata['public_cards_type'] == 2:
					print 'zhuanpai:'
					# print publiccards
					# print public_list
					# print m_list
					c = Cards(publiccards[0])
					# print c
					public_list.append(c)
					# print public_list
					dicret = corestrategy.makedecision_hepai(public_list, m_list)
					print 'dicret: ' + str(dicret)
					print 'zhuanpai end...'

				if jsondata['public_cards_type'] == 3:
					print 'hepai:'
					print publiccards
					print public_list
					print m_list
					public_list.append(Cards(publiccards[0]))
					print public_list
					dicret = corestrategy.makedecision_hepai(public_list, m_list)
					print dicret
					print 'hepai end...'

			if im['msg_type'] == 6:
				print '牌局结果：'
				for i in jsondata['result']:
					if i['user'] == 'pangjian':
						print i
						print "底牌： " + Cards(i['hole_cards'][0]).description + ' ' + Cards(i['hole_cards'][1]).description
						print "赢得筹码：" + str(i['win_wager'])
						m.totalmoney = i['money']


		print '-' *100

		time.sleep(0.1)



if __name__ == '__main__':
	if len(sys.argv) == 2:
		deskid = sys.argv[1]
		print deskid
		startpokergame(deskid)