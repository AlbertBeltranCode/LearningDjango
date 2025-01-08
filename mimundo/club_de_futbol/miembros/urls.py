from django.urls import path
from . import views

urlpatterns = [
    path('miembros/', views.miembros, name='miembros'),
]