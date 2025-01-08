from django.http import HttpResponse
from django.template import loader

def miembros(request):
  template = loader.get_template('miprimer.html')
  return HttpResponse(template.render())