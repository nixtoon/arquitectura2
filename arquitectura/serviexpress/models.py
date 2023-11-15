from django.db import models

# Create your models here.

class Servicio(models.Model):
  nombre_servicio = models.CharField(max_length=50)
  precio_servicio = models.IntegerField()
  descripcion = models.TextField()

  def __str__(self):
    return self.nombre_servicio
  
class Cliente(models.Model):
  nombre_cliente = models.CharField(max_length=50)
  apellido_cliente = models.CharField(max_length=50)
  direccion_cliente = models.CharField(max_length=60)
  telefono_cliente = models.CharField(max_length=12)
  correo_cliente = models.CharField(max_length=70)
  nombre_usuario = models.CharField(max_length=50)
  password = models.CharField(max_length=20)

  def __str__(self):
    return self.nombre_cliente
  
class Facturacion(models.Model):
  nombre_facturacion = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre_facturacion
  
class Reserva_hora(models.Model):
  fecha = models.DateField()
  hora = models.DateTimeField()
  cliente = models.ForeignKey(Cliente, on_delete=models.PROTECT)
  servicio = models.ForeignKey(Servicio, on_delete=models.PROTECT)
  Facturacion = models.ForeignKey(Facturacion, on_delete=models.PROTECT)

  def __str__(self):
    return self.id
  
class Empleado(models.Model):
  nombre_empleado = models.CharField(max_length=50)
  apellido_empleado = models.CharField(max_length=50)
  direccion_empleado = models.CharField(max_length=60)
  telefono_empleado = models.CharField(max_length=12)
  correo_empleado = models.CharField(max_length=70)
  nombre_usuario = models.CharField(max_length=50)
  password = models.CharField(max_length=20)

  def __str__(self):
    return self.nombre_empleado
  
class Rubro_proveedor(models.Model):
  nombre_rubro = models.CharField(max_length=50)

  def __str__(self):
    return self.nombre_rubro
  
class Proveedor(models.Model):
  nombre_proveedor = models.CharField(max_length=50)
  direccion_proveedor = models.CharField(max_length=70)
  telefono_proveedor = models.CharField(max_length=12)
  correo_proveedor = models.CharField(max_length=70)
  rubro = models.ForeignKey(Rubro_proveedor, on_delete=models.PROTECT)

  def __str__(self):
    return self.nombre_proveedor
  
class Orden_Pedido(models.Model):
  producto = models.CharField(max_length=50)
  cantidad = models.IntegerField()
  proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)

  def __str__(self):
    return self.id
  
class Recepcion_pedido(models.Model):
  orden_pedido = models.ForeignKey(Orden_Pedido, on_delete=models.PROTECT)
  proveedor = models.ForeignKey(Proveedor, on_delete=models.PROTECT)
  estado = models.BooleanField()

  def __str__(self):
    return self.id

class Informe(models.Model):
  nombre_informe = models.CharField(max_length=20)
  fecha_informe = models.DateField()

  def __str__(self):
    return self.nombre_informe

