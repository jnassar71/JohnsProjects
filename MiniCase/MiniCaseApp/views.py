from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import View, TemplateView,ListView,DetailView
from . import models

def index(request):
    return render(request,'MiniCaseApp/index.html')
    #return HttpResponse("You are at the main page")
