from django.db import models

class Miembro(models.Model):
  Nombre = models.CharField(max_length=255)
  Apellido = models.CharField(max_length=255)
  telefono = models.IntegerField(null=True)
  fecha_registro = models.DateField(null=True)