#!/usr/bin/env python
# encoding=utf-8
# Date:    2017-07-24
# Author:  pangjian
import smtplib
from email.mime.text import MIMEText
import config
import traceback


def send_mail(to_list, sub, content):
	totext = ''
	me = config.mail_user + config.mail_postfix
	print me
	msg = MIMEText(content, _subtype='plain', _charset='utf-8')
	msg['Subject'] = sub
	msg['From'] = me
	for i in to_list:
		totext = totext + ';' + i
	print '-------------------'
	print totext
	msg['To'] = totext
	print to_list

	try:
		server = smtplib.SMTP(mail_server, mail_server_port)
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
		server.login(config.mail_user, config.mail_pass)
		server.sendmail(me, to_list, msg.as_string())
		server.quit()
		return True
	except Exception, e:
		print str(e)
		traceback.print_exc()
		return False

def send_mail2(to_list, sub, content, mailformat):
	totext = ''
	me = config.mail_user + config.mail_postfix
	print me
	msg = MIMEText(content, _subtype=mailformat, _charset='utf-8')
	msg['Subject'] = sub
	msg['From'] = me
	for i in to_list:
		totext = totext + ';' + i
	print '-------------------'
	print totext
	msg['To'] = totext
	print to_list

	try:
		server = smtplib.SMTP(mail_server, mail_server_port)
		server.ehlo()
		server.starttls()
		print '------------'
		server.login(config.mail_user, config.mail_pass)
		server.sendmail(me, to_list, msg.as_string())
		server.quit()
		return True
	except Exception, e:
		print str(e)
		traceback.print_exc()
		return False




if __name__ == '__main__':
	html = """\
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>萌店AB环境</title>
<body>
<div id="container">
<p><strong>萌店sla状态统计</strong></p>
<p>采集时间: """ + 'timezone' + """</p>
<div id="content">
 <table width="500" border="2" bordercolor="red" cellspacing="2">
<tr>
  <td><strong>站点</strong></td>
  <td><strong>总访问量</strong></td>
  <td><strong>正常数</strong></td>
  <td><strong>正常百分比</strong></td>
  <td><strong>异常数</strong></td>
  <td><strong>异常百分比</strong></td>
</tr>
<tr>
  <td><a href="http://log.xxx.com/#/dashboard/file/node.json">node</a></td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
</tr>
<tr>
  <td><a href="http://log.xxxlcom/#/dashboard/file/api.json">api</a></td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
</tr>
<tr>
  <td><a href="http://log.xxx.com/#/dashboard/file/mapi.json">mapi</a></td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
</tr>
<tr>
  <td><a href="http://log.xxx.com/#/dashboard/file/yunying-sla.json">yunying</a></td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
  <td>""" + 'a[4]' + """</td>
</tr>
</table>
</div>
</div>
<p><strong>点击站点名可查看详细表图</strong> </p>
</div>
</body>
</html>
      """
	if send_mail2(mailto_list, 'hello', html, 'html'):
		print '发送成功'
	else:
		print '发送失败'