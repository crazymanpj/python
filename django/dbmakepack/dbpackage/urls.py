from django.contrib import admin
# from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    url('^makepackage', views.makepackage),
    url('^getproductlist', views.getproductlist),
    url('^gettrynolist', views.gettrynolist),
    url('^getallmakepacketinfo', views.getallmakepacketinfo),
    url('^getresultbytaskid', views.getresultbytaskid),
    url('^stopmakepackage', views.stopmakepackage),
    url('^getpartnerlist', views.getpartnerlist),
    url('^testupdatesvn', views.test_updatesvn),
    url('^test_method', views.test_method),
    url('^addparner', views.addpartner),
    url('^getinstallxml', views.getinstallxml),
    url('^getpacketxml', views.getpacketxml),
    url('^getlastpackageinfobyitemname', views.getlastpackageinfobyitemname),
    url('^getautotidtod', views.getautotidtod),
]
