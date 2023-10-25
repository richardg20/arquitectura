from django.urls import path
from . import views
urlpatterns = [
    path('',views.cargarInicio),
    path('inicio',views.cargarInicio,name="cargarinicio"),
    path('descripcion',views.cargarDescripcion),
    path('catalogo',views.cargarCatalogo),
    path('editar',views.cargarEditar),
    path('carro',views.cargarCarro,name='cargarcarro'),
    path('agregar',views.cargarAgregarProducto),
    path('agregarProductoForm',views.agregarProducto),
    path('editarProducto/<sku>',views.cargarEditarProducto),
    path('editarProductoForm',views.editarProducto),
    path('eliminarProducto/<sku>',views.eliminarProducto),
    path('carrito',views.carrito),
    path('obtener-productos', views.obtener_productos, name='obtener_productos'),
    path('actualizar-stock',views.actualizar_stock),
    path('signup/', views.registrarse, name='signup'),
    path('logout/', views.log_out, name='logout'),
    path('signin/', views.loguearse, name='signin')
    
    
]