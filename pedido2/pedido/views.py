from ctypes.wintypes import MSG
from django.shortcuts import render
from django.http import HttpResponse
from .models import Almuerzo, Ensalada, Crema, Desayuno
# Create your views here.

def index(request):
    ctx = {'activate_link': 'index'}
    return render(request, 'index.html', ctx)

def pizza(request):
    ensaladas = Ensalada.objects.all()
    ctx = {'ensaladas': ensaladas, 'activate_link': 'ensaladas'}
    return render(request, 'ensalada.html', ctx)

def crema(request):
    cremas = Crema.objects.all()
    ctx = {'cremas': cremas, 'activate_link': 'cremas'}
    return render(request, 'cremas.html', ctx)

def desayuno(request):
    desayunos = Desayuno.objects.all()
    ctx = {'desayunos': desayunos, 'activate_link': 'desayunos'}
    return render(request, 'desayunos.html', ctx)

def almuerzo(request):
    almuerzos = Almuerzo.objects.all()
    ctx = {'almuerzos': almuerzos, 'activate_link': 'almuerzos'}
    return render(request, 'almuerzo.html', ctx)
