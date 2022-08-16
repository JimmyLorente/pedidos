from dataclasses import field
import email
from pyexpat import model
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from .models import Formulario

class NewUserForm(UserCreationForm):
    email = forms.EmailField(max_length=100, required=True, help_text='Informar si tu correo es valido')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class FormularioOpinion(ModelForm):
    class Meta:
        model = Formulario
        fields = "__all__"