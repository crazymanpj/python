#coding=utf-8
import imaplib
import string
import email
from email.iterators import _structure
import sys
import chardet
import os
import codecs
from MailInfo import MailInfo
from ParseMail import ParseMail
from MysqlHelper import MysqlHelper
import myconfig
import markdown
import datetime
reload(sys)
sys.setdefaultencoding('utf-8')

class MailManager:
    IMAP_SERVER = ""
    IMAP_PORT = ""
    M = ""
    response = ""
    mailboxes = ""
    def __init__(self): 
        self.IMAP_SERVER='imap.gmail.com'
        self.IMAP_PORT=993
        self.M = None
        self.response
        self.mailboxes = [] 
        
    def login(self, username, password): 
        self.M = imaplib.IMAP4_SSL(self.IMAP_SERVER, self.IMAP_PORT) 
        rc, self.response = self.M.login(username, password) 
        return rc 
    
    def get_first_text_block(self,email_message_instance):
        maintype = email_message_instance.get_content_maintype()
        if maintype == 'multipart':
            _structure(email_message_instance)
            for part in email_message_instance.walk():
                print part.get_payload(decode=True)
                if part.get_content_maintype() == 'text':
                    text = part.get_payload(decode=True)
                    encod = chardet.detect(text)
                    print encod['encoding'] + "\r\n"
                    if encod['encoding'] != None:
                        temp = text.decode(encod['encoding'], 'ignore')
                        return temp
                    return text
                    
            for part in email_message_instance.get_payload():
                #print part
                if part.get_content_maintype() == 'text':
                    text = part.get_payload(decode=True).strip()
                    encod = chardet.detect(text)
                    print encod['encoding'] + "\r\n"
                    if encod['encoding'] != None:
                        temp = text.decode(encod['encoding'], 'ignore')
                        return temp
                    return text
        elif maintype == 'text':
            _structure(email_message_instance)
            text = email_message_instance.get_payload(decode=True).strip()  
            print text
            encod = chardet.detect(text)
            print encod['encoding'] + "\r\n"
            if encod['encoding'] != None:
                temp = text.decode(encod['encoding'], 'ignore')
                return temp
            return text
        
    def receive_mail(self):       
        recvMail = receiveMail.ReceiveMail(self.M) 
        mailCounts = recvMail.get_mail_count()
        print 'A total of '+ mailCounts +' mails in your input mailbox.'
        print 'A total of '+recvMail.get_unread_count()+ ' UNREAD mails in your input mailbox.'
        recvMail.get_imap_quota()
        mailBody = recvMail.check_simpleInfo(mailCounts) #返回值是邮件content
        if mailBody != 0:
            recvMail.check_detailInfo(mailBody)
        return    
    
    def get_mail_content(self, content):
        print 'MailContent:'+'\n'+ content #直接将内容显示到了终端    
    
    def check_detailInfo(self, mailBody):
        print "Input 'y' to check the detailInfo. Other cmds to abandon!"
        while True:
            args = string.split(raw_input('$====>'))
            if len(args)!=0:
                if args[0] == 'y':
                    self.get_mail_content(mailBody)
                    return
                else:
                    break
            else:
                pass
        else:
            pass       
        
    def get_mail_simpleInfo_from_id(self, id): 
        status, response = self.M.fetch(id,"(RFC822)")
        mailText = response[0][1]
        mail_message = email.message_from_string(mailText)
        subject = unicode(email.Header.make_header(email.Header.decode_header(mail_message['subject'])))
        #print "subject_________:" +subject
        mail_from = email.utils.parseaddr(mail_message["from"])[1]
        mail_to = email.utils.parseaddr(mail_message["to"])[1]
        time = mail_message['Date']
        print '['+mail_message['Date']+']'+'\n'+'From:'+mail_from+ ' To:'+mail_to+'\n'+'Subject:'+subject+'\n'
        return self.get_first_text_block(mail_message), subject, mail_from, time
    
    def check_simpleInfo(self, mailCounts):
        mailBody, mailsubject, mail_from, time = self.get_mail_simpleInfo_from_id(mailCounts)
        print "subject_________:" +mailsubject
        return mailBody, mailsubject, mail_from, time
    
    def getMailSubject():
        return mailsubject

    #by crazymanpj 7.25  获取数据库中的频道信息
    def getlanguageandchannel(self, mailinfo, datapath):
        #mysql查询需要转义反斜杠
        #datapath = datapath.strip(r"\n")
        datapath = datapath.replace('\\', '\\\\')
        print datapath
        sql_language = "select language from dubadata_data where path_223 = '%s'" %datapath
        print sql_language
        mysqlhelper = MysqlHelper()
        language = mysqlhelper.query_data(sql_language)
        print language
        sql_channel = "select channel from dubadata_data where path_223 = '%s'" %datapath
        print sql_channel
        channel = mysqlhelper.query_data(sql_channel)
        print channel
        return language[0][0], channel[0][0]

    #by pj 7.25
    def getallfileinfo(self, mailinfo, datapath):
        #mysql查询需要转义反斜杠
        #datapath = datapath.strip(r"\r\n")
        datapath = datapath.replace('\\', '\\\\')
        print datapath
        id_sql = "select id from dubadata_data where path_223 = '%s'" %datapath
        print id_sql
        mysqlhelper = MysqlHelper()
        ret = mysqlhelper.query_data(id_sql)
        id = ret[0][0]
        allfileinfo_sql = "select filename,fileversion from dubadata_publishfile where data_id = '%s'" %id
        print allfileinfo_sql
        allfileinfo = mysqlhelper.query_data(allfileinfo_sql)
        print allfileinfo
        return allfileinfo

    #by pj 8.1
    def getdataid(self, mailinfo, datapath):
        #mysql查询需要转义反斜杠
        #datapath = datapath.strip(r"\r\n")
        datapath = datapath.replace('\\', '\\\\')        
        sql = "select id from dubadata_data where path_223 = '%s'" %datapath
        print sql
        mysqlhelper = MysqlHelper()
        ret = mysqlhelper.query_data(sql)
        print ret
        data_id = int(ret[0][0])
        print data_id
        return data_id

    #by pj 8.1
    def getmailhtml(self, mailinfo, mailtext):
        md = markdown.Markdown()
        html = md.convert(mailtext)
        #print html
        return html

    def encrypt(self, key, s):     
        b = bytearray(str(s).encode("gbk"))     
        n = len(b) # 求出 b 的字节数     
        c = bytearray(n*2)     
        j = 0
        for i in range(0, n):     
            b1 = b[i]     
            b2 = b1 ^ key # b1 = b2^ key     
            c1 = b2 % 16
            c2 = b2 // 16 # b2 = c2*16 + c1     
            c1 = c1 + 65
            c2 = c2 + 65 # c1,c2都是0~15之间的数,加上65就变成了A-P 的字符的编码     
            c[j] = c1     
            c[j+1] = c2     
            j = j+2
        return c.decode("gbk")     

    def decrypt(self, key, s):     
        c = bytearray(str(s).encode("gbk"))     
        n = len(c) # 计算 b 的字节数     
        if n % 2 != 0 :     
            return ""     
        n = n // 2
        b = bytearray(n)     
        j = 0
        for i in range(0, n):     
            c1 = c[j]     
            c2 = c[j+1]     
            j = j+2
            c1 = c1 - 65
            c2 = c2 - 65
            b2 = c2*16 + c1     
            b1 = b2^ key     
            b[i]= b1     
        try:     
            return b.decode("gbk")     
        except:     
            return "decrypt failed"

    def getusernameandpsw(self):
        key = myconfig.getconfigvalue("mailconfig.ini", "userconfig", "key")
        username = myconfig.getconfigvalue("mailconfig.ini", "userconfig", "user")
        password = myconfig.getconfigvalue("mailconfig.ini", "userconfig", "psd")
        username = self.decrypt(int(key), username)
        password = self.decrypt(int(key), password)
        return username,password

    def getSourceData(self):
        file = "RealseData.txt"
        h_file = open(file, "rb")
        text = h_file.readlines()
        h_file.close()
        return text

    def outputResult(self, result, filename):
        relativePath = "result"
        if os.path.exists(os.path.join(os.getcwd(), relativePath)) == False:
            os.mkdir(os.path.join(os.getcwd(), relativePath))
        
        path = os.path.join(os.getcwd(), relativePath)
        file = codecs.open(os.path.join(path, filename), "a+", "utf-8")
        file.write(result)
        file.close()

    def outputParseResult(self, mailinfo, filename):
        relativePath = "parse"
        if os.path.exists(os.path.join(os.getcwd(), relativePath)) == False:
            os.mkdir(os.path.join(os.getcwd(), relativePath))

        parsepath = os.path.join(os.getcwd(), relativePath)
        file = codecs.open(os.path.join(parsepath, filename), "a+", "utf-8")
        file.write(u"================获取结果====================\r\n")
        file.write("\r\n")
        file.write(u"====数据路径:====\r\n")
        file.writelines(mailinfo.datapath + "\r\n")
        file.write("\r\n")
        file.write(u"====频道:====\r\n")
        file.writelines(mailinfo.channel + "\r\n")
        file.write("\r\n")
        file.write(u"====子版本:====\r\n")
        file.writelines(mailinfo.subchannel + "\r\n")
        file.write("\r\n")
        file.write(u"====邮件标题:====\r\n")
        file.writelines(mailinfo.mailtitle + "\r\n")
        file.write("\r\n")
        file.write(u"====产品:====\r\n")
        file.writelines(mailinfo.pd)
        file.write("\r\n")
        file.write(u"====修改内容:====\r\n")
        file.writelines(mailinfo.changelist)
        file.write("\r\n")
        file.write(u"====测试点:====\r\n")
        file.writelines(mailinfo.checklist)
        file.write("\r\n")
        file.write(u"====是否合格:====\r\n")
        file.writelines(mailinfo.isqualified)
        file.write("\r\n")
        file.write(u"====不通过原因:====\r\n")
        file.writelines(mailinfo.notpassreason)
        file.write("\r\n")
        file.write(u"====文件信息:====\r\n")
        #for i in mailinfo.fileinfo:
         #   file.writelines(i[0] + " " + i[1])
         #   file.write("\r\n")
        file.close()

    def writemailinfotodb(self, mailinfo):
        sql = "insert into dubadata_mailinfo(data_id, mailtitle, tester, publishtime, mailid, pd, isqualified, fileinfo, changelist, checklist, notpassreason, datapath, channel, subchannel) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        enc = chardet.detect(sql)
        print enc['encoding']
        print type(sql)
        print type(mailinfo.mailtitle)
        #, channel, subchannel , , mailinfo.channel, mailinfo.subchannel
        print sql
        sqlmanger =MysqlHelper()
        sqlmanger.execute_sql_mailinfo(sql, mailinfo)
        return True

    def formatfileinfo(self, alltext):
        ret = ""
        for i in alltext:
            ret = ret + i[0] + " " + i[1] + "\r\n"
        return ret

    def searchmailbyarray(self, sourcedata):
        #sourcedata = getSourceData()
        m = MailManager()
        #解密用户名和密码
        username,password = self.getusernameandpsw()
        t = m.login(username, password)
        tye,data = m.M.select()
        print tye,data

        i = 0
        for datapath in sourcedata:
            i = i + 1
            result = ""
            #keyword = "%(path)s" % {'path': datapath}
            datapath = datapath.strip("\r\n")
            print datapath
            ret, msgnums = m.M.search(None, 'BODY', datapath)
            if msgnums[0] == "":
                print "can not find the relative mail"
                result = "can not find the relative mail"
                self.outputResult(result, str(i) + ".txt")
                continue
            print msgnums
            numlist = msgnums[0].split(" ")
            print numlist[0]
            testnum = numlist[0]
            #print testnum
            mailinfo = MailInfo(datapath)

            mailinfo.data_id = self.getdataid(mailinfo, datapath)
            print "datapath is: " + datapath
            print "==========data_id is: " + str(mailinfo.data_id) + "==================================="
            mailBody, mailsubject, mail_from, time = m.check_simpleInfo(testnum)
            mailinfo.mailtitle = mailsubject
            #enc = chardet.detect(mailsubject)
            #print enc['encoding']

            time = datetime.datetime.strptime(time, "%a, %d %b %Y %H:%M:%S +0800")
            time.strftime('%Y-%m-%d %H:%M:%S')
            mailinfo.publishtime = time
            print mailinfo.publishtime
            mailinfo.tester = mail_from
            mailinfo.mailid = testnum
            mailinfo.datapath = datapath
            #print chardet.detect(mailBody)
            #print mailBody
            #m.check_detailInfo(mailBody)
            self.outputResult(mailBody, str(i) + ".txt")

            mailinfo.channel, mailinfo.subchannel = self.getlanguageandchannel(mailinfo, datapath)
            mailinfo.fileinfo = self.getallfileinfo(mailinfo, datapath)
            #转化成一个字符串
            mailinfo.fileinfo = self.formatfileinfo(mailinfo.fileinfo)
            #mailinfo.mailhtml = self.getmailhtml(mailinfo, mailBody)

            resultfile = os.path.join(os.getcwd(), "result", str(i)+".txt")
            print resultfile
            MailInfo.mailfilepath = resultfile
            parsemail = ParseMail()
            parsemail.parsemailallinfo(mailinfo)
            self.outputParseResult(mailinfo, str(i) + ".txt")
            self.writemailinfotodb(mailinfo)