# !/usr/bin/env python
# encoding=utf-8
# Date:    2016-10-20
# Author:  pangjian
import os, subprocess,sys, shutil
from ftplib import FTP
import logging
from hashlib import md5
import xml.dom.minidom
import winhelper
import traceback
import zipfile
import re
import axmlparserpy.axmlprinter as axmlprinter
from xml.dom import minidom
# from cm import config
from config import FTP_CM_PASSWORD, FTP_CM_USERNAME, FTP_CMS_PASSWORD, FTP_CMS_USERNAME


import sys
reload(sys)
exec("sys.setdefaultencoding('utf-8')");

logger = logging.getLogger('mobiledata_cm')
BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
DOWNLOAD_DIR = os.path.join(BASE_DIR, "download")

def getfilefromftp(url, user, password):
	logger.debug(url)
	logger.debug(user)
	logger.debug(password)
	filename = os.path.basename(url)
	logger.debug(filename)
	# n_domain_start = url.index("ftp://")
	# n_domain_end = url.index("/", 7)
	# domain = url[n_domain_start + 6 : n_domain_end]
	domain = winhelper.getftpdomain(url)
	lenofdomain = len(domain)
	if domain.find("10.60") >= 0:
		domain = domain.strip("ftpadm@")
	logger.debug(domain)
	if url:
		subpath = os.path.dirname(url[7 + lenofdomain : len(url)])
		logger.debug(subpath)
	ftp = FTP(domain, user, password)
	try:
		ftp.cwd(subpath)
	except:
		logger.debug('download path error...')
		sys.exit()
	h_downloadfile = open(filename, "wb")
	logger.debug(r"RETR %s"%(filename))
	ftp.retrbinary(r"RETR %s"%(filename), h_downloadfile.write)
	logger.debug("get file %s ok"%(filename))
	h_downloadfile.close()
	srcfile = os.path.join(os.getcwd(), filename)
	logger.debug(srcfile)
	distfile = os.path.join(DOWNLOAD_DIR, filename)
	logger.debug(distfile)
	try:
		shutil.move(srcfile, distfile)
	except:
		logger.debug("move file to download_dir error")
	return True

def getfilepath(apkfilepath):
	user = "ftpadm"
	password = "ftpaadm123"
	#通过判断域名支持不同ftp地址
	logger.debug(apkfilepath)
	if apkfilepath.find("ftp") == 0:
		domain = winhelper.getftpdomain(apkfilepath)
		if domain.find("10.60") >= 0:
			logger.debug("the package path is cm...")
			getfilefromftp(apkfilepath, FTP_CM_USERNAME, FTP_CM_PASSWORD)
		elif domain.find("dubabin") >=0:
			logger.debug("the package path is cms...")
			getfilefromftp(apkfilepath, FTP_CMS_USERNAME, FTP_CMS_PASSWORD)
		else:
			logger.debug("unknow ftp path...")
	elif os.path.exists(apkfilepath):
		logger.debug("return local path")
		return apkfilepath

	# if apkfilepath.find("ftp") == 0:
	# 	getfilefromftp(apkfilepath, user, password)
	# elif os.path.exists(apkfilepath):
	# 	return apkfilepath
	filename = os.path.basename(apkfilepath)
	filepath = os.path.join(DOWNLOAD_DIR, filename)
	logger.debug("filepath: " + filepath)
	return filepath

def getApkVersionCode(apkfilepath):
	aaptpath =os.path.join(os.path.abspath(os.path.dirname(__file__)), "aapt.exe")
	versioncode = ""
	cmd = aaptpath + " d badging" +" " + apkfilepath
	#print cmd
	ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
	cmdret = ret.stdout.read()
	#print cmdret
	packageInfo = cmdret.splitlines()[0]
	arraytemp = packageInfo.split(" ")
	for subitem in arraytemp:
		if subitem.find("versionCode") >= 0:
			versioncodeinfo = subitem
			versioncode = versioncodeinfo.split("=")[1].strip("'")
			break
	#print versioncode
	return versioncode

