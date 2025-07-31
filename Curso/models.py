from django.db import models

# Create your models here.

class Trading(models.Model):
    id_car=models.AutoField(primary_key=True)   
    nombre_car= models.CharField(max_length=100)
    fecha_creacion_car = models.DateField()

    def __str__(self):
        return self.nombre_car