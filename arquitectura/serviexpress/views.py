from django.shortcuts import render


# Create your views here.

def login(request):
    return render(request, 'app/login.html')

def reserva_hora(request):
    context = {}
    return render(request, 'app/reserva-hora.html')