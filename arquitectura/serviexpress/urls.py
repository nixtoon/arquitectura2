from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('reserva-hora/', views.reserva_hora, name='reserva-hora')
]