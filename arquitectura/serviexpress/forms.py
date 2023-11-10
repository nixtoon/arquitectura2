from django import forms
from .models import Servicio
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm

class ServicioForm(ModelForm):
    class Meta:
        model = Servicio
        fields = "__all__"

class CustomUserForm(UserCreationForm):
    pass
