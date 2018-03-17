#encoding=utf-8
# Date:    2018-02-01
# Author:  pangjian
# version: 1.0
from dbpackage import db

class ProductList(db.Model):
    __tablename__ = 'db_productlist'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(50), unique=False, nullable=True)
    addtime = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Integer)

    def __init__(self, name, description, addtime, status):
        self.name = name
        self.description = description
        self.addtime = addtime
        self.status = status

    def __repr__(self):
        return '<product %r>' % self.description

class TrynoList(db.Model):
    __tablename__ = 'db_trynolist'
    id = db.Column(db.Integer, primary_key=True)
    tryno = db.Column(db.String(20), unique=True, nullable=False)
    description = db.Column(db.String(50), unique=False, nullable=True)
    addtime = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Integer)


    def __init__(self, tryno, description, addtime, status):
        self.tryno = tryno
        self.description = description
        self.addtime = addtime
        self.status = status

    def __repr__(self):
        return '<product %r>' % self.tryno

class PackageInfo(db.Model):
    __tablename__ = 'db_packageinfo'
    taskid = db.Column(db.Integer, primary_key=True)
    makepackagetime = db.Column(db.DateTime, nullable=True)
    tryno = db.Column(db.String(20))
    product = db.Column(db.String(20))
    isnewitem = db.Column(db.Integer)
    itemname = db.Column(db.String(20))
    packagetype = db.Column(db.String(20))
    packagemodel = db.Column(db.String(10))
    tid1 = db.Column(db.String(10))
    tid2 = db.Column(db.String(10))
    tod1 = db.Column(db.String(10))
    tod2 = db.Column(db.String(10))
    fixuplive = db.Column(db.Integer)
    islokmp = db.Column(db.Integer)
    specialfile = db.Column(db.Integer)
    localname = db.Column(db.String(20))
    user = db.Column(db.String(50), nullable=False)
    islokmp = db.Column(db.Integer)
    result = db.Column(db.Integer)

    def __init__(self, m_time, product, isnewitem,itemname,tryno,packettype,packetmodel,tid1,tid2,tod1,tod2,fixuplive,islokmp,specialfile,localname):
        self.product = product
        self.isnewitem = isnewitem
        self.itemname = itemname
        self.tryno = tryno
        self.packagetype = packettype
        self.packagemodel = packetmodel
        self.tid1 = tid1
        self.tid2 = tid2
        self.tod1 = tod1
        self.tod2 = tod2
        self.fixuplive = fixuplive
        self.islokmp = islokmp
        self.specialfile = specialfile
        self.localname = localname
        self.makepackagetime = m_time
        self.user = ''
        self.result = 0

class PackageRet(db.Model):
    __tablename__ = 'db_packageret'
    id = db.Column(db.Integer, primary_key=True)
    taskid = db.Column(db.Integer)
    localpath = db.Column(db.String(200))

class ParnerList(db.Model):
    __tablename__ = 'db_partnerlist'
    id = db.Column(db.Integer, primary_key=True)
    partner = db.Column(db.String(50))
    description = db.Column(db.String(50))
    addtime = db.Column(db.DateTime)
    status = db.Column(db.Integer)
