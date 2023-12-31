from django.urls import path
from AppChuleleche import views


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

]

urlpatterns += [
    path('proveedores/list2', views.ProveedorListView2.as_view(), name="ProveedorList2"),
    path('proveedores/list', views.ProveedorListView.as_view(), name="ProveedorList"),
    path('proveedor/<int:pk>/', views.ProveedorDetalle.as_view(), name='ProveedorDetalle'),

]
