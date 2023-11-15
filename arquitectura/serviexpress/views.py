from django.shortcuts import render

from .models import Servicio


# Create your views here.

def index(request):
    context = {}
    return render(request, 'app/index.html')

def login(request):
    return render(request, 'app/login.html')

def reserva_hora(request):
    servicios = Servicio.objects.all()

    data = {
        'servicios': servicios
    }
    return render(request, 'app/reserva-hora.html', data)

def registro(request):
    return render(request, 'registration/registro.html')

