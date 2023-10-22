from django.urls import path
from AppChuleleche import views

from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', views.inicio, name="Raiz"),
    path('proveedores/', views.proveedores, name="Proveedores"),
    path('pedidos/', views.pedidos, name="Pedidos"),
    path('clientes/', views.clientes, name="Clientes"),
    path('ventas/', views.ventas, name="Ventas"),
    path('proveedores-alta/', views.alta_proveedores, name="ProveedoresAlta"),
    path('proveedores-buscar/', views.buscar_proveedores, name="ProveedoresBuscar"),
    path('clientes-alta/', views.alta_clientes, name="ClientesAlta"),
    path('clientes-buscar/', views.buscar_clientes, name="ClientesBuscar"),
    path('pedidos-alta/', views.alta_pedidos, name="PedidosAlta"),
    path('pedidos-buscar/', views.buscar_pedidos, name="PedidosBuscar"),
    path('ventas-alta/', views.alta_ventas, name="VentasAlta"),
    path('ventas-buscar/', views.buscar_ventas, name="VentasBuscar"),
    path('login/', views.login_request, name="Login"),
    path('registro/', views.register, name='Register'),
    path('logout/', LogoutView.as_view(template_name='AppChuleleche/index.html'), name='Logout'),
    path('edit/', views.editProfile, name='Edit'),

]

urlpatterns += [
    path('proveedores/list', views.ProveedorListView.as_view(), name="ProveedorList"),
    #path('proveedores/list', views.ProveedorListView.as_view(), name="ProveedorList"),

]
