from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.template import RequestContext
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Group
from django.db import connection
import cx_Oracle
from datetime import datetime


#########################################################################
#                  Template----->View-------->URL                       #
#########################################################################
# ---------------------------------CORE-----------------------------------
def home(request):  # Para navegacion de home
    return render(request, 'core/home.html')


def login(request):  # Para navegacion de home
    return render(request, 'registration/login.html')


def registrar(request):
    return render(request, 'core/seleccionarusuario.html')
#====================================================================================================================#
#----------------------------------CRUD productor--------------------------------------------------------------------#
#====================================================================================================================#

# Registrar Productor Pagina 1 por django
#------------------------------#

def registrar_productor(request):
    data = {
        'form': DjangoUserForm()
    }
    if request.method == 'POST':
        formulario = DjangoUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            username = formulario.cleaned_data.get('username')
            group = Group.objects.get(name="Productor")
            user.groups.add(group)

        return redirect(to='reg_productor')
    return render(request, 'formularios/formularioproduc.html', data)

# Registrar Productor Pagina 2 para la base de datos
#----------------------------------------#

def registrar_prod(request):
    data = {
        'form': ProductorRegisterForm()
    }
    if request.method == 'POST':
        salida = ProductorRegisterForm(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='login')
    return render(request, 'formularios/formularioproduc.html', data)

# conexion con el PACK_MANT_PRODUCTOR de la base de datos
#---------------------------------------------------------#

def agregar_productor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("PACK_MANT_PRODUCTOR.SP_AGREGAR_PRODUCTOR",
                    [rut_produc, nom_produc, apellidop_produc, apellidom_produc, direccion_produc, ciudad_produc, telefono_produc, correo_produc, pass_produc, rol_id_rol,
                     salida])
    return salida.getvalue()


