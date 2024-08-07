import os


import sys

#sys.path.insert(0,'D:/python_env/env_django18/Lib/site-packages')
sys.path.append('d:/kuaipan/python/mobiledata')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mobiledata.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()