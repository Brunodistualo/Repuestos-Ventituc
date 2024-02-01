from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=42)
    description = models.TextField(default='Descripción predeterminada')
    imagenes = models.ImageField(upload_to='images/')    
    
    def __str__(self) -> str:
        return self.name + ' _ ' + self.description
    
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(default='Descripción predeterminada')
    imagenes = models.ImageField(upload_to='task_imagenes/')
    modelo_vt = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.title + ' - ' + self.description

class Ventiladores(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='ventiladores/')
    
    def __str__(self) -> str:
        return self.nombre + ' _ ' + self.descripcion
    
