from multiprocessing import context
from re import template
from unittest import loader
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Almuerzo, Ensalada, Crema, Desayuno, Task, Receta, Formulario
from .forms import NewUserForm, FormularioOpinion
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

def recetas(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'recetas.html', ctx)

def receta1(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta1.html', ctx)

def receta2(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta2.html', ctx)

def receta3(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta3.html', ctx)

def receta4(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta4.html', ctx)

def receta5(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta5.html', ctx)

def receta6(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta6.html', ctx)

def receta7(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta7.html', ctx)

def receta8(request):
    ctx = {'activate_link': 'recetas'}
    return render(request, 'Recetaaas/receta8.html', ctx)

def preguntas(request):
    ctx = {'activate_link': 'preguntas'}
    return render(request, 'preguntas.html', ctx)

def pagos(request):
    ctx = {'activate_link':'pagos'}
    return render(request, 'pagos.html',ctx)

def realizado(request):
    ctx = {'activate_link': 'realizado'}
    return render(request, 'realizado.html', ctx)

# Aqui la view de inicar secion
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
    

# Aqui el view del request

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

# Formulario de opinion 
def form(request):
    submitted = False
    if request.method == "POST":
        formi = FormularioOpinion(request.POST)
        if formi.is_valid():
            formi.save()
            return redirect('index')
    else:
        formi = FormularioOpinion
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'form.html', {'form':formi, 'submitted':submitted})

# Aqui las view de las preguntas 
# def list_tasks(request):
#     tasks = Task.objects.all()
#     return render(request, 'list_tasks.html', {"tasks": tasks })

# def create_tasks(request):
#    task = Task(title=request.POST['Nombre de la mascota'])
#    task.save()
#    return redirect('/Preguntas/')

# def delete_task(request, task_id):
#     task = Task.objects.get(id=task_id)
#     task.delete()
#     return redirect('/Preguntas/')


# def index(request):
#     template = loader.get_template('tu.html')
#     context = {}
#     return HttpResponse(template.render(context, request))

