from ctypes.wintypes import MSG
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    ctx = {'name': 'Jungle', 'msg':'Django project'}
    return render(request, 'index.html', ctx)

def pizza(request):
    return render(request, 'ensalada.html')