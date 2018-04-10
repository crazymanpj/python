from __future__ import unicode_literals

from django.db import models

# Create your models here.

class PublishRecord(models.Model):
	id = models.IntegerField(primary_key=True)
	publishtime = models.DateTimeField()
	filetype = models.CharField(max_length=20)
	channel = models.CharField(max_length=100)
	details = models.CharField(max_length=2000)
	filepath = models.CharField(max_length=1000)
	opuser = models.CharField(max_length=50, null=True)
	hostver = models.CharField(max_length=20)

class Plugin(models.Model):
	id = models.IntegerField(primary_key=True)
	publishid = models.IntegerField()
	pluginver = models.CharField(max_length=20)
	hostver = models.CharField(max_length=20)
	pluginmd5 = models.CharField(max_length=40)
	plugintype = models.CharField(max_length=20)
	pluginsize = models.CharField(max_length=20)
	channel = models.CharField(max_length=20)
	publishtime = models.DateTimeField()

class Package(models.Model):
	id = models.IntegerField(primary_key=True)
	apkver = models.CharField(max_length=20)
	packagepath = models.CharField(max_length=200)
	hostver = models.CharField(max_length=20)
	packagemd5 = models.CharField(max_length=40)
	packagesize = models.CharField(max_length=20)
	channel = models.CharField(max_length=20)
	publishtime = models.DateTimeField()
	iid_code = models.CharField(max_length=500)
	flag = models.CharField(max_length=20)
	remarks = models.CharField(max_length=200)
	issync = models.IntegerField(default=0)
	opuser = models.CharField(max_length=50)

class SideBarGroup(models.Model):
	id = models.IntegerField(primary_key=True)
	group = models.CharField(max_length=50)
	blank = models.CharField(max_length=20)
	status = models.IntegerField()

class SideBar(models.Model):
	id = models.IntegerField(primary_key=True)
	group = models.ForeignKey(SideBarGroup)
	name = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	blank = models.CharField(max_length=20)
	status = models.IntegerField()

class Procduct(models.Model):
	id = models.IntegerField(primary_key=True)
	procductname = models.CharField(max_length=20)
	description = models.CharField(max_length=50)

class FileType(models.Model):
	id = models.IntegerField(primary_key=True)
	type = models.CharField(max_length=20)
	description = models.CharField(max_length=50)

class Channel(models.Model):
	id = models.IntegerField(primary_key=True)
	channelnum = models.IntegerField(unique=True)
	description = models.CharField(max_length=50)
	addtime = models.DateTimeField(null=True)
	status = models.IntegerField()
	opuser = models.CharField(max_length=50)

	def get_channelnum_bydesc(self):
		return self.channelnum

class PluginType(models.Model):
	id = models.IntegerField(primary_key=True)
	name = models.CharField(max_length=20)
	description = models.CharField(max_length=50)
	addtime = models.DateTimeField(null=True)

class HostVer(models.Model):
	id = models.IntegerField(primary_key=True)
	hostver = models.CharField(max_length=20)
	addtime = models.DateTimeField(null=True)
	status = models.IntegerField()

class ApkVer(models.Model):
	id = models.IntegerField(primary_key=True)
	apkver = models.CharField(max_length=20)
	addtime = models.DateTimeField(null=True)
	status = models.IntegerField()

class PluginVer(models.Model):
	id = models.IntegerField(primary_key=True)
	pluginver = models.CharField(max_length=20)
	addtime = models.DateTimeField(null=True)
	status = models.IntegerField()

class IIDcode(models.Model):
	id = models.IntegerField(primary_key=True)
	iidcode = models.CharField(max_length=20)
	addtime = models.DateTimeField(null=True)
	status = models.IntegerField()