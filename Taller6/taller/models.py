from django.db import models

# Create your models here.
class Tipodocumento(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el nombre")
    descripcion = models.TextField(blank=True, help_text="Ingrese una descripcion")
    def __str__(self):
        return "Documento " + self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=100, help_text="Ingrese el nombre")
    descripcion = models.TextField(blank=True, help_text="Ingrese una descripcion")
    def __str__(self):
        return "Ciudad " + self.nombre

class Persona(models.Model):
    nombres = models.CharField(max_length=100, help_text="Ingrese el nombre")
    apellidos = models.TextField(blank=True, help_text="Ingrese una descripcion")
    idtipodocumento = models.ForeignKey(Tipodocumento, on_delete=models.CASCADE)
    documento = models.IntegerField()
    lugarresidencia = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    fechanacimiento = models.DateField(blank=True)
    email = models.EmailField(blank=True)
    telefono = models.IntegerField()
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    def __str__(self):
        return "Persona " + self.nombres