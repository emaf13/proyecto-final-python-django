from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=40)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=40)
    hacen_envios = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.nombre}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=20)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField(max_length=40)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    numero = models.IntegerField()
    valor = models.FloatField()
    fecha = models.DateField()

    def __str__(self):
        return f"Pedido nro {self.numero}"

class Venta(models.Model):
    numero = models.IntegerField()
    valor = models.FloatField()
    fecha = models.DateField()
    
    def __str__(self):
        return f"Venta nro {self.numero}"
