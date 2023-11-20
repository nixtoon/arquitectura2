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

def homeAdmin(request):
    return render(request, 'app/homeadmin.html')

def registro_cliente(request):
    return render(request, 'registration/registro-cliente.html')
    
def registro_proveedor(request):
    return render(request, 'registration/registro-proveedor.html')

def registro_empleado(request):
    return render(request, 'registration/registro-empleado.html')

def recepcion_producto(request):
    return render(request, 'registration/recepcion-producto.html')

def boleta_factura(request):
    return render(request, 'registration/boleta-factura.html')