from django.db import models

# Create your models here.
class empleado(models.Model):

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=100)
    nacimiento = models.CharField(max_length=50,blank=True)
    edad = models.CharField(max_length=50)
    dni = models.CharField(max_length=50)
    localidad = models.CharField(max_length=100)
    foto = models.ImageField(
        upload_to = 'foto/%Y/%m/%d',
        blank = True,
        verbose_name = ('Foto del empleado')
    )

class Meta:
    verbose_name = ('empleado')
    verbose_name_plural = ('empleados')

def __str__(self):
    return self.nombre