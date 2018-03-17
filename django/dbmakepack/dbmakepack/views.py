from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import HttpResponseRedirect

# from dbpackage.task import add


def index(request):
    return HttpResponseRedirect('/dbmakepack')
