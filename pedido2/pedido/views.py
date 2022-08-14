from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Almuerzo, Ensalada, Crema, Desayuno
from .forms import NewUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
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

def orden(request):
    ctx = {'activate_link': 'orden'}
    return render(request, 'orden.html', ctx)

def signup(request):
    ctx = {}
    if request.POST:
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            ctx['form'] = form
    else:
        form = NewUserForm()
        ctx['form'] = form
    return render(request, 'signup.html', ctx)

def logIn(request):
    if request.POST:
        username = request.POST.get('username')
        pwd= request.POST.get('password')
        user= authenticate(request, usarname=username, password=pwd)
        if user is not None:
            logIn(request, user)
            return redirect('index')
        else:
            messages.info(request, 'usario o contraseña incorrectos')
    ctx = {'activate_link': 'logIn'}
    return render(request, 'login.html', ctx)

def logOut(request):
    logout(request)
    return redirect('index')
