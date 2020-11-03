from django import forms
from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class DjangoUserForm(UserCreationForm):
    

    class Meta:
        model = User
        fields = ['username','password1','password2','first_name', 'last_name']

########################## FORM PRODUCTOR ##########################

class ProductorRegisterForm(ModelForm):

    class Meta:
        model = Productor
        fields = ['rut_produc',
                  'nom_produc',
                  'apellidop_produc',
                  'apellidom_produc', 
                  'direccion_produc',
                  'ciudad_produc',
                  'telefono_produc',
                  'correo_produc',
                  'pass_produc',
                  'rol_id_rol']

        labels = {'rut_produc':'Rut',
                  'nom_produc':'Nombre',
                  'apellidop_produc':'Apellido Paterno',
                  'apellidom_produc':'Apellido Materno', 
                  'direccion_produc':'Direccion', 
                  'ciudad_produc':'Ciudad', 
                  'telefono_produc':'Telefono', 
                  'correo_produc':'Correo',
                  'pass_produc':'Repita su Contraseña',
                  'rol_id_rol':'ROL'
                   }
########################## FORM TRANSPORTISTA ##########################

class TransportistaRegisterFrom(ModelForm):

    class Meta:
        model = Transportista
        fields = ['rut_transp',
                  'nombre_transp',
                  'apellidop_transp',
                  'apellidom_transp',
                  'correo_trasp',
                  'telefono_transo',
                  'patente_vehiculo',
                  'capacidad_carga',
                  'refrigeracion',
                  'pass_transp',
                  'rol_id_rol'
                  ]

        labels = {'rut_transp':'Rut',
                  'nombre_transp':'Nombre',
                  'apellidop_transp':'Apellido Paterno',
                  'apellidom_transp':'Apeliido Materno',
                  'correo_trasp':'Correo',
                  'telefono_transo':'Numero Telefonico',
                  'patente_vehiculo':'Patente del Vehiculo',
                  'capacidad_carga':'Capacidad de Carga',
                  'refrigeracion':'Refrigeracion',
                  'pass_transp':'Repita su Contraseña',
                  'rol_id_rol':'Rol'
                  }
                  
########################## FORM CLIENTE INTERNO ##########################


class ClienteInternoReg(ModelForm):

    class Meta:
        model = ClienteInterno
        fields = ['rut_cli_ex',
                  'nom_clien_in',
                  'apellidop_clien_in',
                  'apellidom_clientein', 
                  'direccion_clien_in',
                  'ciudad_clien_in',
                  'correo_clien_in',
                  'numero_cliente_in',
                  'pass_cliente',
                  'rol_id_rol'
                  ]

        labels = {'rut_cli_ex':'Rut',
                  'nom_clien_in':'Nombre',
                  'apellidop_clien_in':'Apellido Paterno',
                  'apellidom_clientein':'Apellido Materno', 
                  'direccion_clien_in':'Direccion', 
                  'ciudad_clien_in':'Ciudad', 
                  'numero_cliente_in':'Telefono', 
                  'correo_clien_in':'Correo',
                  'pass_cliente':'Repita su Contraseña',
                  'rol_id_rol':'ROL'
                   }

########################## FORM CLIENTE EXTERNO ##########################

class ClienteExternoReg(ModelForm):

    class Meta:
        model = ClienteExterno
        fields = ['rut_cliente',
                  'nom_cliente',
                  'apellidop_cliente',
                  'apellidom_cliente', 
                  'direccion_residencial',
                  'ciudad_residencial',
                  'numero_telefonico',
                  'correo_electronico',
                  'pass_cliente',
                  'rol_id_rol']

        labels = {'rut_cliente':'Rut',
                  'nom_cliente':'Nombre',
                  'apellidop_cliente':'Apellido Paterno',
                  'apellidom_cliente':'Apellido Materno', 
                  'direccion_residencial':'Direccion', 
                  'ciudad_residencial':'Ciudad', 
                  'numero_telefonico':'Telefono', 
                  'correo_electronico':'Correo',
                  'pass_cliente':'Repita su Contraseña',
                  'rol_id_rol':'ROL'
                   }

########################## FORM Producto ##########################
class ProductoReg(ModelForm):

    class Meta:
        model = Producto
        fields = ['id_prod',
                  'nom_prod',
                  'precio_prod',
                  'peso_prod',
                  'calidad_prod',
                  'productor_rut_produc'
                  ]

        labels = {'id_prod':'ID',
                  'nom_prod':'Nombre',
                  'precio_prod':'Precio',
                  'peso_prod':'Peso', 
                  'calidad_prod':'Calidad', 
                  'productor_rut_produc':'Productor', 
                   }

########################### FROM Solicitud de Venta #########################

class SolicitudVentaReg(ModelForm):

    class Meta:
        model = SolicitudVenta
        fields = ['id_soli',
                 'numero_soli',
                 'direccion_entrega',
                 'cliente_externo_rut_cliente'
                ]
        labels = {'id_soli':'ID',
                  'numero_soli':'Numero',
                  'direccion_entrega':'Entrega',
                  'cliente_externo_rut_cliente':'Rut Cliente',
                 }


########################## FROM Subasta ######################################

class SubastaReg(ModelForm):

    class Meta:
        model = Subasta
        fields = ['id_subasta',
                  'requisito_subasta',
                  'pedido_venta_cod_pedido',
                  'oferta_transp_cod_ot'
                 ]
        labels = {'id_subasta':'ID',
                  'requisito_subasta':'REQUISITO SUBASTA',
                  'pedido_venta_cod_pedido':'COD_PEDIDO',
                  'oferta_transp_cod_ot':'ID OFERTA TRANSPORTISTA',
                 }


class ProcesoVentaReg(ModelForm):

    class Meta:
        model = ProcesoVenta
        fields = ['id_proceso',
                  'informacion_venta',
                  'contrato_venta_id_cont',
                 ]
        labels = {'id_proceso':'ID',
                  'informacion_venta':'Informacion',
                  'contrato_venta_id_cont':'ID_CONTRATO',
                 }






































