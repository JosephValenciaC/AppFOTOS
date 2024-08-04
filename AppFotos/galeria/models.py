from django.db import models

class Tarea(models.Model):
    nombre = models.CharField(max_length=255)

class Nota(models.Model):
    tarea = models.ForeignKey(Tarea, related_name='notas', on_delete=models.CASCADE)
    contenido = models.TextField()

class Foto(models.Model):
    nota = models.ForeignKey(Nota, related_name='fotos', on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='media/')
