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

]