from unicodedata import name
from django.urls import path

from . import views

app_name = 'pedido'

urlpatterns = [
    path('pizza', views.pizza, name='pizza' ),
    path('crema', views.crema, name='crema' ),
    path('desayuno', views.desayuno, name='desayuno' ),
    path('almuerzo', views.almuerzo, name='almuerzo' ),
    path('orden', views.orden, name='orden' ),
    path('signup', views.signup, name='signup' ),
    path('login', views.logIn, name='login' ),
    path('logout', views.logOut, name='logout' ),
    path('recetas', views.recetas, name='recetas'),
    path('receta1', views.receta1, name='receta1'),
    path('receta2', views.receta2, name='receta2'),
    path('receta3', views.receta3, name='receta3'),
    path('receta4', views.receta4, name='receta4'),
    path('receta5', views.receta5, name='receta5'),
    path('receta6', views.receta6, name='receta6'),
    path('receta7', views.receta7, name='receta7'),
    path('receta8', views.receta8, name='receta8'),
    path('form', views.form, name='form'),
    path('preguntas', views.preguntas, name='preguntas'),
    path('pagos', views.pagos, name='pagos'),
    path('realizado', views.realizado, name='realizado')
    # path('tu', views.index , name='tu')
    # path('', views.list_tasks, name='list_' ),
    # path('new', views.create_tasks, name='preguntas'),
    # path('delete_task/<int:task_id>/', views.delete_task, name='delete_task'),

]