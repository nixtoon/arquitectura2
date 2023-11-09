from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('reserva-hora/', views.reserva_hora, name='reserva-hora'),
    path('login/', views.login, name='login'),
]