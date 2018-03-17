#encoding=utf-8
# Date:    2018-02-01
# Author:  pangjian
# version: 1.0
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

ins_dbpackage = Flask(__name__)
ins_dbpackage.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:kingsoft@localhost/dbmakepack'
ins_dbpackage.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
ins_dbpackage.config['PROJECT_PATH'] = r'd:\kuaipan\python\Flask\dbmakepack'
db = SQLAlchemy(ins_dbpackage)

import dbpackage.views
