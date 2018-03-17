from django.db import models

# Create your models here.


class DBpackageinfo(models.Model):
    taskid = models.IntegerField(primary_key=True)
    makepackagetime = models.DateTimeField()
    product = models.CharField(max_length=20)
    isnewitem = models.IntegerField()
    itemname = models.CharField(max_length=20)
    tryno = models.CharField(max_length=20)
    packagetype = models.CharField(max_length=20)
    packagemodel = models.CharField(max_length=10)
    tid1 = models.IntegerField()
    tid2 = models.IntegerField()
    tod1 = models.IntegerField()
    tod2 = models.IntegerField()
    fixuplive = models.IntegerField()
    islokmp = models.IntegerField()
    specialfile = models.CharField(max_length=50)
    localname = models.CharField(max_length=256)
    user = models.CharField(max_length=50)
    result = models.IntegerField()

    class Meta:
        db_table = 'db_packageinfo'


class DBpackageret(models.Model):
    id = models.IntegerField(primary_key=True)
    taskid = models.IntegerField()
    localpath = models.CharField(max_length=200)

    class Meta:
        db_table = 'db_packageret'


class DBproductlist(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=50)
    addtime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = 'db_productlist'


class DBtrynolist(models.Model):
    id = models.IntegerField(primary_key=True)
    tryno = models.IntegerField()
    description = models.CharField(max_length=50)
    addtime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = 'db_trynolist'

class DBPartnerlist(models.Model):
    id = models.IntegerField(primary_key=True)
    partner = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    addtime = models.DateTimeField()
    status = models.IntegerField()

    class Meta:
        db_table = 'db_partnerlist'