# PERFIL PRODUCTOR
#---------------------------------------------------------#
def listar_productor():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('PACK_MANT_PRODUCTOR.SP_LEER_PRODUCTOR', [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

def perfilproductor(request):
    data = {
        'productor':listar_productor()
    }

    if request.method == 'POST':
        RUT_PRODUC = request.POST.get('RUT_PRODUC')
        NOM_PRODUC = request.POST.get('NOM_PRODUC')
        APELLIDOP_PRODUC = request.POST.get('APELLIDOP_PRODUC')
        APELLIDOM_PRODUC = request.POST.get('APELLIDOM_PRODUC')
        DIRECCION_PRODUC = request.POST.get('DIRECCION_PRODUC')
        CIUDAD_PRODUC = request.POST.get('CIUDAD_PRODUC')
        TELEFONO_PRODUC = request.POST.get('TELEFONO_PRODUC')
        CORREO_PRODUC = request.POST.get('CORREO_PRODUC')
        PASS_PRODUC = request.POST.get('PASS_PRODUC')
        data['productor'] = listar_productor()
    
    return render (request, 'perfil/perfilproductor.html', data)

def perfil_productor(request):
    productor = Productor.objects.get()
    return render(request, 'perfil/perfilproductor.html', {"productor":productor})







# mODIFICAR PRODUCTOR
#---------------------------------------------------------#






#====================================================================================================================#
# ---------------------------------CRUD Transportista----------------------------------------------------------------#
#====================================================================================================================#

# Registrar Transportista Pagina 1
#-----------------------------------#
def registrar_transportista(request):
    data = {
        'form': DjangoUserForm()
    }
    if request.method == 'POST':
        formulario = DjangoUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            username = formulario.cleaned_data.get('username')
            group = Group.objects.get(name="Transportista")
            user.groups.add(group)

        return redirect(to='reg_transportista')
    return render(request, 'formularios/formulariotrans.html', data)

# Registrar Transportista Pagina 2 (ejemplo)
#--------------------------------------------#

def registrar_trans(request):
    data = {
        'form': TransportistaRegisterFrom()
    }
    if request.method == 'POST':
        salida = TransportistaRegisterFrom(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='login')
    return render(request, 'formularios/formulariotrans.html', data)

# conexion con el PACK_MANT_TRANSPORTISTA de la base de datos
#-------------------------------------------------------------#

def agregar_transportista():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("PACK_MANT_TRANSPORTISTA.SP_AGREGAR_TRANSPORTISTA",
                    [RUT_TRANSP, NOMBRE_TRANSP, APELLIDOP_TRANSP, APELLIDOM_TRANSP, direccion_produc, ciudad_produc, PATENTE_VEHICULO,
                     CAPACIDAD_CARGA, REFRIGERACION, PASS_TRANSP, ROL_ID_ROL, salida])
    return salida.getvalue()


#====================================================================================================================#
#--------------------------------CRUD de Cliente Interno-------------------------------------------------------------#
#====================================================================================================================#

# Registrar Cliente Interno Pagina 1
#------------------------------------#

def registrar_cliente_interno(request):
    data = {
        'form': DjangoUserForm()
    }
    if request.method == 'POST':
        formulario = DjangoUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            username = formulario.cleaned_data.get('username')
            group = Group.objects.get(name="ClienteInterno")
            user.groups.add(group)

        return redirect(to='reg_clientein')
    return render(request, 'formularios/formularioclienteinterno.html', data)


# Registrar Cliente Interno Pagina 2
#------------------------------------#

def registrar_cliente_in(request):
    data = {
        'form': ClienteInternoReg()
    }
    if request.method == 'POST':
        salida = ClienteInternoReg(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='login')
    return render(request, 'formularios/formularioclienteinterno.html', data)


# conexion con el PACK_MANT_CLIENTEINTERNO de la base de datos
#--------------------------------------------------------------#

def agregar_clienteInterno():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("PACK_MANT_CLIENTE_INTERNO.SP_AGREGAR_CLIENTE_INTERNO",
                    [rut_cli_ex, nom_clien_in, apellidop_clien_in, apellidom_clientein, direccion_clien_in, ciudad_clien_in, correo_clien_in, numero_cliente_in, pass_cliente, rol_id_rol, salida])
    return salida.getvalue()

#====================================================================================================================#
#--------------------------------CRUD de Cliente Externo-------------------------------------------------------------#
#====================================================================================================================#

# Registrar Cliente Externo Pagina 1
#------------------------------------#


def registrar_cliente_externo(request):
    data = {
        'form': DjangoUserForm()
    }
    if request.method == 'POST':
        formulario = DjangoUserForm(request.POST)
        if formulario.is_valid():
            user = formulario.save()
            username = formulario.cleaned_data.get('username')
            group = Group.objects.get(name="ClienteExterno")
            user.groups.add(group)

        return redirect(to='reg_clienteex')
    return render(request, 'formularios/formularioclientexterno.html', data)

# Registrar Cliente Externo Pagina 2
#------------------------------------#

def registrar_cliente_ex(request):
    data = {
        'form': ClienteExternoReg()
    }
    if request.method == 'POST':
        salida = ClienteExternoReg(request.POST)
        if salida.is_valid():
            salida.save()

        return redirect(to='login')
    return render(request, 'formularios/formularioclientexterno.html', data)


# conexion con el PACK_MANT_CLIENTEXTERNO de la base de datos
#-------------------------------------------------------------#

def agregar_clientexterno(request):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("PACK_MANT_CLIENTE_EXTERNO.SP_AGREGAR_CLIENTE_EXTERNO",
                    [RUT_CLIENTE, NOM_CLIENTE, APELLIDOP_CLIENTE, APELLIDOM_CLIENTE, DIRECCION_RESIDENCIAL, CIUDAD_RESIDENCIAL, CORREO_ELECTRONICO, NUMERO_TELEFONICO, PASS_CLIENTE, ROL_ID_ROL,
                     salida])
    return salida.getvalue()

#====================================================================================================================#    
#---------------------------------CRUD de Productos------------------------------------------------------------------#
#====================================================================================================================#

# Agregar PRODUCTO con PACKAGE
#-----------------------------#

def registrar_producto(request):
    data = {
        'form': ProductoReg()
    }
    if request.method == 'POST': 
        salida = ProductoReg(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='productos')
    return render(request, 'registration/registrarproducto.html', data)

def IngresarProducto(ID_PROD,NOM_PROD,PRECIO_PROD,PESO_PROD, CALIDAD_PROD,PRODUCTOR_RUT_PRODUC):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('PACK_MANT_PRODUCTO.SP_INGRESAR_PRODUCTO',[ID_PROD,NOM_PROD,PRECIO_PROD,PESO_PROD, CALIDAD_PROD,PRODUCTOR_RUT_PRODUC,out_cur])

    return salida.getvalue()

# Listar Productos
#-----------------#

def listar_producto():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cur = django_cursor.connection.cursor()

    cursor.callproc('PACK_MANT_PRODUCTO.SP_LEER_PRODUCTO', [out_cur])
    lista = []
    for fila in out_cur:
        lista.append(fila)
    return lista

#############3### listar productos cliente externo###########################

def productoex(request):  # Para navegacion de home
    data = {
        'productoex': listar_producto()
    }

    if request.method == 'POST':
        ID_PROD = request.POST.get('ID_PROD')
        NOM_PROD = request.POST.get('NOM_PROD')
        PRECIO_PROD = request.POST.get('PRECIO_PROD')
        PESO_PROD = request.POST.get('PESO_PROD')
        CALIDAD_PROD = request.POST.get('CALIDAD_PROD')
        data['productos'] = listar_producto()
    
    return render(request, 'core/productosclienteex.html')

def productos(request):

    data = {
        'productos': listar_producto()
    }

    if request.method == 'POST':
        ID_PROD = request.POST.get('ID_PROD')
        NOM_PROD = request.POST.get('NOM_PROD')
        PRECIO_PROD = request.POST.get('PRECIO_PROD')
        PESO_PROD = request.POST.get('PESO_PROD')
        CALIDAD_PROD = request.POST.get('CALIDAD_PROD')
        data['productos'] = listar_producto()

    return render(request, 'core/productos.html', data)

## Modificar producto con 
#-------------------------------#
def modificarproducto(request, id): 
    producto = Producto.objects.get(id_prod=id)
    data = {
        'form' : ProductoReg(instance=producto)
    }

    if request.method == 'POST':
        formulario = ProductoReg(data=request.POST, instance=producto)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario
            return redirect(to='productos')

    return render(request, 'modificar/modificarproducto.html', data)

## Eliminar producto con PACKAGE

def eliminar_producto(request, id): 
    producto = Producto.objects.get(id_prod=id)
    producto.delete()
    return redirect(to="productos")
#====================================================================================================================#    
#---------------------------------      TIENDA     ------------------------------------------------------------------#
#====================================================================================================================#

#Cliente externo
def tienda(request): 
    products = Producto.objects.all()


    return render(request, "core/tienda.html", {"products":products})

    

#====================================================================================================================#    
#---------------------------------SOLICITUD DE VENTA ----------------------------------------------------------------#
#====================================================================================================================#

# Solicitud Venta

def registrar_solicitud(request):
    data = {
        'form': SolicitudVentaReg()
    }
    if request.method == 'POST': 
        salida = SolicitudVentaReg(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='listado_solicitud_venta')
    return render(request, 'registration/registrarsolicitud.html', data)

def Ingresar_solicitud(ID_SOLI,NUMERO_SOLI,DIRECCION_ENTREGA,CLIENTE_EXTERNO_RUT_CLIENTE):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc('PACK_MANT_SOLICITUD_VTA.SP_INGRESAR_SOLICITUD_VTA',[ID_SOLI,NUMERO_SOLI,DIRECCION_ENTREGA,CLIENTE_EXTERNO_RUT_CLIENTE,out_cur])

    return salida.getvalue()

#Listar 
#------------------#

def listado_solicitud_venta (request):
    solicitud = SolicitudVenta.objects.all()
    data = {
        'solicitud': solicitud
    }
    return render(request, 'core/solicitud_venta.html', data)


#====================================================================================================================#    
#--------------------------------- SUBASTA --------------------------------------------------------------------------#
#====================================================================================================================#
def registrar_subasta (request):
    data = {
        'form': SubastaReg()
    }
    if request.method == 'POST': 
        salida = SubastaReg(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='subasta')
    return render(request, 'registration/registrarsubasta.html', data)


#Listar
#-------------------#

def listado_subasta (request):
    subasta = Subasta.objects.all()
    data = {
        'subasta' : subasta
    }
    return render (request, 'core/subasta.html', data)

#Modificar 
#----------------------#

def modificar_subasta(request, id): 
    subasta = Subasta.objects.get(id_subasta=id)
    data = {
        'form' : SubastaReg(instance=subasta)
    }

    if request.method == 'POST':
        formulario = SubastaReg(data=request.POST, instance=subasta)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Modificado Correctamente"
            data['form'] = formulario

    return render(request, 'modificar/modificarsubasta.html', data)

#Eliminar
#-----------------------#

def eliminar_subasta (request, id):
    subasta = Subasta.objects.get(id_subasta=id)
    subasta.delete()
    return redirect (to="listado_subasta")


#====================================================================================================================#    
#--------------------------------- Proceso de Venta  ----------------------------------------------------------------#
#====================================================================================================================#


#Registro Proceso de Venta
#----------------------------#

def registrar_proceso_venta (request):
    data = {
        'form': ProcesoVentaReg()
    }
    if request.method == 'POST': 
        salida = ProcesoVentaReg(request.POST)
        if salida.is_valid():
            salida.save()

            return redirect(to='listado_proceso_venta')
    return render(request, 'registration/registrarprocesoventa.html', data)


#Listar Proceso de Venta 
#----------------------------#

def listado_proceso_venta (request):
    procesoventa = ProcesoVenta.objects.all()
    data = {
        'procesoventa' : procesoventa
    }
    return render (request, 'core/proceso_venta.html', data)

def eliminar_proceso_venta(request, id):
    procesove = ProcesoVenta.objects.get(id_proceso=id)
    procesove.delete()
    return redirect (to="listado_proceso_venta")



 
 

