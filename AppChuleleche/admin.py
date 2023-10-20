from django.contrib import admin
from AppChuleleche.models import Proveedor, Cliente, Pedido, Venta

# Register your models here.

admin.site.register(Proveedor)
admin.site.register(Cliente)
admin.site.register(Venta)
admin.site.register(Pedido)
