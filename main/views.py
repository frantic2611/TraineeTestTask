from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

import cgi, cgitb
from django import forms
def index(request):

    return render(request, 'main/home.html')
# Create your views here.
def greeting(request):
    name = request.GET.get('name')
    message = request.GET.get('message')
    return render(request, 'main/greeting.html', {'name':name, 'message':message})
