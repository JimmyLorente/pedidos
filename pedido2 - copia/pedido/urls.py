from django.urls import path

from . import views

app_name = 'pedido'

urlpatterns = [
    path('pizza', views.pizza, name='pizza' )
]