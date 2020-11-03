from django.urls import path
from .views import *
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

urlpatterns = [
    ##-----------------pagina principal---------------------------------
    path('', home, name = "home"), 
    path('registro', registrar, name = "registrar"),
    path('tienda', tienda, name = "show_tienda"),
    ##-----------------pagina productor---------------------------------
    path('registrarproductor', registrar_productor, name = "reg_prod"),
    path('formularioproduc', registrar_prod, name="reg_productor"),
    path('perfilproductor',perfilproductor , name="perfil_productor"),
    ##----------------página productos-----------------------------------
    path('productos', productos, name="productos"),  #Muestra el  listar de los productos
    path('productosclienteex', productoex, name="productosclienteex"),
    path('registrarproducto', registrar_producto, name="registrarproducto"),#Redirige a la pantalla de registrar Producto
    path('eliminarproducto/<id>/', eliminar_producto, name="eliminarproducto"), #Redirige a la pantalla de Modificar Producto
    path('modificar-producto/<id>/', modificarproducto, name="modificarproducto"), #Redirige a formulario para  modificar 
    ##-----------------pagina transportista---------------------------------
    path('registrartransportista',registrar_transportista, name="reg_trans"),
    path('formulariotrans', registrar_trans, name="reg_transportista"),

    ##-----------------pagina cliente interno---------------------------------
    path('registrarclienteinterno',registrar_cliente_interno, name="reg_clienteinterno"),
    path('formularioclienteinterno', registrar_cliente_in, name="reg_clientein"),

    ##-----------------pagina cliente externo---------------------------------
    path('registrarclienteexterno', registrar_cliente_externo, name = "reg_clienteexterno"), 
    path('formularioclientexterno', registrar_cliente_ex, name="reg_clienteex"),
   
       ##-----------------pagina de solicitud venta-------------------------------
    path('listado_solicitud_venta', listado_solicitud_venta, name = "listado_solicitud_venta"),    
    path('registrarsolicitud', registrar_solicitud, name = "registrarsolicitud"),
    ##-----------------pagina de subasta---------------------------------------
    path('modificar_subasta/<id>/', modificar_subasta, name= "modificar_subasta"),
    path('eliminar_subasta/<id>/', eliminar_subasta, name="eliminar_subasta"),
    path('listado_subasta', listado_subasta, name= "listado_subasta"),
        path('registrar_subasta', registrar_subasta, name="registrar_subasta"),


    ##-----------------pagina de proceso de venta-------------------------------
    path('listado_proceso_venta', listado_proceso_venta, name="listado_proceso_venta"),
    path('registrar_proceso_venta', registrar_proceso_venta, name="registrar_proceso_venta"),
    path('eliminar_proceso_venta/<id>/', eliminar_proceso_venta, name="eliminar_proceso_venta"),
]
    ##--------------------------pagina tienda---------------------------------