def md5_file(filepath):
	m = md5()
	a_file = open(filepath, 'rb')
	m.update(a_file.read())
	a_file.close()
	return m.hexdigest()

def gethostverfromfile(xmlfile):
	dom = xml.dom.minidom.parse(xmlfile)
	root = dom.documentElement
	#print root.nodeName
	#print root.nodeValue
	#print root.nodeType
	#print root.ELEMENT_NODE
	metadatas = root.getElementsByTagName("meta-data")
	#print metadatas[6]
	for metadata in metadatas:
		attr =  metadata.getAttribute("android:name")
		if attr =="hostCode":
			hostver = metadata.getAttribute("android:value")
			#print hostver
			logger.debug(hostver)
			logger.debug(hostver)
			return hostver
		#print (metadata.nodeName)
	return False

def getpluginverfromxmlfile(xmlfile):
	dom = xml.dom.minidom.parse(xmlfile)
	root = dom.documentElement
	#print root.nodeName
	#print root.nodeValue
	#print root.nodeType
	#print root.ELEMENT_NODE
	metadatas = root.getElementsByTagName("meta-data")
	#print metadatas[6]
	for metadata in metadatas:
		attr =  metadata.getAttribute("android:name")
		if attr =="pluginCode":
			pluginver = metadata.getAttribute("android:value")
			logger.debug(pluginver)
			pattern = re.compile('\d{14}')
			match = pattern.search(pluginver)
			if match:
				substr = match.group()
				logger.debug(substr)
				# print substr
				return substr
			else:
				return ""
	return False

def getpluginverfromsofile(sofile):
	# print "-" *10
	try:
		ret = decodeapkfile(sofile)
		if ret == False:
			logger.debug("decodeapkfile error...")
			# print "-" *10
			return False
		# basename = os.path.basename(apkfilepath)
		# releasepath = os.path.join(os.getcwd(), os.path.splitext(basename)[0])
		releasepath = os.path.join(ret, os.path.basename(sofile).split('.')[0])
		logger.debug(releasepath)
		androidmanifestxmlfile = os.path.join(releasepath, "AndroidManifest.xml")

		ap = axmlprinter.AXMLPrinter(open(androidmanifestxmlfile, 'rb').read())
		buff = minidom.parseString(ap.getBuff()).toxml()
		xmlfilename = os.path.basename(sofile).split('.')[0] + '.xml'
		logger.debug(xmlfilename)
		xmlfile = open(os.path.join(ret, xmlfilename), "w")
		xmlfile.write(buff)
		xmlfile.close()
		logger.debug(os.path.join(ret, xmlfilename))
		hostver = getpluginverfromxmlfile(os.path.join(ret, xmlfilename))
		logger.debug(hostver)
		shutil.rmtree(releasepath)
		return hostver
	except IOError,e:
		# print "-" *10
		logger.debug("getpackagehostver error...")
		logger.debug(e)
		traceback.print_exc()
		return False
	finally:
		# print "-" *10
		try:
			shutil.rmtree(releasepath)
			pass
		except:
			pass

def getpackagehostver(apkfilepath):
	try:
		ret = decodeapkfile(apkfilepath)
		if ret == False:
			logger.debug("decodeapkfile error...")
			return False
		# basename = os.path.basename(apkfilepath)
		# releasepath = os.path.join(os.getcwd(), os.path.splitext(basename)[0])
		releasepath = os.path.join(ret, os.path.basename(apkfilepath).split('.')[0])
		logger.debug(releasepath)
		androidmanifestxmlfile = os.path.join(releasepath, "AndroidManifest.xml")

		ap = axmlprinter.AXMLPrinter(open(androidmanifestxmlfile, 'rb').read())
		buff = minidom.parseString(ap.getBuff()).toxml()
		xmlfilename = os.path.basename(apkfilepath).split('.')[0] + '.xml'
		logger.debug(xmlfilename)
		xmlfile = open(os.path.join(ret, xmlfilename), "w")
		xmlfile.write(buff)
		xmlfile.close()
		logger.debug(os.path.join(ret, xmlfilename))
		hostver = gethostverfromfile(os.path.join(ret, xmlfilename))
		logger.debug(hostver)
		shutil.rmtree(releasepath)
		return hostver
	except IOError,e:
		logger.debug("getpackagehostver error...")
		logger.debug(e)
		traceback.print_exc()
		return False
	finally:
		try:
			shutil.rmtree(releasepath)
		except:
			pass

