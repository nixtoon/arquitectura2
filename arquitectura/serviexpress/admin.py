from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Servicio)
admin.site.register(Cliente)
admin.site.register(Empleado)
admin.site.register(Facturacion)
admin.site.register(Reserva_hora)
admin.site.register(Rubro_proveedor)
admin.site.register(Proveedor)
admin.site.register(Orden_Pedido)
admin.site.register(Recepcion_pedido)
admin.site.register(Informe)