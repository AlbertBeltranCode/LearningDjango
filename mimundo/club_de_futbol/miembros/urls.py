from django.urls import path
from . import views

urlpatterns = [
    path('', views.principal, name='principal'),
    path('miembros/', views.miembros, name='miembros'),
    path('miembros/detalles/<int:id>', views.detalles, name='detalles'),
    path('testing/', views.testing, name='testing'), 
]