def decodeapkfile_byapktool(apkfilepath):
	try :
		apktoolpath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "apktool.jar")
		cmd = "java -jar " + apktoolpath + " d " + apkfilepath
		logger.debug(cmd)
		filename = os.path.basename(apkfilepath)
		releasepath = os.path.join(os.path.abspath(os.path.dirname(__file__)), filename.split(".")[0])
		logger.debug(releasepath)
		logger.debug(cmd)
		if os.path.isdir(releasepath):
			logger.debug("remove releasepath...")
			shutil.rmtree(releasepath)
		ret = subprocess.Popen(cmd, stdin = subprocess.PIPE, stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)
		ret.wait()
		logger.debug("go on...")
	except:
		logger.debug("decode apk file error...")
		return False
	return True

def decodeapkfile(apkfilepath):
	try :
		f = zipfile.ZipFile(apkfilepath)
		filename = os.path.basename(apkfilepath).split(".")[0]
		logger.debug(filename)
		temppath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "temp")
		logger.debug(temppath)
		f.extractall(os.path.join(temppath, filename))
		return temppath
	except:
		logger.debug("decode apk file error...")
		return False

def getmd5(filepath):
	md5ret = md5_file(filepath)
	logger.debug(md5ret)
	return md5ret

def getfilesize(filepath):
	filesize = os.path.getsize(filepath)
	return filesize

# def gethostver(pluginPath):
# 	return True

def getpluginver(pluginpath):
	# filename = os.path.basename(pluginpath)
	# pluginvertext = filename.split(r"_")
	# pluginver = pluginvertext[-2]
	# logger.debug(pluginver)
	pattern = re.compile('\d{14}')
	match = pattern.search(pluginpath)
	if match:
		substr = match.group()
		return substr
	else:
		return ""

#需鸡哥提供插件类型更改
def getplugintype(pluginpath):
	pattern = re.compile('cms*_plugin_[abcdefghijklmnopqrstuvwxyz]+')
	match = pattern.search(pluginpath)
	if match:
		substr = match.group()
		return substr.split('_')[2]
	else:
		return ""

	# filename = os.path.basename(pluginpath)
	# pluginvertext = filename.split(r"_")
	# plugintype = pluginvertext[-3]
	# logger.debug(plugintype)
	# return plugintype

def verifypackage(packagepath):
	ext = os.path.splitext(packagepath)[1]
	logger.debug(ext)
	if ext != ".apk":
		return False
	else:
		return True

def verifyplugin(pluginpath):
	ext = os.path.splitext(pluginpath)[1]
	logger.debug(ext)
	if ext != ".lzma":
		return False
	else:
		return True

def getsofilelist(apkfilepath):
	sofilelist = []
	f = zipfile.ZipFile(apkfilepath)
	extractpath = os.path.join(DOWNLOAD_DIR, os.path.basename(apkfilepath).split('.')[0])
	# print extractpath
	f.extractall(extractpath)
	for parent, dirnames, filenames in os.walk(extractpath):
		for file in filenames:
			fullfilepath = os.path.join(parent, file)
			ext = os.path.splitext(fullfilepath)
			if ext[1] == ".so" and os.path.basename(fullfilepath).find("plugin") == 0:
				# print fullfilepath
				sofilelist.append(fullfilepath)
	# print sofilelist
	return sofilelist

def getapkpluginfo(apkfilepath):
	pluginfo = "" + "\n"
	sofilelist = getsofilelist(apkfilepath)
	for i in sofilelist:
		ret = getpluginverfromsofile(i)
		pluginfo = pluginfo + str(os.path.basename(i).split('.')[0]) + "     " + str(ret) + "\n"
	return pluginfo

