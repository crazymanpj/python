#coding=utf-8
class MailInfo(object):
	"""docstring for MailInfo"""
	#根据邮件接口获取==========================================
	#邮件标题
	mailtitle = ""
	#测试
	tester = ""
	#发布时间
	publishtime = ""
	#邮件id号
	mailid = ""
	#邮件html格式
	mailhtml = ""

	#根据关键词匹配获取=========================================
	#产品
	pd = ""
	#提测是否合格
	isqualified = ""
	#文件信息
	fileinfo = []
	#修改点
	changelist = []
	#测试点
	checklist = []
	#不通过原因：
	notpassreason = ""

    #通过数据库获取的内容===========================================
    #发布数据路径
	datapath = ""
	#渠道
	channel = ""
	#子版本
	subchannel = ""
	#数据地址唯一id标识
	data_id = 0


	#无法获取的内容============================================
	#小组
	group = ""
	#所属模块
	modle = ""

	#==========================================================
	mailfilepath = "" 



	def __init__(self, datapath):
		super(MailInfo, self).__init__()
		self.datapath = datapath
