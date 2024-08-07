#coding=utf-8
import os
import ConfigParser
import MailInfo
import codecs
import myconfig
import chardet
import re

class ParseMail(object):
	"""docstring for ParseMail"""

	configfile = os.path.join(os.getcwd(), "mailconfig.ini")
	mailcontent = ""

	def __init__(self):
		super(ParseMail, self).__init__()

	def parsemailallinfo(self, mailinfo):
		mailfilepath = mailinfo.mailfilepath
		h_mailfile = open(mailfilepath, "r")
		self.mailcontent = h_mailfile.readlines()

		mailinfo.pd = self.getpd()
		mailinfo.isqualified = self.getisqualified()
		mailinfo.changelist = self.getchangelist()
		print "查找测试内容"
		mailinfo.checklist = self.getchecklist()
		mailinfo.notpassreason = self.getnotpassreason()
		#mailinfo.fileinfo = self.getfileinfo()
		return True

	def formatmail(mailcontent):
		return mailcontent

	def getmailcontentbykeyword(self, keywordstart, keywordend):
		content = []
		isfind = 0
		keywordstart = unicode(keywordstart, "GB2312")
		keywordend = unicode(keywordend, "GB2312")
		print "keywordstart==========:    " + keywordstart
		print "keywordend==========:    " + keywordend
		for linetext in self.mailcontent:	

			#if len(linetext) < 2 and isfind == 1:
			#	break		

			if linetext == "" or len(linetext) < 2:
				continue				
			
			linetext = unicode(linetext, "utf-8")
			#print isinstance(keywordstart, unicode)
			#print isinstance(linetext, unicode)
			
			pattern_start = re.compile(keywordstart)
			pattern_end = re.compile(keywordend)

			match_start = pattern_start.search(linetext)
			#print "keyword: " + keywordstart 
			#print "content: " + linetext
			match_end = pattern_end.search(linetext)
			#print "endkeyword: " + keywordend
			
			if match_start and isfind == 0:
				print "find the start; " + keywordstart
				content.append(linetext)
				isfind = 1
				continue
			elif match_end and isfind == 1:
				print "find the end: "  + keywordend
				break
			elif isfind == 1:
				content.append(linetext)			
			else:
				continue	
		
		if isfind == 0:
			return ""
		else:
			print "result....................."
			for text in content:
				print text
			return content

	def getpd(self):
		keywordstart = myconfig.getconfigvalue(self.configfile, "keywordstart", "pd")
		keywordend = myconfig.getconfigvalue(self.configfile, "keywordend", "pd")
		pd = self.getmailcontentbykeyword(keywordstart, keywordend)
		ret = ""
		for i in pd:
			ret = ret + i
		return ret

	def getisqualified(self):
		keywordstart = myconfig.getconfigvalue(self.configfile, "keywordstart", "isqualified")
		keywordend = myconfig.getconfigvalue(self.configfile, "keywordend", "isqualified")
		isqualified = self.getmailcontentbykeyword(keywordstart, keywordend)
		ret = ""
		if len(isqualified) == 0:
			ret = "NULL"
		for i in isqualified:
			ret = ret + i
		return ret

	def getfileinfo(self):
		keywordstart = myconfig.getconfigvalue(self.configfile, "keywordstart", "fileinfo")
		keywordend = myconfig.getconfigvalue(self.configfile, "keywordend", "fileinfo")
		fileinfo = self.getmailcontentbykeyword(keywordstart, keywordend)
		return fileinfo

	def getchangelist(self):
		keywordstart = myconfig.getconfigvalue(self.configfile, "keywordstart", "changelist")
		keywordend = myconfig.getconfigvalue(self.configfile, "keywordend", "changelist")
		changelist = self.getmailcontentbykeyword(keywordstart, keywordend)
		ret = ""
		for i in changelist:
			ret = ret + i
		return ret

	def getchecklist(self):
		keywordstart = myconfig.getconfigvalue(self.configfile, "keywordstart", "checklist")
		keywordend = myconfig.getconfigvalue(self.configfile, "keywordend", "checklist")
		checklist = self.getmailcontentbykeyword(keywordstart, keywordend)
		ret = ""
		for i in checklist:
			ret = ret + i
		return ret

	def getnotpassreason(self):
		keywordstart = myconfig.getconfigvalue(self.configfile, "keywordstart", "notpassreason")
		keywordend = myconfig.getconfigvalue(self.configfile, "keywordend", "notpassreason")
		notpassreason = self.getmailcontentbykeyword(keywordstart, keywordend)
		ret = ""
		for i in notpassreason:
			ret = ret + i
		return ret

