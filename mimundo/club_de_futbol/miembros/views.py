from django.http import HttpResponse
from django.template import loader
from .models import Miembro

#Creamos una vista que nos devuelva todos los miembros
def miembros(request):
  mismiembros = Miembro.objects.all().values()
  template = loader.get_template('todos_los_miembros.html')
  context = {
    'mismiembros': mismiembros,
  }
  return HttpResponse(template.render(context, request))

#Creamos una vista que nos devuelva los detalles de un miembro
def detalles(request, id):
  mimiembro = Miembro.objects.get(id=id)
  template = loader.get_template('detalles.html')
  context = {
    'mimiembro': mimiembro,
  }
  return HttpResponse(template.render(context, request))

#Creamos una vista que nos devuelva la pagina principal
def principal(request):
  template = loader.get_template('principal.html')
  return HttpResponse(template.render())

#Creamos una vista para los test
def testing(request):
  template = loader.get_template('template.html')
  context = {
    'frutas': ['Manzana', 'Banana', 'Cereza'],   
  }
  return HttpResponse(template.render(context, request))