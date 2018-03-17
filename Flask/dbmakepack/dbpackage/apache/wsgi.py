import os


import sys

sys.path.insert(0,'D:/kuaipan/python/Flask/dbmakepack')

from dbpackage import ins_dbpackage
application = ins_dbpackage
# application = get_wsgi_application()
