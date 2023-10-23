from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=60)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(max_length=40, null=True, blank=True)
    web = models.URLField(max_length=40, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)
    hacen_envios = models.BooleanField(default=False)
    logo = models.ImageField(null=True, blank=True, upload_to="proveedores", default="proveedores/default_logo2.png")


    def __str__(self):
        return f"{self.nombre}"

class Cliente(models.Model):
    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40, null=True, blank=True)
    telefono = models.CharField(max_length=20, null=True, blank=True)
    correo = models.EmailField(max_length=40, null=True, blank=True)
    descripcion = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pedido(models.Model):
    numero = models.IntegerField()
    valor = models.FloatField()
    fecha = models.DateField()
    proveedor = models.ForeignKey(Proveedor, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"Pedido nro {self.numero}"

class Venta(models.Model):
    numero = models.IntegerField()
    valor = models.FloatField()
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)

    
    def __str__(self):
        return f"Venta nro {self.numero}"
