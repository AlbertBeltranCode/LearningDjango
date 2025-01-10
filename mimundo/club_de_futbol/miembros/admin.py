from django.contrib import admin
from .models import Miembro

# Register your models here.
class MiembroAdmin(admin.ModelAdmin):
  list_display = ("Nombre", "Apellido", "fecha_registro",)
  
admin.site.register(Miembro, MiembroAdmin)