from django.shortcuts import render
from django.http import HttpResponse

def index(request):
  if request.method == 'GET':
    return HttpResponse('Hi Py GET')
  if request.method == 'POST':
    return HttpResponse('Hi Py POST')