#!/usr/bin/env python
# encoding=utf-8
# Date:    2017-07-24
# Author:  pangjian
import smtplib
from email.mime.text import MIMEText
# import config
from mail_config import MAIL_HOST, MAIL_PASS, MAIL_USER, MAIL_POSTFIX, MAIL_SERVER, MAIL_SERVER_PORT, MAILTO_LIST
import traceback




def send_mail(to_list, sub, content):
	totext = ''
	me = MAIL_USER + MAIL_POSTFIX
	print me
	msg = MIMEText(content, _subtype='plain', _charset='utf-8')
	msg['Subject'] = sub
	msg['From'] = me
	for i in MAILTO_LIST:
		totext = totext + ';' + i
	print '-------------------'
	print totext
	msg['To'] = totext
	print MAILTO_LIST

	try:
		server = smtplib.SMTP(MAIL_SERVER, MAIL_SERVER_PORT)
		# server.set_debuglevel(1)
		server.ehlo()
		server.starttls()
		print '------------'
		# print config.mail_user
		# print config.mail_pass
		# ret = server.login(config.mail_user, config.mail_pass)
		# print '---------------'
		# print 'ret:'
		# print ret
		server.login(MAIL_USER, MAIL_PASS)
		server.sendmail(me, MAILTO_LIST, msg.as_string())
		server.quit()
		return True
	except Exception, e:
		print str(e)
		traceback.print_exc()
		return False

def send_mail2(to_list, sub, content, mailformat):
	totext = ''
	me = MAIL_USER + MAIL_POSTFIX
	print me
	msg = MIMEText(content, _subtype=mailformat, _charset='utf-8')
	msg['Subject'] = sub
	msg['From'] = me
	for i in MAILTO_LIST:
		totext = totext + ';' + i
	print '-------------------'
	print totext
	msg['To'] = totext
	print MAILTO_LIST

	try:
		server = smtplib.SMTP(MAIL_SERVER, MAIL_SERVER_PORT)
		server.ehlo()
		server.starttls()
		print '------------'
		server.login(MAIL_USER, MAIL_PASS)
		server.sendmail(me, MAILTO_LIST, msg.as_string())
		server.quit()
		return True, ''
	except Exception, e:
		print str(e)
		traceback.print_exc()
		return False, traceback.print_exc()




if __name__ == '__main__':
	html = 'test'
	if send_mail2(MAILTO_LIST, 'hello', html, 'html'):
		print '发送成功'
	else:
		print '发送失败'
